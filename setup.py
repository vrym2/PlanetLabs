from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'Planet API functions'
LONG_DESCRIPTION = 'Functions and modules related to Planet API'

# Setting up
setup(
        name="planet_UoL", 
        version=VERSION,
        author="Vardhan Raj Modi",
        author_email="vardhan609@gmail.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages()
)