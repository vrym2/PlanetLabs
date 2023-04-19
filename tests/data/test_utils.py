from src.data import OilTerminalsBBox

def test_bbox():
    """Testing GeoJson objects"""
    oilterminals = OilTerminalsBBox()
    data = oilterminals.geojson_data()
    assert type(data) is dict
    for _, dict_geojson in data.items():
        keys = list(dict_geojson.keys())
        assert 'coordinates' in keys
        assert 'type' in keys