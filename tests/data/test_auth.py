from src.data import PlanetAuth

def test_planet_auth():
    """Testing planet authentication"""
    session = PlanetAuth()
    assert session.status_code == 200