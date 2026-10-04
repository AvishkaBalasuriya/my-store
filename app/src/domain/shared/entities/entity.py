from dataclasses import dataclass, field
from datetime import UTC, datetime, timedelta
from uuid import UUID, uuid7


@dataclass(eq=False, kw_only=True)
class Entity:
    _id: UUID = field(
        default_factory=lambda: uuid7(),
        doc="Unique identifier for the entity",
    )
    _version: int = field(
        default=1, doc="Version of the entity, incremented on each modification"
    )
    _is_discarded: bool = field(default=False, doc="Mark if entity is discarded")
    _discarded_at: datetime | None = field(
        default=None, doc="Indicates entity discarded date"
    )
    _created_at: datetime = field(
        default_factory=lambda: datetime.now(UTC),
        doc="Entity creation date as UTC datatime object",
    )
    _modified_at: datetime = field(
        default_factory=lambda: datetime.now(UTC),
        doc="Entity modified date as UTC datatime object",
    )

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, type(self)):
            return NotImplemented

        return self._id == other._id

    def __hash__(self) -> int:
        return hash(self._id)

    @property
    def _time_since_discarded(self) -> timedelta:
        if not self._discarded_at:
            return timedelta(0)

        return datetime.now(tz=UTC) - self._discarded_at

    @property
    def _time_since_created(self) -> timedelta:
        return datetime.now(tz=UTC) - self._created_at

    @property
    def _time_since_last_modified(self) -> timedelta:
        return datetime.now(tz=UTC) - self._modified_at

    def _discard(self) -> None:
        self._is_discarded = True
        self._discarded_at = datetime.now(tz=UTC)

    def _retain(self) -> None:
        self._is_discarded = False
        self._discarded_at = None

    def _is_retainable(self, retainable_period_in_days: timedelta) -> bool:
        return not self._is_discarded or (
            self._time_since_discarded < retainable_period_in_days
        )

    def _touch(self) -> None:
        self._version += 1
        self._modified_at = datetime.now(UTC)
