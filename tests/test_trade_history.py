import datetime
import os
import sys
import unittest
import uuid

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from spirit.packets.handlers.trade import (  # noqa: E402
    _offer_to_lot_history, TradeHandler,
)

SENDER = str(uuid.uuid4())
ACCEPTER = str(uuid.uuid4())
CARD_GUID = "11111111-2222-3333-4444-555555555555"
PACK_GUID = "99999999-8888-7777-6666-555555555555"

OFFER = {
    "id": 1,
    "offer_id": str(uuid.uuid4()),
    "sender_id": SENDER,
    "sender_name": "brandon",
    "recipient_id": None,
    "offering": {CARD_GUID: 2},
    "requesting": {PACK_GUID: 5},
    "status": "accepted",
    "accepted_by": ACCEPTER,
    "created_at": "2026-10-07 17:25:04",
}

LOT_HISTORY_KEYS = {
    "id", "offer", "counterOffer", "offeredBy", "acceptedBy",
    "offeredByUsername", "acceptedByUsername", "price",
    "acceptedDttm", "isPrivate", "cardPrice",
}
HISTORY_ITEM_KEYS = {"itemID", "ownerID", "archetypeID", "created", "isTradable"}


class LotHistoryShapeTests(unittest.TestCase):
    """Exact match against core.dll's LotHistory DTO (client decompiled evidence)."""

    def test_entry_has_exact_key_set_and_scalar_types(self):
        names = {SENDER: "brandon", ACCEPTER: "Yashiroe"}
        entry = _offer_to_lot_history(OFFER, names)
        self.assertEqual(set(entry), LOT_HISTORY_KEYS)
        uuid.UUID(entry["id"])
        uuid.UUID(entry["offeredBy"])
        uuid.UUID(entry["acceptedBy"])
        self.assertIsInstance(entry["price"], int)
        self.assertEqual(entry["price"], 0)
        self.assertIsInstance(entry["acceptedDttm"], int)
        self.assertFalse(entry["isPrivate"])
        self.assertEqual(entry["cardPrice"], {PACK_GUID: 5})
        self.assertEqual(entry["offeredByUsername"], "brandon")
        self.assertEqual(entry["acceptedByUsername"], "Yashiroe")

    def test_arrays_one_item_per_copy_with_expected_owners(self):
        entry = _offer_to_lot_history(OFFER, {})
        self.assertEqual(len(entry["offer"]), 2)
        self.assertEqual(len(entry["counterOffer"]), 5)
        for item in entry["offer"]:
            self.assertEqual(set(item), HISTORY_ITEM_KEYS)
            uuid.UUID(item["itemID"])
            uuid.UUID(item["ownerID"])
            uuid.UUID(item["archetypeID"])
            self.assertIsInstance(item["created"], float)
            self.assertTrue(item["isTradable"])
            self.assertEqual(item["ownerID"], SENDER)
            self.assertEqual(item["archetypeID"], CARD_GUID)
        for item in entry["counterOffer"]:
            self.assertEqual(item["ownerID"], ACCEPTER)
            self.assertEqual(item["archetypeID"], PACK_GUID)

    def test_both_arrays_present_when_counts_empty(self):
        entry = _offer_to_lot_history(dict(OFFER, offering={}, requesting={}), {})
        self.assertEqual(entry["offer"], [])
        self.assertEqual(entry["counterOffer"], [])
        self.assertEqual(entry["cardPrice"], {})

    def test_missing_names_render_empty_strings(self):
        entry = _offer_to_lot_history(OFFER, {})
        self.assertEqual(entry["offeredByUsername"], "")
        self.assertEqual(entry["acceptedByUsername"], "")

    def test_accepted_dttm_equals_created_at_epoch_ms(self):
        entry = _offer_to_lot_history(OFFER, {})
        expected = int(datetime.datetime.fromisoformat(
            OFFER["created_at"]).timestamp() * 1000)
        self.assertEqual(entry["acceptedDttm"], expected)

    def test_is_private_reflects_recipient(self):
        private = dict(OFFER, recipient_id=str(uuid.uuid4()))
        self.assertTrue(_offer_to_lot_history(private, {})["isPrivate"])
        self.assertFalse(_offer_to_lot_history(OFFER, {})["isPrivate"])


class LotsPathRegressionTests(unittest.TestCase):
    """The lots panels keep the Lot shape byte-unchanged."""

    def setUp(self):
        # _offer_to_lot never touches self; build a bare instance to call it
        self.handler = object.__new__(TradeHandler)

    def test_offer_to_lot_shape_unchanged(self):
        lot = self.handler._offer_to_lot(OFFER)
        self.assertEqual(set(lot), {
            "id", "items", "price", "owner", "ownerName", "lockID",
            "lockedBy", "lockedByName", "expirationDate", "expirationHR",
            "expirationType", "isDeck", "cardPrice", "message",
        })
        uuid.UUID(lot["id"])
        uuid.UUID(lot["owner"])
        self.assertEqual(lot["ownerName"], "brandon")
        self.assertEqual(len(lot["items"]), 2)
        self.assertEqual(lot["items"][0]["archetypeID"], CARD_GUID)
        self.assertEqual(lot["price"], 0.0)
        self.assertEqual(lot["cardPrice"], {PACK_GUID: 5})
        self.assertEqual(lot["message"], "")
        self.assertFalse(lot["isDeck"])


if __name__ == "__main__":
    unittest.main()
