import os
import asyncio
from planet import Auth, Session
from src.data import planet_search
from pprint import pprint

async def send_request(
        location_name, 
        search_filter,
        download_dir):
    """Function to send request to Planet service"""
    PLANET_APIKEY = os.environ.get('PL_API_KEY')
    client = Auth.from_key(PLANET_APIKEY)
    async with Session() as sess:
        cl = sess.client('data')
        search_json = await cl.create_search(
            name = location_name,
            search_filter = search_filter,
            item_types = ["REOrthoTile", "PSScene"])
        await sess.aclose()
    
    async with Session() as sess:
        cl = sess.client('data')
        items = cl.run_search(
            search_id = search_json['id'],
            limit = 50)
        items_list = [i async for i in items]
        await sess.aclose()

    # Getting a single item
    item = items_list[0]
    item_id = item['id']
    item_type = item['properties']['item_type']
    print(item_id, item_type)
        
start_date = '2023-04-01'
end_date = '2023-04-18'
location_name = 'stanlow'
cloud_cover = 10 
download_dir = 'data' 
search = planet_search()
request = search.build_request(
    start_date = start_date,
    end_date = end_date,
    location_name = location_name,
    cloud_cover = cloud_cover)
asyncio.run(send_request(
    location_name = location_name,
    search_filter = request,
    download_dir = download_dir))