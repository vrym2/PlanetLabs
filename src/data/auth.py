import os
import requests
from planet import Auth

import logging
import logging.config
logging.config.fileConfig('logger.ini')

def PlanetAuth()-> None:
    """Authenticating Planet with API KEY"""
    PL_API_KEY = os.environ.get('PL_API_KEY')
    try:
        assert PL_API_KEY is not None
    except AssertionError as e:
        logging.debug("Make sure to add PLANET APIKEY as the env variable")
    
    # Base URL
    base_url = 'https://api.planet.com/data/v1'
    session = requests.session()
    session.auth = (PL_API_KEY, "")

    # Making a request
    req = session.get(base_url)

    if req.status_code == 200:
        logging.info("Planet data Authentication successful")
        return Auth.from_key(PL_API_KEY)
    else:
        logging.debug("Planet data authentication unsuccessful")
        return None
