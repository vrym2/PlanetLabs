import json
import requests
import pandas as pd
import numpy as np
from typing import List
from datetime import datetime
from requests.auth import HTTPBasicAuth

from planet import data_filter


class planet_search:
    """Class function to retrieve search results"""
    def __init__(self) -> None:
        pass

    def location_bbox(
            self, 
            location_name:str = None)-> None:
        """Getting the location bbox coords"""
        filepath = 'data/oil_terminals_bbox.csv'
        df = pd.read_csv(filepath, header = 1)
        df_row = df.loc[df['location_name'] == location_name]
        bbox = df['bounding_coords'].values[0]

    def results(
            self,
            start_date:str = None,
            end_date:str = None,
            location_name:str = None,
            cloud_cover_range:List[np.int32, np.int32] = None            )-> None:
        """Get the results in JSON"""
        # Date time objects
        start_date = datetime.strptime(start_date, "%y-%m-%d")
        end_date = datetime.strptime(end_date, "%y-%m-%d")      
        date_range = data_filter.date_range_filter(
            field_name = 'acquired',
            gte = start_date,
            lte = end_date)
        
