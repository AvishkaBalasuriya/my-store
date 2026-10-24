import unittest
from datetime import datetime, timedelta, timezone
from uuid import uuid4

from src.domain.shared.entities.entity import Entity
from src.domain.shared.exceptions.entity_exception import (
    EntityAlreadyDiscardedError, EntityCannotBeRetainedError,
    EntityNotDiscardedError, ErrorCodes)


class TestEntityInitialization(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.valid_entity_data = {
            "id": uuid4(),
            "version": 1,
            "created_at": datetime.now(tz=timezone.utc),
            "modified_at": datetime.now(tz=timezone.utc),
            "is_discarded": False,
            "discarded_at": None,
        }

    def test_valid_entity_initialization(self):
        entity = Entity(**self.valid_entity_data)

        self.assertEqual(entity.id, self.valid_entity_data["id"])
        self.assertEqual(entity.version, self.valid_entity_data["version"])
        self.assertEqual(entity.created_at, self.valid_entity_data["created_at"])
        self.assertEqual(entity.modified_at, self.valid_entity_data["modified_at"])
        self.assertEqual(entity.is_discarded, self.valid_entity_data["is_discarded"])
        self.assertEqual(entity.discarded_at, self.valid_entity_data["discarded_at"])

    def test_entity_discarded_state(self):
        entity = Entity(**self.valid_entity_data)
        self.assertFalse(entity.is_discarded)
        self.assertIsNone(entity.discarded_at)

    def test_entity_mark_as_discarded(self):
        entity = Entity(**self.valid_entity_data)
        entity._discard()
        self.assertTrue(entity.is_discarded)
        self.assertIsNotNone(entity.discarded_at)
        self.assertIsInstance(entity.discarded_at, datetime)

    def test_entity_time_since_discarded(self):
        entity = Entity(**self.valid_entity_data)
        entity._discard()
        time_since_discarded = (
            datetime.now(tz=timezone.utc) - entity.discarded_at
        ).total_seconds()
        self.assertGreaterEqual(
            entity.time_since_discarded.total_seconds(), time_since_discarded
        )
        self.assertIsInstance(entity.time_since_discarded, timedelta)

    def test_entity_time_since_discarded_without_discard(self):
        entity = Entity(**self.valid_entity_data)
        self.assertEqual(entity.time_since_discarded.total_seconds(), 0)
        self.assertIsInstance(entity.time_since_discarded, timedelta)

    def test_entity_discard_on_already_discarded(self):
        entity = Entity(**self.valid_entity_data)
        entity._discard()

        with self.assertRaises(EntityAlreadyDiscardedError) as context:
            entity._discard()

            self.assertIn(
                ErrorCodes.ENTITY_ALREADY_DISCARDED_ERROR.message,
                str(context.exception),
            )

    def test_entity_retain_within_retainable_period(self):
        entity = Entity(**self.valid_entity_data)

        entity._discard()
        retainable_period_in_days = timedelta(days=1)
        entity._retain(retainable_period_in_days)

        self.assertFalse(entity.is_discarded)
        self.assertIsNone(entity.discarded_at)

    def test_entity_retain_outside_retainable_period(self):
        entity = Entity(**self.valid_entity_data)

        entity._discard()
        retainable_period_in_days = timedelta(days=1)
        entity.discarded_at -= timedelta(
            days=2
        )  # Simulate that the discard happened 2 days ago

        with self.assertRaises(EntityCannotBeRetainedError) as context:
            entity._retain(retainable_period_in_days)

            self.assertTrue(
                ErrorCodes.ENTITY_CANNOT_BE_RETAINED_ERROR.message
                in str(context.exception)
            )

    def test_entity_retain_without_discard(self):
        entity = Entity(**self.valid_entity_data)

        retainable_period_in_days = timedelta(days=1)

        with self.assertRaises(EntityNotDiscardedError) as context:
            entity._retain(retainable_period_in_days)

            self.assertTrue(
                ErrorCodes.ENTITY_NOT_DISCARDED_ERROR.message in str(context.exception)
            )

    def test_entity_version_increment_on_touch(self):
        entity = Entity(**self.valid_entity_data)
        initial_version = entity.version
        entity._touch()
        entity._touch()
        self.assertEqual(entity.version, initial_version + 2)
        self.assertIsInstance(entity.modified_at, datetime)
