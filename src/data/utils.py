import os
from math import sqrt
import json
import numpy as np
import pandas as pd
import geopandas as gpd
import geojson
from shapely.wkt import loads
from shapely.geometry import mapping

class OilTerminalsBBox:
    """Class functions of terminal data for Planet"""
    terminal_file_path = '/home/vardh/gcp_project/planet_UoL/data/uk_oil_terminals.xlsx'
    assert os.path.exists(terminal_file_path) is True

    def __init__(self) -> None:
        pass

    @staticmethod
    def bounding_box(
            center_lat: np.float64 = None,          
            center_lon: np.float64 = None, 
            half_side: np.int64 = 10, # in Km
            ):
        """
        Function that gives WKT of a polygon from a center lon, lat

        Args:
            center_lat: Centre Latitude
            center_lon: Center Longitude
            half_side: Length from center to side of the bounding box in Km.
        """
        # Sanity check
        assert half_side > 0
        assert center_lat >= -90.0 and center_lat  <= 90.0
        assert center_lon >= -180.0 and center_lon <= 180.0

        # Km to m
        half_side = (half_side*1000)/sqrt(2)

        # Geopandas geo-series
        gs = gpd.GeoSeries(loads(f'POINT({center_lon} {center_lat})'))
        # GeoDataFrame
        gdf = gpd.GeoDataFrame(geometry=gs)
        # Projection
        gdf.crs='EPSG:4326'
        gdf = gdf.to_crs('EPSG:3857')
        res = gdf.buffer(
            distance=half_side,
            cap_style=3,
        )    

        # Get the geom
        geom = res.to_crs('EPSG:4326').iloc[0]
        # Getting Polygon WKT string
        return geom.wkt    

    def geojson_data(self)-> None:
        """Reading the Oil terminal data"""
        # Load the excel file
        df = pd.read_excel(
            self.terminal_file_path,
            skiprows = 1)
        # Getting all the Lat and Lon
        location_geojson = {}
        lat_lon = list(zip(df['Lat'], df['Lon']))
        for index, row in df.iterrows():
            location = row['Region']
            location = location.split(',')[0].lower()
            # Getting the bounding box coords
            wkt_string = OilTerminalsBBox.bounding_box(
                center_lat = lat_lon[index][0],
                center_lon = lat_lon[index][1])
            geojson_string = geojson.dumps(mapping(loads(wkt_string)))
            geojson_dict = json.loads(geojson_string)
            location_geojson[location] = geojson_dict
        return location_geojson


        