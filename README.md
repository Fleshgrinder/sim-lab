# sim-lab

Script that check if the [GT1 EVO Sim Racing Cockpit] is in stock and then shows a Windows Toast that informs you to go and get yours. I highly recommend
that you get an account on their site and put everything in the cart that you want to order along. It remembers your cart’s content if you are registered
and this will speed up your checkout.

## Usage

- Install [Python](https://www.python.org/downloads/windows/): `winget install --id python.python.3`
- Provision `venv`: `python3 -m venv venv`
- Edit the script and assign your email address to the `EMAIL` variable at the top, you want to be a good web citizen and let the Sim-Lab admins know who
  is probing their server over and over again. 😉
- Start the script: `.\venv\Scripts\python.exe .\main.py`
- Have fun!

[GT1 EVO Sim Racing Cockpit]: https://sim-lab.eu/shop/product/slc001-gt1-evo-sim-racing-cockpit-446?category=138
