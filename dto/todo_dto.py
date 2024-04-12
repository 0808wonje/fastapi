from typing import Optional

from pydantic import BaseModel, ConfigDict


class ToDoDto(BaseModel):
    task_data: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)


