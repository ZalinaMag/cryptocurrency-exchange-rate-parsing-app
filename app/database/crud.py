from decimal import Decimal
from database.models import KeyJson

async def create_key_json(data):
    key_json_record = await KeyJson.create(
        title=data["title"],
        kash=data["kash"],
        difference=Decimal(data["difference"]),
        total_amount=Decimal(data["total amount"]),
        date=data["date"],
        coins=data["coins"]
    )
    return key_json_record

async def read_key_json(record_id):
    return await KeyJson.get(id=record_id)

async def update_key_json(record_id, data):
    key_json_record = await KeyJson.get(id=record_id)
    key_json_record.title = data["title"]
    key_json_record.kash = data["kash"]
    key_json_record.difference = Decimal(data["difference"])
    key_json_record.total_amount = Decimal(data["total amount"])
    key_json_record.date = data["date"]
    key_json_record.coins = data["coins"]
    await key_json_record.save()
    return key_json_record

async def delete_key_json(record_id):
    key_json_record = await KeyJson.get(id=record_id)
    await key_json_record.delete()
