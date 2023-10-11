from pydantic import BaseModel
from typing import Optional


class Values(BaseModel):
    nodeid: str
    tds: float
    lat: float
    long: float
    pH: float
    turbidity: float
    timestamp: int


class nullishValues(BaseModel):
    nodeid: Optional[str] = None
    tds: Optional[float] = None
    lat: Optional[float] = None
    long: Optional[float] = None
    pH: Optional[float] = None
    turbidity: Optional[float] = None
    timestamp: Optional[int] = None


class dbGet_id(BaseModel):
    iD: str


class dbPost(BaseModel):
    values: Values


class dbUpdate(BaseModel):
    filter: str
    updateValues: nullishValues


class dbUpdate_id(BaseModel):
    iD: str
    updateValues:Optional[nullishValues] = None


class dbDelete(BaseModel):
    filter: str


class dbDelete_id(BaseModel):
    iD: str
