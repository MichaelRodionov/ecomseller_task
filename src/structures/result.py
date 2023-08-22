from pydantic import BaseModel


# ----------------------------------------------------------------
class ResultStruct(BaseModel):
    item_id: int
    offer_id: str
    name: str
    description: str
