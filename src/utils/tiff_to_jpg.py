import os
import logging
from PIL import Image
from pathlib import Path

logger = logging.getLogger(__name__)

def convert_to_jpg(tif_file:str = None):
    """Function to convert the files into jpg"""
    filename = Path(tif_file).stem
    parent_dir = Path(tif_file).parents[0]

    # Converting into JPG
    logger.info(f"Converting the tiff file:\n{parent_dir}/{filename}")
    im = Image.open(tif_file)
    jpg_file = os.path.join(parent_dir, f'{filename}'+'.jpg')
    rgb_im = im.convert('RGB')
    rgb_im.save(jpg_file)
    logger.info("Finished!")


if __name__ == "__main__":
    location_dir = '/home/vardh/tmp/planet/stanlow'
    tif_files = os.listdir(location_dir)
    for tif in tif_files:
        tif_file = os.path.join(location_dir, tif)
        convert_to_jpg(tif_file = tif_file)