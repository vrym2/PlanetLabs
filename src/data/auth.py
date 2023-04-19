import os
import requests
import logging
from planet import Auth

def PlanetAuth()-> None:
    """Authenticating Planet with API KEY"""
    log = logging.getLogger(__name__)
    PLANET_APIKEY = os.environ.get('PL_API_KEY')
    try:
        assert PLANET_APIKEY is not None
    except AssertionError as e:
        log.debug("Make sure to add PLANET APIKEY as the env variable")
    
    # Base URL
    base_url = 'https://api.planet.com/data/v1'
    session = requests.session()
    session.auth = (PLANET_APIKEY, "")

    # Making a request
    req = session.get(base_url)

    if req.status_code == 200:
        log.info("Planet data Authentication successful")
        return Auth.from_key(PLANET_APIKEY)
    else:
        log.debug("Planet data authentication unsuccessful")
        return None
