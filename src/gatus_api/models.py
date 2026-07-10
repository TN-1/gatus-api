"""Models for Gatus API."""

from dataclasses import dataclass

@dataclass(frozen=True)
class Result:
    """Representation of an endpoint check result."""

    success: bool
    status: int


@dataclass(frozen=True)
class EndpointStatus:
    """Representation of an endpoint status."""

    key: str
    name: str
    group: str | None
    results: list[Result]
