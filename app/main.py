import asyncio
from database.db import init_db, close_db
from services.price_fetcher import process_prices

async def main():
    await init_db()
    previous_totals = {}

    while True:
        previous_totals = await process_prices(previous_totals)
        await asyncio.sleep(120)

    await close_db()

if __name__ == "__main__":
    asyncio.run(main())
