import requests
import csv
import os
import os.path
from os import path
import time
from bs4 import BeautifulSoup

FILE = 'sANDp500.csv'

# load csv file with ticker symbols and names
def getStockTickers():
    tickers = []
    with open(FILE, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        next(reader) # skip header
        for row in reader:
            tickers.append(row[0].split(",")[0])
    return tickers

def downloadData(stock_ticker):
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
    URL = f"https://ca.finance.yahoo.com/quote/{stock_ticker}/profile?p={stock_ticker}"
    resp = requests.get(URL, headers=headers, timeout=5) 
    if resp.status_code == 200:
        soup = BeautifulSoup(resp.content, "lxml")
        raw_data = soup.find_all(class_="quote-sub-section Mt(30px)")
        time.sleep(1) # accounts for api rate limiter
    else:
        raise Exception("error with response")

    return [stock_ticker, raw_data]

def main():
    # create new file for download results
    for i in range(1000):
        if not path.exists(f"./results/results{i}.csv"):
            with open(f"./results/results{i}.csv", mode='w', encoding='utf-8') as data_file:
                data_writer = csv.writer(data_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                tickers = getStockTickers()
                for t in tickers[119:]:
                    print(f"attempting to get data for: {t}")
                    try:
                        individual_data = downloadData(t)
                    except:
                        print("encountered error")
                        break

                    data_writer.writerow(individual_data)
            break   

main()
