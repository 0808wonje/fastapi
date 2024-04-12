from abc import ABC, abstractmethod
from typing import Optional, List

from sqlalchemy.orm import Session

from domain.item_entity import ItemEntity
from dto.item_dto import ItemDto


class ItemRepositoryInterface(ABC):

    @abstractmethod
    def persist_item(self, item: ItemEntity) -> int:
        pass

    @abstractmethod
    def find_item_by_id(self, item_id: int) -> Optional[ItemEntity]:
        pass

    @abstractmethod
    def find_all_item(self, db: Session) -> List[ItemEntity]:
        pass

    @abstractmethod
    def update_item(self, item_id: int, name: str, price: Optional[int], description: Optional[str]) -> None:
        pass

    @abstractmethod
    def remove_item(self, item: ItemEntity) -> None:
        pass

