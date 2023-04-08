from typing import Any, Protocol

from ...domain.user import User


class UserRepository(Protocol):
    def get_by_id(self, id: int) -> User | None:
        ...

    def get_by_username(self, username: str) -> User | None:
        ...

    def get_all(self) -> list[User]:
        ...

    def create(self, payload: dict[str, Any]) -> User:
        ...
