# Welcome to Planet

### Install pre-requisites

Install all the necessary packages and modules listed as per below.
```
$ sudo apt-get install gcc libpq-dev build-essential -y
$ sudo apt-get install python-dev  python-pip -y
$ sudo apt-get install python3-dev python3-pip python3-venv python3-wheel -y
```
```
# Create a virtual environment and make sure to check python version and path
$ which python
$ python -V # Make sure to use python>=3.7
$ sudo pip3 install virtualenv
$ virtualenv planet_UoL/.venv/planet_data
$ source planet_UoL/.venv/planet_data activate
$ python -m pip install wheel
$ python -m pip install --upgrade pip
$ python -m pip install --upgrade setuptools
```

This repo considers data from a corresponding repo regarding (UK oil terminals)[https://github.com/vrym2/UK_oil_terminals]. So, it is advised to install the git repo in virtual environment.
```
$ git clone https://github.com/vrym2/UK_oil_terminals.git
$ cd UK_oil_terminals
$ pip install -r requirements.txt
$ pip install .
```

Follow the (instructions)[https://planet-sdk-for-python-v2.readthedocs.io/en/latest/get-started/quick-start-guide/] to install `planet` API in the `venv`

## Workflow
```
├── data
│   ├── planet_items_scenes_json
│   └── planet_json_reqs
├── src
│   ├── data
│   │   ├── auth.py
│   │   ├── data_request.py
│   │   ├── json_request.py
│   │   ├── planet_download.py
│   │   └── retrieve.py
│   ├── images
│   └── utils
└── tests
    └── data
```

```Authentication(auth.py)--->Building JSON request file(json_request.py)---->retrieving results(data_request.py)--->downloading data(planet_download.py)```

**Note**- Workflow must be followed in order to download the planet data. WHen downloading, it takes time to retrieve the assets, so patience is important. After retrieving assets, the program will fail, saying that `Is asset active?`, the asset will be downloaded when the script is run again.

## Change the default python version
```
$ sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.4 1 #python3.4 is given 1st priority
$ sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.6 2 #python3.6, given second priority
# To change the priorities
$ sudo update-alternatives --config python # And follow the instructions
```
