from termcolor import cprint
from config import *
from main import *

if __name__ == "__main__":

    cprint(RUN_TEXT, RUN_COLOR)
    cprint(f'\nsubscribe to us : https://t.me/hodlmodeth', RUN_COLOR)

    if RM_WALLETS == True:
        random.shuffle(KEYS_LIST)

    for privatekey in KEYS_LIST:

        cprint(f'\n=============== start : {privatekey} ===============', 'white')

        swaps(privatekey, CHAIN)


