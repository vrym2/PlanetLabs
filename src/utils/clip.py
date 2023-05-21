import os
import rasterio
from rasterio.mask import mask
from shapely.geometry import shape

import logging
logger = logging.getLogger(__name__)

from UK_oil_terminals.src import OilTerminals

class raster_clip:
    """Function to clip the raster data"""
    def __init__(
            self,
            raster_file:str = None) -> None:
        """Setting the paths"""
        self.raster_file = raster_file

        # Directory path
        self.dir_name = os.path.dirname(self.raster_file)

        # Getting the name of the tif file
        self.file_name = os.path.basename(self.raster_file)
        self.file_name = self.file_name.split('.')[0]
        self.clip_file_name = f"{self.file_name}_clipped.tif"

        # Path to the clipped file
        self.save_clip_file = os.path.join(self.dir_name, self.clip_file_name)
    
    def bounding_box(self)-> None:
        """Getting the bounding box for clipping"""
        location_name = os.path.basename(self.dir_name)
        oil_terminal = OilTerminals()
        oil_terminal.location_names()
        geo_json = oil_terminal.geojson_data()
        self.location_geom = geo_json[location_name]
    
    def clipped(self)-> None:
        """Clipping the raster file"""
        feature_shape = shape(self.location_geom)
        # Clipping the raster
        with rasterio.open(self.raster_file) as src:
            out_image, out_transform = mask(src, [feature_shape], crop = True)
            out_meta = src.meta

        # Writing the metadata
        out_meta.update({"driver": "GTiff",
            "height": out_image.shape[1],
            "width": out_image.shape[2],
            "transform": out_transform})
        
        # Writing the file
        with rasterio.open(self.save_clip_file, "w", **out_meta) as dest:
            dest.write(out_image)

        try:
            assert os.path.exists(self.save_clip_file)
        except AssertionError:
            logger.debug(f"{self.save_clip_file} has not been clipped!")
        



if __name__ == "__main__":
    raster_file = "data/PS_Scenes/flotta/20230421_110847_34_247d_3B_Visual.tif"
    raster = raster_clip(raster_file)
    raster.bounding_box()
    raster.clipped()
