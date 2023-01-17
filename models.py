from pydantic import BaseModel
from datetime import datetime
from currencies import Currency
from typing import Dict, List


class MetaData(BaseModel):
    time_of_conversion: datetime
    from_currency: Currency
    to_currency: Currency


class Conversion(BaseModel):
    converted_amount: float
    rate: float
    metadata : MetaData