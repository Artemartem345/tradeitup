'''
python3 -m client.main
'''
import asyncio 
import aiohttp
import json
import project.models as test 
from datetime import datetime
from scripts.config import REFRESH_TIME
async def fetch(session, url):
    async with session.get(url) as response:        
        return await response.text()
async def make_request_BTC():
     async with aiohttp.ClientSession() as session:        
        response = await fetch(session, "https://test.deribit.com/api/v2/public/get_index?currency=BTC")
        BTC_course = json.loads(response)       
        db = test.connect_db()
        btc = test.CryptoCourse(currency='BTC', course=BTC_course["result"]["BTC"], time=datetime.utcnow())
        
        db.add(btc)
        db.commit()
        
async def make_request_ETH():
    async with aiohttp.ClientSession() as session:
        response = await fetch(session, "https://test.deribit.com/api/v2/public/get_index?currency=ETH")
        ETH_course = json.loads(response)
        db = test.connect_db()
        eth = test.CryptoCourse(currency='ETH', course=ETH_course["result"]["ETH"], time=datetime.utcnow())
        db.add(eth)
        db.commit()
   
async def run():    
    while True:
        await make_request_BTC()
        await make_request_ETH()        
        await asyncio.sleep(REFRESH_TIME)
        
        

if __name__ == '__main__':
    loop = asyncio.get_event_loop()    
    loop.run_until_complete(run())

    
