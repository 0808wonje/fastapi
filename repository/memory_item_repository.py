from typing import Dict, Optional, List

from domain.item_entity import ItemEntity
from repository.item_repository_interface import ItemRepositoryInterface


class MemoryItemRepository(ItemRepositoryInterface):

    def __init__(self):
        self.memory_db: Dict[int, ItemEntity] = dict()
        self.CURRENT_ITEM_IDX: int = 1

    def persist_item(self, item: ItemEntity) -> int:
        item.set_item_id(self.CURRENT_ITEM_IDX)
        self.memory_db[self.CURRENT_ITEM_IDX] = item
        self.CURRENT_ITEM_IDX += 1
        return item.get_item_id()

    def find_item_by_id(self, item_id: int) -> Optional[ItemEntity]:
        if item_id in self.memory_db.keys():
            item = self.memory_db[item_id]
            return item
        return None

    def find_all_item(self, memory_db) -> List[ItemEntity]:
        item_entity_list = list()
        for key in self.memory_db.keys():
            item_entity_list.append(self.memory_db[key])
        return item_entity_list

    def update_item(self,
                    item: ItemEntity,
                    name: Optional[str] = None,
                    price: Optional[int] = None,
                    description: Optional[str] = None) -> None:
        if name:
            item.change_name(name)
        if price:
            item.change_price(price)
            item.set_tax()
        if description:
            item.change_description(description)
        item.set_update_time()

    def remove_item(self, item: ItemEntity) -> None:
        del self.memory_db[item.get_item_id()]


