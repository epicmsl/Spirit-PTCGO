import datetime
import os
import shutil
import sys
import tempfile
import unittest
import uuid

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sqlalchemy import create_engine  # noqa: E402

_TMP_DIR = tempfile.mkdtemp(prefix="spirit_delete_test_")
_TEST_DB = os.path.join(_TMP_DIR, "test.db").replace("\\", "/")
_TEST_ENGINE = create_engine("sqlite:///" + _TEST_DB)

from spirit.database import connection as _db_connection  # noqa: E402
_db_connection.Session.configure(bind=_TEST_ENGINE)

from spirit.database import (  # noqa: E402
    db_session, Base, Account, Wallet, Deck, Collection, ArchetypeFlag,
    Friendship, CodeRedemptionEntry, RedemptionCode, TradeOffer, VersusProgress,
    DailyLoginProgress, AsyncTournament, TournamentEntry,
    TournamentLeaderboardClaim,
)
from spirit.database.models.quests import QuestAccount, DailyQuest, QuestMatchCredit  # noqa: E402
from spirit.database.admin_data import delete_account  # noqa: E402

Base.metadata.create_all(_TEST_ENGINE)


class DeleteAccountTests(unittest.TestCase):

    def setUp(self):
        with db_session() as s:
            for model in (TradeOffer, CodeRedemptionEntry, RedemptionCode,
                          TournamentLeaderboardClaim, TournamentEntry,
                          AsyncTournament, DailyLoginProgress, VersusProgress,
                          QuestMatchCredit, DailyQuest, QuestAccount, Friendship,
                          ArchetypeFlag, Collection, Deck, Wallet, Account):
                s.query(model).delete(synchronize_session=False)

    def make_account(self, username: str) -> str:
        account_id = str(uuid.uuid4())
        with db_session() as s:
            s.add(Account(account_id=account_id, username=username,
                          password_hash="hash", screen_name=username))
            s.flush()
            s.add(Wallet(account_id=account_id, coins=100))
            s.add(Deck(id=str(uuid.uuid4()), account_id=account_id,
                       name="Test Deck", deck_data={"piles": {}}))
            s.add(Collection(account_id=account_id, archetype_id="A1",
                             tradable_count=2, nontradable_count=1))
            s.add(ArchetypeFlag(account_id=account_id, archetype_id="A1", wanted=1))
            s.add(QuestAccount(account_id=account_id))
            s.add(DailyQuest(quest_id=str(uuid.uuid4()), account_id=account_id,
                             offered_date=datetime.date(2026, 10, 17),
                             definition={"id": "q"}))
            s.add(QuestMatchCredit(account_id=account_id, game_id="g1"))
            s.add(VersusProgress(account_id=account_id, points=10))
            s.add(DailyLoginProgress(account_id=account_id, streak=1))
        return account_id

    def test_delete_removes_account_and_all_data(self):
        account_id = self.make_account("victim_full")
        counts = delete_account(account_id)
        self.assertIsNotNone(counts)
        with db_session() as s:
            self.assertIsNone(s.query(Account).filter_by(account_id=account_id).first())
            for model in (Wallet, Deck, Collection, ArchetypeFlag, QuestAccount,
                          DailyQuest, QuestMatchCredit, VersusProgress, DailyLoginProgress):
                self.assertEqual(s.query(model).count(), 0, model.__name__)

    def test_delete_unknown_account_returns_none(self):
        self.assertIsNone(delete_account("does-not-exist-" + str(uuid.uuid4())))

    def test_delete_keeps_other_accounts_and_global_data(self):
        victim = self.make_account("victim_partial")
        survivor = self.make_account("survivor")
        with db_session() as s:
            s.add(Friendship(account_id=victim, friend_id=survivor, status="accepted"))
            s.add(Friendship(account_id=survivor, friend_id=victim, status="accepted"))
            s.add(RedemptionCode(code_string="CODE1", reward_json={}, max_uses=1, enabled=True))
            s.add(CodeRedemptionEntry(code_string="CODE1", account_id=victim,
                                      redeemed_at=datetime.datetime.now()))
            s.add(TradeOffer(offer_id="o1", sender_id=victim, recipient_id=survivor,
                             offering_json={}, requesting_json={}))
            s.add(AsyncTournament(tournament_id="t1", definition_json={}, enabled=True))
            s.add(TournamentEntry(entry_id="e1", tournament_id="t1",
                                  account_id=victim, deck_json={}))
            s.add(TournamentLeaderboardClaim(tournament_id="t1", account_id=victim, rank=1))

        counts = delete_account(victim)

        self.assertIsNotNone(counts)
        self.assertEqual(counts["friends"], 2)
        self.assertEqual(counts["code_redemption_entries"], 1)
        self.assertEqual(counts["trade_offers"], 1)
        self.assertEqual(counts["tournament_entries"], 1)
        self.assertEqual(counts["tournament_leaderboard_claims"], 1)
        with db_session() as s:
            self.assertEqual(s.query(Account).count(), 1)
            self.assertEqual(s.query(Wallet).count(), 1)
            self.assertEqual(s.query(Deck).count(), 1)
            self.assertEqual(s.query(Collection).count(), 1)
            self.assertEqual(s.query(Friendship).count(), 0)
            self.assertEqual(s.query(CodeRedemptionEntry).count(), 0)
            self.assertEqual(s.query(TradeOffer).count(), 0)
            self.assertEqual(s.query(TournamentEntry).count(), 0)
            self.assertEqual(s.query(TournamentLeaderboardClaim).count(), 0)
            self.assertEqual(s.query(AsyncTournament).count(), 1)
            self.assertEqual(s.query(RedemptionCode).count(), 1)
            self.assertIsNotNone(s.query(Account).filter_by(account_id=survivor).first())

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(_TMP_DIR, ignore_errors=True)


if __name__ == "__main__":
    unittest.main()
