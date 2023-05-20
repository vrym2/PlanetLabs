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
$ python -V
$ python -m venv planet_UoL/.venv/planet_data
$ source planet_UoL/.venv/planet_data activate
$ python -m pip install wheel
```

```
python3.7 -m pip install --upgrade pip
python3 -m pip install --upgrade setuptools
```

## Change the default python version
```
$ sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.4 1 #python3.4 is given 1st priority
$ sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.6 2 #python3.6, given second priority
# To change the priorities
$ sudo update-alternatives --config python # And follow the instructions
```
