import os
import json
import asyncio
from typing import Dict

from planet import Auth, Session
from planet_UoL.src.utils import write_json_data

# Loading the config file
import logging
import logging.config
logging.config.fileConfig('logger.ini')


async def PS_items(
        location_name:str = None, 
        request_json:Dict = None,
        output_dir:str = None):
    """Sending request to API to download the data from Planet API service
        Args:
            location_name: Name of the oil terminal location
            request_json: JSON dict request build from 'quick_search.py'
    """    
    # Planet API Authentication 
    logging.info("Authenticating with API")
    PLANET_APIKEY = os.environ.get('PL_API_KEY')
    assert PLANET_APIKEY is not None
    Auth.from_key(PLANET_APIKEY)

    # Begin the session
    async with Session() as sess:
        cl = sess.client('data')
        logging.info("Creating a search mechanism and running it with API")

        # Creating the search mechanism
        search_json = await cl.create_search(
            name = location_name,
            search_filter = request_json,
            item_types = ["REOrthoTile", "PSScene"])
        
        # Running the search to retrieve results
        items = cl.run_search(
            search_id = search_json['id'],
            limit = 50)
        items_list = [i async for i in items]

        if items_list is None:
            raise Exception("No scenes have been found based on given params")
        
        # Writing JSON data into a file
        write_json_data(items_list, output_dir, location_name)

        # Closing the session
        await sess.aclose()
        return items_list

if __name__ == "__main__":
    output_dir = 'data/planet_items_scenes_json'
    json_requests = 'data/planet_json_reqs'
    for json_file in os.listdir(json_requests):
        if json_file.endswith('.json'):
            with open(os.path.join(json_requests, json_file)) as file:
                request_json = json.load(file)
                asyncio.run(PS_items(
                    location_name = os.path.splitext(json_file)[0],
                    request_json = request_json,
                    output_dir = output_dir))
            file.close()

            