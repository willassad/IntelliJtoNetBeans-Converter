#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

__author__ = "Will Assad"
__copyright__ = "Copyright 2018, Convert"
__credits__ = ["Will Assad", "Devansh Kaloti"]
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "DKSources"
__email__ = "willassadcode@gmail.com"
__status__ = "Production"

import os
import platform

class InstallConvert():

    def __init__(self):
        print('+------------------------------------------------------+')
        print('|             Installing IntelliJ Converter            |')
        print('|                 Developed By DkSources               |')
        print('|                  Edited by Will Assad                |')
        print('+------------------------------------------------------+')


    def setup(self):
        homedir = os.path.expanduser('~')

        if platform.system() == "Darwin":
            self.mac_osx_install_route()
        with open(os.path.join(homedir, "path.txt"),"w") as f:
            f.write(os.getcwd())

    def mac_osx_install_route(self):
        os.system("chmod +x ./main.py")
        os.system('export PATH="$PATH:$HOME/bin"')
        os.system("ln -s " + os.getcwd() + "/main.py /usr/local/bin/convert")


if __name__ == "__main__":
    installer = InstallConvert()
    installer.setup()
    print("INSTALLED successfully.")
