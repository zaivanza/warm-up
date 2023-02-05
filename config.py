import time
import json
import random
from tqdm import tqdm


# NOVA | ARBITRUM | OPTIMISM
CHAIN = 'ARBITRUM'

FROM_AMOUNT = 0.000001 
TO_AMOUNT   = 0.00001
RM_AMOUNT   = random.randint(6, 9) # кол-во цифр после точки
FROM_COIN   = 1
TO_COIN     = 3
SLEEP_FROM  = 100
SLEEP_TO    = 200
RM_WALLETS  = True # False

COINS       = {
    'ARBITRUM' : [
        {'address': '0xf97f4df75117a78c1A5a0DBb814Af92458539FB4',
        'symbol': 'LINK'}, 

        {'address': '0x539bdE0d7Dbd336b79148AA742883198BBF60342',
        'symbol': 'MAGIC'},

        {'address': '0xfc5A1A6EB076a2C7aD06eD22C90d7E710E35ad0a',
        'symbol': 'GMX'},

        {'address': '0x6C2C06790b3E3E3c38e12Ee22F8183b37a13EE55',
        'symbol': 'DPX'},

        {'address': '0x1622bF67e6e5747b81866fE0b85178a93C7F86e3',
        'symbol': 'UMAMI'},

        {'address': '0x10393c20975cF177a3513071bC110f7962CD67da',
        'symbol': 'JONES'},

        {'address': '0x5575552988A3A80504bBaeB1311674fCFd40aD4B',
        'symbol': 'SPA'},

        {'address': '0x51318B7D00db7ACc4026C88c3952B66278B6A67F',
        'symbol': 'PLS' },

        {'address': '0x6694340fc020c5E6B96567843da2df01b2CE1eb6',
        'symbol': 'STG'},

        {'address': '0xFF970A61A04b1cA14834A43f5dE4533eBDDB5CC8',
        'symbol': 'USDC'},

        {'address': '0xB5de3f06aF62D8428a8BF7b4400Ea42aD2E0bc53',
        'symbol': 'BRC'},
    ],
    
    'OPTIMISM' : [
        {'address': '0x4200000000000000000000000000000000000042',
        'symbol': 'OP'},

        {'address': '0x7F5c764cBc14f9669B88837ca1490cCa17c31607',
        'symbol': 'USDC'},

        {'address': '0x94b008aA00579c1307B0EF2c499aD98a8ce58e58',
        'symbol': 'USDT'}
    ],

    'NOVA' : [
        {'address': '0x750ba8b76187092B0D1E87E28daaf484d1b5273b',
        'symbol': 'USDC'},

        {'address': '0x1d05e4e72cD994cdF976181CfB0707345763564d',
        'symbol': 'WBTC'},

        {'address': '0xDA10009cBd5D07dd0CeCc66161FC93D7c9000da1',
        'symbol': 'DAI'},

        {'address': '0x6DcB98f460457fe4952e12779Ba852F82eCC62C1',
        'symbol': 'BRICK'},

        {'address': '0xfe60A48a0bCf4636aFEcC9642a145D2F241A7011',
        'symbol': 'SUSHI'},
    ],
}

with open("private_keys.txt", "r") as f:
    KEYS_LIST = [row.strip() for row in f]



RPCS = [
    {'chain': 'ETH', 'chain_id': 1, 'rpc': 'https://rpc.ankr.com/eth', 'scan': 'https://etherscan.io/tx', 'token': 'ETH'},

    {'chain': 'OPTIMISM', 'chain_id': 10, 'rpc': 'https://rpc.ankr.com/optimism', 'scan': 'https://optimistic.etherscan.io/tx', 'token': 'ETH'},

    {'chain': 'BNB', 'chain_id': 56, 'rpc': 'https://bsc-dataseed.binance.org', 'scan': 'https://bscscan.com/tx', 'token': 'BNB'},

    {'chain': 'MATIC', 'chain_id': 137, 'rpc': 'https://polygon-rpc.com', 'scan': 'https://polygonscan.com/tx', 'token': 'MATIC'},

    {'chain': 'ARBITRUM', 'chain_id': 42161, 'rpc': 'https://arb1.arbitrum.io/rpc', 'scan': 'https://arbiscan.io/tx', 'token': 'ETH'},

    {'chain': 'AVAXC', 'chain_id': 43114, 'rpc': 'https://api.avax.network/ext/bc/C/rpc', 'scan': 'https://snowtrace.io/tx', 'token': 'AVAX'},

    {'chain': 'NOVA', 'chain_id': 42170, 'rpc': 'https://nova.arbitrum.io/rpc', 'scan': 'https://nova.arbiscan.io/tx', 'token': 'ETH'},

    {'chain': 'FTM', 'chain_id': 250, 'rpc': 'https://rpc.ankr.com/fantom', 'scan': 'https://ftmscan.com/tx', 'token': 'FTM'},
]

text1 = '''
 /$$   /$$  /$$$$$$  /$$$$$$$  /$$       /$$      /$$  /$$$$$$  /$$$$$$$ 
| $$  | $$ /$$__  $$| $$__  $$| $$      | $$$    /$$$ /$$__  $$| $$__  $$
| $$  | $$| $$  \ $$| $$  \ $$| $$      | $$$$  /$$$$| $$  \ $$| $$  \ $$
| $$$$$$$$| $$  | $$| $$  | $$| $$      | $$ $$/$$ $$| $$  | $$| $$  | $$
| $$__  $$| $$  | $$| $$  | $$| $$      | $$  $$$| $$| $$  | $$| $$  | $$
| $$  | $$| $$  | $$| $$  | $$| $$      | $$\  $ | $$| $$  | $$| $$  | $$
| $$  | $$|  $$$$$$/| $$$$$$$/| $$$$$$$$| $$ \/  | $$|  $$$$$$/| $$$$$$$/
|__/  |__/ \______/ |_______/ |________/|__/     |__/ \______/ |_______/                                                                                                                                                                                                          
'''

text2 = '''
      ___          ___                                    ___          ___                  
     /\  \        /\  \        _____                     /\  \        /\  \        _____    
     \:\  \      /::\  \      /::\  \                   |::\  \      /::\  \      /::\  \   
      \:\  \    /:/\:\  \    /:/\:\  \                  |:|:\  \    /:/\:\  \    /:/\:\  \  
  ___ /::\  \  /:/  \:\  \  /:/  \:\__\  ___     ___  __|:|\:\  \  /:/  \:\  \  /:/  \:\__\ 
 /\  /:/\:\__\/:/__/ \:\__\/:/__/ \:|__|/\  \   /\__\/::::|_\:\__\/:/__/ \:\__\/:/__/ \:|__|
 \:\/:/  \/__/\:\  \ /:/  /\:\  \ /:/  /\:\  \ /:/  /\:\~~\  \/__/\:\  \ /:/  /\:\  \ /:/  /
  \::/__/      \:\  /:/  /  \:\  /:/  /  \:\  /:/  /  \:\  \       \:\  /:/  /  \:\  /:/  / 
   \:\  \       \:\/:/  /    \:\/:/  /    \:\/:/  /    \:\  \       \:\/:/  /    \:\/:/  /  
    \:\__\       \::/  /      \::/  /      \::/  /      \:\__\       \::/  /      \::/  /   
     \/__/        \/__/        \/__/        \/__/        \/__/        \/__/        \/__/    
'''

texts = [text1, text2]
colors = ['cyan', 'magenta', 'blue']

RUN_TEXT = random.choice(texts)
RUN_COLOR = random.choice(colors)

def intToDecimal(qty, decimal):
    return int(qty * int("".join(["1"] + ["0"]*decimal)))

def check_rpc(chain):
    for elem in RPCS:
        if elem['chain'] == chain:
            RPC = elem['rpc']
            chainId = elem['chain_id']
            scan = elem['scan']
            token = elem['token']

            return {
                'rpc': RPC, 'chain_id': chainId, 'scan': scan, 'token': token
            }

def sleeping(from_sleep, to_sleep):
    x = random.randint(from_sleep, to_sleep)
    for i in tqdm(range(x), desc='sleep ', bar_format='{desc}: {n_fmt}/{total_fmt}'):
        time.sleep(1)

def func_chunks_generators(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i: i + n]

