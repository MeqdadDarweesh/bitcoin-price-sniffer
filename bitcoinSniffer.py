# Project Idea: Bitcoin price program using CoinDesk API with Python.
# Developed By: Meqdad Darweesh

# Importing libraries
import requests as rq
from datetime import datetime
import logging
import objectpath  # Read the library doc: http://objectpath.org/


def get_api_data():

    LOG_FORMAT = '%(levelname)s : %(asctime)s - %(message)s'
    logging.basicConfig(level=logging.DEBUG,
                        format=LOG_FORMAT, filemode='w')  # , datefmt='%d-%b-%y %H:%M:%S'
    logger = logging.getLogger()

    try:
        API_LINK = 'https://api.coindesk.com/v1/bpi/currentprice.json'   # CoinDesk API Link
        API_Data = rq.get(API_LINK)
        logger.debug("Getting API data - Done")

        api_data = API_Data.json()
        logger.debug("Converting API data to JSON - Done")
        return api_data

    except Exception as e:
        print("Exception occurred: ", e)
        logger.debug("Exception occurred.")


def main():

    # Getting the data from API
    data = get_api_data()
    tree_data = objectpath.Tree(data)

    time = tuple(tree_data.execute('$..updated'))

    usd = list((tree_data.execute('$..USD')))
    price = dict(usd[0])
    price_usd = price["rate"]
    price_description = price["description"] + ' - USD'

    print(f"The price in {price_description}: {price_usd}")
    print(f"Time of the price: {time}")


if __name__ == '__main__':
    main()

'''
Add new features to this code, like:
* Price in GBP
* Price in EUR
* Visualize these data :)
'''
