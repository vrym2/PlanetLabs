# Welcome to Planet

### Install pre-requisites
```
$ sudo apt-get install gcc libpq-dev build-essential -y
$ sudo apt-get install python-dev  python-pip -y
$ sudo apt-get install python3-dev python3-pip python3-venv python3-wheel -y
```
```
# Create a virtual environment and make sure to ceck python version and path
$ which python
$ python -V # Make sure to use python>=3.7
$ sudo pip3 install virtualenv
$ virtualenv planet_UoL/.venv/planet_data
$ source planet_UoL/.venv/planet_data activate
$ python -m pip install wheel
$ python -m pip install --upgrade pip
$ python -m pip install --upgrade setuptools
```

Follow the (instructions)[https://planet-sdk-for-python-v2.readthedocs.io/en/latest/get-started/quick-start-guide/] to install `planet` API in the `venv`

## Change the default python version
```
$ sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.4 1 #python3.4 is given 1st priority
$ sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.6 2 #python3.6, given second priority
# To change the priorities
$ sudo update-alternatives --config python # And follow the instructions
```
