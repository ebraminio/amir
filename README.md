# Amir accounting software

Amir accounting program is free (as in freedom) software, and you can change it or even give it to your friends.

Version 0.1 of this program is now available for [Windows](https://launchpad.net/amir/0.1/0.1/+download/Amir-0.1-win32-setup.exe) and Linux operating systems. Program is writen with Python and if you are a programmer then you can run it on other platforms.

Amir is released under the GPL v3 license.

Our sites:
http://www.freeamir.com

https://github.com/Jooyeshgar/amir

https://launchpad.net/amir/

![Screenshot](http://www.freeamir.com/images/thumb/c/cd/Win1.png/727px-Win1.png)


## Installation

```bash
pip install -r requirements.txt
python setup.py install
```

## Installation Using .deb File

To install the latest version of the package you can [download](https://launchpad.net/amir/0.1/0.1/+download/amir_0.2_all.deb) it from Lanchpad and install it.

## Run

```bash
amir
```

## Generate Documentation

To generate documentations first install [doxygen](http://www.doxygen.org/)

```bash
cd doc
make all
```