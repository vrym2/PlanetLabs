from src.data import planet_auth

def test_planet_auth():
    """Testing planet authentication"""
    session = planet_auth()
    assert session.status_code == 200