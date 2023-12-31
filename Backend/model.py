from pydantic import BaseModel
from typing import Optional


class Values(BaseModel):
    vestid: str
    bullet_detected: bool
    lat: float
    long: float
    temp: float
    heartrate: int
    timestamp: int


class nullishValues(BaseModel):
    vestid: Optional[str] = None
    bullet_detected: Optional[bool] = None
    lat: Optional[float] = None
    long: Optional[float] = None
    temp: Optional[float] = None
    heartrate: Optional[int] = None
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
