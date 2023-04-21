import os
import asyncio
from typing import Dict
import logging
import logging.config
from planet import Auth, Session
from src.utils import write_json_data
from src.data import OilTerminalsBBox

# Loading the config file
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
    # Preparing download dir
    download_dir = os.path.join(download_dir,location_name)
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)

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


            # # Retrieving a single scene
            # # TODO add more filtering options here in the future
            # # For the time being, selecting the first scene in the search results
            # item = items_list[0]
            # item_id = item['id']
            # item_type = item['properties']['item_type']
            # asset_types = item['_permissions']
            # asset_types = [asset.split(':')[0] for asset in asset_types]
            # asset_types = [asset.split('.')[1] for asset in asset_types]
            # if not asset_id_type in asset_types:
            #     raise Exception(f"{item}\nAbove item does not have Asset:{asset_id_type}")

            # # Get Asset
            # if download_xml_file:
            #     asset_type_id = f'asset_id_type_xml'
            # else:
            #     asset_type_id = asset_id_type
            # loading = Loader("Getting the Asset.....", "Asset retrieved...")
            # asset_desc = await cl.get_asset(item_type_id=item_type,item_id=item_id, asset_type_id=asset_type_id)
            # loading.stop()
            
            # # Activate Asset
            # loading = Loader("Activating the asset, may take some time....", "That was fast!")
            # await cl.activate_asset(asset=asset_desc)
            # # Wait Asset (this may take some time!)
            # loading = Loader("Wait")
            # await cl.wait_asset(asset=asset_desc)
            # loading.stop()

            # # Download Asset
            # loading = Loader("Downloading the asset.....", "Download finished.......")
            # asset_path = await cl.download_asset(asset=asset_desc, directory=download_dir, overwrite=True)
            # loading.stop()

            # await sess.aclose()