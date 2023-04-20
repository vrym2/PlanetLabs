import numpy as np
from typing import List
from datetime import datetime
from planet import data_filter

from src.data import (
    OilTerminalsBBox, 
    instrument_filter,
    PlanetAuth)


class planet_search:
    """Class function to retrieve search results"""
    def __init__(self) -> None:
        """Declaring variables"""
        pass

    def build_request(
            self,
            start_date:str = None,
            end_date:str = None,
            location_name:str = None,
            cloud_cover:np.int32 = 10)-> None:
        """Get the results in JSON"""

        # Date time objects
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.strptime(end_date, "%Y-%m-%d")

        # Location bounding box
        geom_dict = OilTerminalsBBox()
        geom_dict = geom_dict.geojson_data()
        geom_dict = geom_dict[location_name]

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
        combined_filter = data_filter.and_filter([
            date_range_filter, aoi_set, cloud_cover])
        return combined_filter


        