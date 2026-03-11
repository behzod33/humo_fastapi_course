from pydantic import BaseModel, Field
from typing import Literal, Optional


class AddUser(BaseModel):
    id: int = Field(description='Id in client', gt=0, lt=40)
    name: str = Field(description='Name in client')
    card_type: str = Field(description='Type of card client')
    active: bool = Field(description='Active to client')
    action: Literal['USER', 'DELETE', 'EDIT']


class UpdateUser(BaseModel):
    id: int = Field(description='Id of the client to update or delete param')
    action: Literal['EDIT', 'DELETE']
    name: Optional[str] = Field(None, description='New name (for EDIT)')
    card_type: Optional[str] = Field(None, description='New card type (for EDIT)')
    active: Optional[bool] = Field(None, description='New active status (for EDIT)')
    param_to_delete: Optional[str] = Field(None, description='Parameter to delete (for DELETE)')