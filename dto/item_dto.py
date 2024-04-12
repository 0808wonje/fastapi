import datetime
from pydantic import BaseModel, Field, ConfigDict
from repository.memory_item_repository import *


class ItemDto(BaseModel):
    item_id: int = None
    name: str
    price: int
    description: Optional[str] = None
    tax: Optional[float] = None
    create_time: Optional[datetime.datetime] = None
    update_time: Optional[datetime.datetime] = None

    model_config = ConfigDict(from_attributes=True)




