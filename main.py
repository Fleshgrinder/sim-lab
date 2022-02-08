#!/usr/bin/env python3
import signal
import webbrowser
from argparse import ArgumentParser
from os.path import dirname, realpath
from time import sleep

import requests
from win10toast_click import ToastNotifier

EMAIL = ''
HEADERS = {'User-Agent': f'Mozilla/5.0 (compatible; AvailabilityCheck; +{EMAIL})'}
SLEEP_SECONDS = 60
TOAST_SECONDS = SLEEP_SECONDS * 10
URL = 'https://sim-lab.eu/shop/product/slc001-gt1-evo-sim-racing-cockpit-446'
run = True


def open_url():
    webbrowser.open(URL)


def main():
    global run

    if EMAIL == '':
        raise ValueError('Be a good web citizen and add your email address to the `EMAIL` constant in the script so that the Sim-Lab admins know who is probing their server.')

    def handler(_, __):
        global run
        run = False

    signal.signal(signal.SIGINT, handler)

    i = 0
    with requests.session() as session:
        while run:
            with session.get(URL) as response:
                if 'out_of_stock' in response.text:
                    i += 1
                    print(f'Still not available after {i} checks, continuing...')
                    sleep(SLEEP_SECONDS)
                else:
                    ToastNotifier().show_toast(
                        title='Sim-lab Website Changed',
                        msg='Be quick and get your rig!',
                        icon_path=f'{dirname(realpath(__file__))}/sim-lab.ico',
                        callback_on_click=open_url,
                    )
                    sleep(TOAST_SECONDS)


if __name__ == '__main__':
    main()
