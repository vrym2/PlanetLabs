# Welcome to Planet

## Change the default python version
```
$ sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.4 1 #python3.4 is given 1st priority
$ sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.6 2 #python3.6, given second priority
# To change the priorities
$ sudo update-alternatives --config python # And follow the instructions
```