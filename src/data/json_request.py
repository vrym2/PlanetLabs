import os
import json
import numpy as np
import logging
import logging.config
from datetime import datetime
from planet import data_filter

from src.data import OilTerminalsBBox

# Loading the config file
logging.config.fileConfig('logger.ini')

class planet_search:
    """Class function to retrieve search results"""
    def __init__(
            self,
            location_name:str = None) -> None:
        """Declaring variables"""
        self.location_name = location_name

    def build_request(
            self,
            start_date:str = None,
            end_date:str = None,
            cloud_cover:np.int32 = 10)-> None:
        """Get the results in JSON"""

        # Date time objects
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.strptime(end_date, "%Y-%m-%d")

        # Location bounding box
        geom_dict = OilTerminalsBBox()
        geom_dict.location_names()
        geom_dict = geom_dict.geojson_data()
        geom_dict = geom_dict[self.location_name]

        # Declaring Date range filter for the search 
        date_range_filter= data_filter.date_range_filter(
            field_name = 'acquired',
            gte = start_date,
            lte = end_date)
        # Declaring Geometry bbox filter
        aoi_set = data_filter.geometry_filter(geom = geom_dict)
        # Cloud cover filter
        cloud_cover = data_filter.range_filter('cloud_cover', None, cloud_cover/100)

        # Adding all filters together
        self.combined_filter = data_filter.and_filter([
            date_range_filter, aoi_set, cloud_cover])
        return self.combined_filter
    
    def write_json(self,output_dir:str = None)-> None:
        """Write the data into json files"""
        write_path = os.path.join(output_dir, self.location_name)
        if not os.path.exists(write_path):
            logging.info(f"Writing {self.location_name}.json build request file")
            logging.info(f"Find the file here : {write_path}")
            with open(write_path, 'w') as f:
                json_data = json.dumps(self.combined_filter, indent = 4)
                f.write(json_data)
                f.close()
            logging.info("Finished!")
        else:
            logging.debug(f"{self.location_name}.json already exists")

if __name__ == "__main__":
    start_date = "2023-03-01"
    end_date = "2023-04-18"
    output_dir = "data/planet_json_reqs"
    oil_terminal = OilTerminalsBBox()
    location_data = oil_terminal.location_names()
    for location_name in location_data:
        search = planet_search(
            location_name = location_name)
        search.build_request(
            start_date = start_date,
            end_date = end_date)
        search.write_json(output_dir = output_dir)