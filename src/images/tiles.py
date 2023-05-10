from PIL import Image
import numpy as np
import os
from pathlib import Path
from itertools import product

def image_tiles(
        path_to_image:str = None,
        splits:np.int32 = None,
        dir_out:str = None):
    """Function to slice an image to equal sized tiles"""
    filename = Path(path_to_image).stem
    parent_dir = Path(path_to_image).parents[0]

    img = Image.open(path_to_image)
    img_height, img_width = img.size     

    grid = product(range(0, img_height-img_height%splits, splits), range(0, img_width-img_width%splits, splits))
    for i, j in grid:
        box = (j, i, j+splits, i+splits)
        out = os.path.join(dir_out, f'{filename}_{i}_{j}.jpg')

        img.crop(box).save(out)    
if __name__ == "__main__":
    path_to_image = '/home/vardh/tmp/planet/stanlow/20230420_111156_17_2402_3B_Visual.jpg'
    dir_out = '/home/vardh/tmp/planet/stanlow/image_patches'
    splits = 250
    image_tiles(path_to_image, splits, dir_out)