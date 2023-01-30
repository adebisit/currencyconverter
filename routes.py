from fastapi import APIRouter, Body, Request, Response, HTTPException, status, Depends
from fastapi.encoders import jsonable_encoder
from typing import List
from currencies import Currency
from models import Conversion
import requests
from lxml import html
from datetime import datetime
from pytz import timezone
import database


router = APIRouter()


@router.get("/currencies")
async def currencies():
    data = {e.name : e for e in Currency}
    return data


@router.get("/convert")
async def convert(
    request: Request,
    amount: int = 1,
    from_currency: Currency = Currency.British_Pound_Sterling,
    to_currency: Currency = Currency.US_Dollar
) -> Conversion:
    resp = requests.get(
        f'https://wise.com/gb/currency-converter/{from_currency.lower()}-to-{to_currency.lower()}-rate?amount=1'
    )
    html_content = html.fromstring(resp.text)
    mid_rates = html_content.xpath('//*[@id="calculator"]//span[@class="text-success"]/text()')
    mid_rate = float(''.join(mid_rates).strip())
    response = {
        "converted_amount": round(amount * mid_rate, 2),
        "rate": mid_rate,
        "metadata": {
            "time_of_conversion": datetime.now(timezone("UTC")),
            "from_currency": from_currency,
            "to_currency": to_currency
        }
    }
    # request.app.database["conversions"].insert_one(jsonable_encoder(response))
    database.db["conversions"].insert_one(jsonable_encoder(response))
    return response


@router.get("/history")
async def history(request: Request) -> List[Conversion]:
    # conversions = list(request.app.database["conversions"].find())
    conversions = list(database.db["conversions"].find())
    return conversions
