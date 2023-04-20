from src.data import planet_search, json_request
from pprint import pprint

def test_quick_search():
    """Testing quick search of Planet catalog"""
    start_date = '2023-01-01'
    end_date = '2023-04-18'
    location_name = 'stanlow'
    cloud_cover = 10
    search = planet_search()
    request = search.build_request(
        start_date = start_date,
        end_date = end_date,
        location_name = location_name,
        cloud_cover = cloud_cover)
    assert request is not None
