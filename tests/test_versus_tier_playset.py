import os
import sys
import tempfile
import unittest
import uuid

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sqlalchemy import create_engine  # noqa: E402

_TMP_DIR = tempfile.mkdtemp(prefix="spirit_playset_test_")
_TEST_DB = os.path.join(_TMP_DIR, "test.db").replace("\\", "/")
_TEST_ENGINE = create_engine("sqlite:///" + _TEST_DB)

from spirit.database import connection as _db_connection  # noqa: E402
_db_connection.Session.configure(bind=_TEST_ENGINE)

from spirit.database import (  # noqa: E402
    db_session, Base, Wallet, Collection, VersusProgress,
)
from spirit.database.versus_data import (  # noqa: E402
    _grant_rewards_in_session, award_match_points,
)
from spirit.game.models.versus import Reward, VersusTier, VersusSeason  # noqa: E402

Base.metadata.create_all(_TEST_ENGINE)

GENESECT = "cb9ff20d-68e5-541f-a08d-1d155c7e6605"
OTHER_CARD = "11111111-2222-3333-4444-555555555555"


def _playset_season():
    """One tier at 80 granting the same archetype three times (a playset split
    across rows) plus tokens, and one tier at 85 granting a different card."""
    tier = VersusTier(rewards={
        80: [Reward("Genesect V", "Archetype", 1, GENESECT),
             Reward("Genesect V", "Archetype", 1, GENESECT),
             Reward("Genesect V", "Archetype", 1, GENESECT),
             Reward("5000 Tokens", "Tokens", 5000, None, "prizeTrainerCoin")],
        85: [Reward("Other Card", "Archetype", 2, OTHER_CARD)],
    })
    return VersusSeason(season_id="TestSeason", start_time=0, end_time=0,
                        description={"id": "test"}, tiers=[tier])


def _multi_threshold_season():
    """Two thresholds both granting the same archetype and tokens, so a single
    award crossing both exercises the shared-session merge paths."""
    tier = VersusTier(rewards={
        78: [Reward("Genesect V", "Archetype", 1, GENESECT),
             Reward("Genesect V", "Archetype", 1, GENESECT),
             Reward("300 Tokens", "Tokens", 300, None, "prizeTrainerCoin")],
        80: [Reward("Genesect V", "Archetype", 1, GENESECT),
             Reward("Genesect V", "Archetype", 1, GENESECT),
             Reward("Genesect V", "Archetype", 1, GENESECT),
             Reward("5000 Tokens", "Tokens", 5000, None, "prizeTrainerCoin")],
    })
    return VersusSeason(season_id="TestSeason", start_time=0, end_time=0,
                        description={"id": "test"}, tiers=[tier])


class PlaysetGrantTests(unittest.TestCase):

    def setUp(self):
        with db_session() as s:
            for model in (Collection, Wallet, VersusProgress):
                s.query(model).delete(synchronize_session=False)

    def _seed_progress(self, account_id, points, granted=None):
        with db_session() as s:
            s.add(VersusProgress(account_id=account_id, season_id="TestSeason",
                                 points=points, all_time_points=points,
                                 granted_json=granted or {}))

    def _collection_rows(self, account_id, archetype_id=None):
        with db_session() as s:
            query = s.query(Collection).filter_by(account_id=account_id)
            if archetype_id is not None:
                query = query.filter_by(archetype_id=archetype_id)
            return [(r.archetype_id, r.tradable_count, r.nontradable_count)
                    for r in query.all()]

    def test_playset_grants_single_row(self):
        account_id = str(uuid.uuid4())
        self._seed_progress(account_id, 75, {"70": True})
        result = award_match_points(account_id, won=True, season=_playset_season())
        self.assertEqual(result["points"], 80)
        self.assertEqual(len(result["granted"]), 4)
        self.assertEqual(self._collection_rows(account_id),
                         [(GENESECT, 0, 3)])
        with db_session() as s:
            row = s.query(VersusProgress).filter_by(account_id=account_id).first()
            self.assertTrue(row.granted_json.get("80"))
            self.assertEqual(row.all_time_points, 80)
            wallet = s.query(Wallet).filter_by(account_id=account_id).first()
            self.assertEqual(wallet.coins, 5000)

    def test_playset_merges_into_existing_row(self):
        account_id = str(uuid.uuid4())
        with db_session() as s:
            s.add(Collection(account_id=account_id, archetype_id=GENESECT,
                             tradable_count=0, nontradable_count=1))
        self._seed_progress(account_id, 75)
        result = award_match_points(account_id, won=True, season=_playset_season())
        self.assertEqual(result["points"], 80)
        self.assertEqual(self._collection_rows(account_id, GENESECT),
                         [(GENESECT, 0, 4)])

    def test_repeated_wins_do_not_double_grant(self):
        account_id = str(uuid.uuid4())
        self._seed_progress(account_id, 75)
        season = _playset_season()
        award_match_points(account_id, won=True, season=season)
        award_match_points(account_id, won=True, season=season)
        award_match_points(account_id, won=True, season=season)
        self.assertEqual(
            sorted(self._collection_rows(account_id)),
            [(OTHER_CARD, 0, 2), (GENESECT, 0, 3)])
        with db_session() as s:
            row = s.query(VersusProgress).filter_by(account_id=account_id).first()
            self.assertEqual(row.points, 90)
            self.assertTrue(row.granted_json.get("80"))
            self.assertTrue(row.granted_json.get("85"))
            wallet = s.query(Wallet).filter_by(account_id=account_id).first()
            self.assertEqual(wallet.coins, 5000)

    def test_one_award_crossing_two_thresholds_merges(self):
        account_id = str(uuid.uuid4())
        self._seed_progress(account_id, 75)
        result = award_match_points(account_id, won=True,
                                    season=_multi_threshold_season())
        self.assertEqual(result["points"], 80)
        # one row for the shared archetype across both thresholds
        self.assertEqual(self._collection_rows(account_id),
                         [(GENESECT, 0, 5)])
        with db_session() as s:
            row = s.query(VersusProgress).filter_by(account_id=account_id).first()
            self.assertTrue(row.granted_json.get("78"))
            self.assertTrue(row.granted_json.get("80"))
            wallets = s.query(Wallet).filter_by(account_id=account_id).all()
            self.assertEqual(len(wallets), 1)
            self.assertEqual(wallets[0].coins, 5300)

    def test_helper_aggregates_duplicate_dict_rewards(self):
        # tournament prize tables call the helper directly with versus-shape dicts
        account_id = str(uuid.uuid4())
        rewards = [
            {"name": "Genesect V", "rewardType": "Archetype",
             "rewardAmount": 1, "rewardProductID": GENESECT,
             "rewardCurrency": "", "rewardDescription": {"id": ""}, "index": 0},
            {"name": "Genesect V", "rewardType": "Archetype",
             "rewardAmount": 1, "rewardProductID": GENESECT,
             "rewardCurrency": "", "rewardDescription": {"id": ""}, "index": 1},
            {"name": "Genesect V", "rewardType": "Archetype",
             "rewardAmount": 1, "rewardProductID": GENESECT,
             "rewardCurrency": "", "rewardDescription": {"id": ""}, "index": 2},
        ]
        with db_session() as s:
            _grant_rewards_in_session(s, account_id, rewards)
        self.assertEqual(self._collection_rows(account_id),
                         [(GENESECT, 0, 3)])

    def test_helper_sums_amounts_for_repeated_archetype(self):
        account_id = str(uuid.uuid4())
        rewards = [
            {"name": "Pack", "rewardType": "Archetype",
             "rewardAmount": 4, "rewardProductID": GENESECT,
             "rewardCurrency": "", "rewardDescription": {"id": ""}, "index": 0},
            {"name": "Pack", "rewardType": "Archetype",
             "rewardAmount": 5, "rewardProductID": GENESECT,
             "rewardCurrency": "", "rewardDescription": {"id": ""}, "index": 1},
        ]
        with db_session() as s:
            _grant_rewards_in_session(s, account_id, rewards)
        self.assertEqual(self._collection_rows(account_id),
                         [(GENESECT, 0, 9)])


if __name__ == "__main__":
    unittest.main()
