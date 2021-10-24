from dotenv import load_dotenv
import os
from binance import AsyncClient
import random


load_dotenv()
BINANCE_API = os.getenv("BINANCE_API_KEY")
BINANCE_SEKRET = os.getenv("BINANCE_SECRET_KEY")


async def fetch_pair_price(crypto_pair):
    # initialise the client
    client = await AsyncClient.create(BINANCE_API, BINANCE_SEKRET)
    cost = await client.get_symbol_ticker(symbol=crypto_pair)
    
    # price = await client.get_all_tickers()

    await client.close_connection()
    return f"{cost['symbol']}\n{cost['price']}\n"


async def fetch_20pairs():
    # initialise the client
    client = await AsyncClient.create(BINANCE_API, BINANCE_SEKRET)
    
    pairs = await client.get_all_tickers()
    pair_list = [symbol['symbol'] for symbol in pairs]

    await client.close_connection()
    return str(random.sample(pair_list, 20))[1:-1]

    