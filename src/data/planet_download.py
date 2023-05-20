import os
import json
import asyncio
import logging
import logging.config
from planet import Auth, Session
from typing import List
from src.utils import Loader
from .retreive import filter_data
from planet.exceptions import ClientError

# Loading the config file
logging.config.fileConfig('logger.ini')


async def data_download(
        scenes_list: List = None,
        asset_type:str = 'ortho_visual',
        download_dir:str = None):
    """Function to download Planet data
    
    Args:
        scenes_id_lis: List of Planet scenes in JSON format
        asset_type: Any asset type in Planet catalog
        https://developers.planet.com/docs/apis/data/items-assets/
        download_dir: Directory to download the data
    """
    # Planet API Authentication 
    logging.info("Authenticating with API")
    PLANET_APIKEY = os.environ.get('PL_API_KEY')
    assert PLANET_APIKEY is not None
    Auth.from_key(PLANET_APIKEY)
    
    # Begin the session
    async with Session() as sess:
        cl = sess.client('data')
        for scene in scenes_list:
            scene_id = scene['id']
            item_type = scene['properties']['item_type']            
            asset_types = scene['_permissions']    
            asset_types = [asset.split(':')[0] for asset in asset_types]
            asset_types = [asset.split('.')[1] for asset in asset_types]    
            if not asset_type in asset_types:
                raise Exception(f"{scene}\nAbove item does not have Asset:{asset_type}")                            

            try:
                loading = Loader("Getting the Asset.....", "Asset retrieved...")
                asset_desc = await cl.get_asset(item_type_id=item_type,item_id=scene_id, asset_type_id=asset_type)
                loading.stop()

            except ClientError as e:
                if str(e) == 'asset missing ["location"] entry. Is asset active?':
                    pass
                else:
                    raise Exception


            # Activate Asset
            loading = Loader("Activating the asset, may take some time....", "That was fast!")
            await cl.activate_asset(asset=asset_desc)
            # Wait Asset (this may take some time!)
            loading = Loader("Wait")
            await cl.wait_asset(asset=asset_desc)
            loading.stop()

            # Download Asset
            loading = Loader("Downloading the asset.....", "Download finished.......")
            asset_path = await cl.download_asset(asset=asset_desc, directory=download_dir, overwrite=True)
            loading.stop()

        await sess.aclose()
        logging.info("Session closed")

if __name__ == "__main__":
    planet_items_scenes_json = 'data/planet_items_scenes_json/stanlow.json'
    download_dir = '/home/vardh/tmp/planet/stanlow'
    scene_id_list = [
        '20230420_111158_20_2402',
        '20230420_111156_17_2402']
    data = filter_data(planet_items_scenes_json)
    scenes_list = data.filter_with_scene_id(scene_id_list)
    asyncio.run(data_download(scenes_list = scenes_list, download_dir = download_dir))
