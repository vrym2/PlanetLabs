import os
import json
import asyncio
import logging
import logging.config
from typing import List, Dict

# Loading the config file
logging.config.fileConfig('logger.ini')


async def data_download(
        search_json: dict = None):
    """Function to download Planet data
    
    Args:
        Path to JSON data file with search results
    """
    # Reading the JSON file
    with open(search_json, 'r') as scenes:
        json_scenes = json.load(scenes)
    
    # Filtering scenes
    clear_confidence = filter(lambda a: a['properties']['clear_confidence_percent'] > 50, json_scenes)
    if len(clear_confidence) == 0:
        raise Exception(f"There are no scenes with clear confidence greater than 50")
    return list(clear_confidence)
