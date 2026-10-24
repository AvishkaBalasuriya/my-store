from dataclasses import dataclass, field
from datetime import UTC, datetime, timedelta
from typing import Optional
from uuid import UUID, uuid4

from src.domain.shared.exceptions.entity_exception import (
    EntityAlreadyDiscardedError, EntityCannotBeRetainedError,
    EntityNotDiscardedError)
from src.domain.shared.exceptions.error_codes import ErrorCodes


@dataclass(eq=False, kw_only=True)
class Entity:
    id: Optional[UUID] = field(
        default_factory=lambda: uuid4(),
        doc="Unique identifier for the entity",
    )
    version: Optional[int] = field(
        default=1, doc="Version of the entity, incremented on each modification"
    )
    created_at: Optional[datetime] = field(
        default_factory=lambda: datetime.now(UTC),
        doc="Entity creation date as UTC datatime object",
    )
    modified_at: Optional[datetime] = field(
        default=None,
        doc="Entity modified date as UTC datatime object",
    )
    is_discarded: Optional[bool] = field(default=False, doc="Mark if entity is discarded")
    discarded_at: Optional[datetime] = field(
        default=None, doc="Indicates entity discarded date"
    )

    @property
    def time_since_discarded(self) -> timedelta:
        if not self.discarded_at:
            return timedelta(0)

        return datetime.now(tz=UTC) - self.discarded_at

    @property
    def time_since_created(self) -> timedelta:
        return datetime.now(tz=UTC) - self.created_at

    @property
    def time_since_last_modified(self) -> timedelta:
        return datetime.now(tz=UTC) - self.modified_at

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, type(self)):
            return NotImplemented

        return self.id == other.id

    def __hash__(self) -> int:
        return hash(self.id)

    def _touch(self) -> None:
        self.version += 1
        self.modified_at = datetime.now(tz=UTC)

    def _discard(self) -> None:
        if self.is_discarded:
            raise EntityAlreadyDiscardedError(
                message=ErrorCodes.ENTITY_ALREADY_DISCARDED_ERROR.message,
                short_desc=ErrorCodes.ENTITY_ALREADY_DISCARDED_ERROR.short_desc,
                code=ErrorCodes.ENTITY_ALREADY_DISCARDED_ERROR.status_code,
            )

        self.is_discarded = True
        self.discarded_at = datetime.now(tz=UTC)
        self._touch()

    def _retain(self, retainable_period_in_days: timedelta) -> None:
        if not self.is_discarded:
            raise EntityNotDiscardedError(
                message=ErrorCodes.ENTITY_NOT_DISCARDED_ERROR.message,
                short_desc=ErrorCodes.ENTITY_NOT_DISCARDED_ERROR.short_desc,
                code=ErrorCodes.ENTITY_NOT_DISCARDED_ERROR.status_code,
            )

        if not self.is_retainable(retainable_period_in_days):
            raise EntityCannotBeRetainedError(
                message=ErrorCodes.ENTITY_CANNOT_BE_RETAINED_ERROR.message,
                short_desc=ErrorCodes.ENTITY_CANNOT_BE_RETAINED_ERROR.short_desc,
                code=ErrorCodes.ENTITY_CANNOT_BE_RETAINED_ERROR.status_code,
            )

        self.is_discarded = False
        self.discarded_at = None
        self._touch()

    def is_retainable(self, retainable_period_in_days: timedelta) -> bool:
        return not self.is_discarded or (
            self.time_since_discarded < retainable_period_in_days
        )
