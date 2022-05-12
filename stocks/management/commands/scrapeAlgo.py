from django.core.management.base import BaseCommand, CommandError
import requests
import pandas as pd  
import numpy as np  
import yfinance as yf  
import datetime as dt 
from pandas_datareader import data as pdr 
from stocks.models import Stock, StockPrice

stockList = [
    {
        "companyName": "Tesla",
        "ticker": "TSLA",
        "logo": "tesla.png"
    },
    {
        "companyName": "Microsoft",
        "ticker": "MSFT",
        "logo": "microsoft.png"

    },
    {
        "companyName": "Advanced Micro Devices",
        "ticker": "AMD",
        "logo": "amd.png"

    },
    {
        "companyName": "Amazon",
        "ticker": "AMZN",
        "logo": "amzn.png"

    },
    {
        "companyName": "Apple",
        "ticker": "AAPL",
        "logo": "appl.png"
    },
    {
        "companyName": "Adobe",
        "ticker": "ADBE",
        "logo": "adobe.png"

    },
    {
        "companyName": "Activision Blizzard",
        "ticker": "ATVI",
        "logo": "Activision.png"

    },
    {
        "companyName": "Broadcom",
        "ticker": "AVGO",
        "logo": "Broadcom.png"

    },
    {
        "companyName": "Biogen",
        "ticker": "BIDU",
        "logo": "Biogen.png"

    },
    {
        "companyName": "Chipotle Mexican Grill",
        "ticker": "CMG",
        "logo": "chipotle.png"

    },
    {
        "companyName": "Charter Communications",
        "ticker": "CHTR",
        "logo": "Charter.png"
    },
    {
        "companyName": "Comcast",
        "ticker": "CMCSA",
        "logo": "cumcast.png"

    },
    {
        "companyName": "Costco",
        "ticker": "COST",
        "logo": "costco.png"

    },
    {
        "companyName": "Cisco",
        "ticker": "CSCO",
        "logo": "cisco.png"

    },
    {
        "companyName": "Dollar Tree",
        "ticker": "DLTR",
        "logo": "dollartree.png"
    },
    {
        "companyName": "Chevron Corporation",
        "ticker": "CVX",
        "logo": "chevron.png"
    },
    {
        "companyName": "DexCom",
        "ticker": "DXCM",
        "logo": "dexcom.png"
    },
    {
        "companyName": "Electronic Arts",
        "ticker": "EA",
        "logo": "ea.png"
    },
    {
        "companyName": "eBay",
        "ticker": "EBAY",
        "logo": "ebay.png"
    },
    {
        "companyName": "Execlon Corporation",
        "ticker": "EXC",
        "logo": "Exelon.png"
    },
    {
        "companyName": "Fastenal",
        "ticker": "FAST",
        "logo": "fastenal.png"
    },
    {
        "companyName": "Meta Platforms",
        "ticker": "FB",
        "logo": "meta.png"
    },
    {
        "companyName": "Verizon",
        "ticker": "VZ",
        "logo": "verizon.png"
    },
    {
        "companyName": "Boeing Co",
        "ticker": "BA",
        "logo": "Boeing.png"
    },
    {
        "companyName": "Alphabet INC. Class A",
        "ticker": "GOOGL",
        "logo": "google.png"
    },
    {
        "companyName": "Corsair",
        "ticker": "CRSR",
        "logo": "corsair.png"
    },
    {
        "companyName": "Intel Corporation",
        "ticker": "INTC",
        "logo": "intel.png"
    },
    {
        "companyName": "Ford",
        "ticker": "F",
        "logo": "ford.png"
    },
    {
        "companyName": "Keurig Dr Pepper Inc",
        "ticker": "KDP",
        "logo": "kdp.png"
    },
    {
        "companyName": "The Kraft Heinz",
        "ticker": "KHC",
        "logo": "kraft.png"
    },
    {
        "companyName": "Lucid Group Inc",
        "ticker": "LCID",
        "logo": "lucidGroup.png"
    },
    {
        "companyName": "Luluemon athletica Inc",
        "ticker": "LULU",
        "logo": "lulu.png"
    },
    {
        "companyName": "Marriot International Class A",
        "ticker": "MAR",
        "logo": "marriott.png"
    },
    {
        "companyName": "Microchip Technology",
        "ticker": "MCHP",
        "logo": "microchip.png"
    },
    {
        "companyName": "Monster Beverage Corporation",
        "ticker": "MNST",
        "logo": "monster.png"
    },
    {
        "companyName": "Moderna",
        "ticker": "MRNA",
        "logo": "Moderna.png"
    },
    {
        "companyName": "Marvell Technology",
        "ticker": "MRVL",
        "logo": "marvell.png"
    },
    {
        "companyName": "Micron technology",
        "ticker": "MU",
        "logo": "micron.png"
    },
    {
        "companyName": "Netflix",
        "ticker": "NFLX",
        "logo": "netflix.png"
    },
    {
        "companyName": "NVIDIA Corporation",
        "ticker": "NVDA",
        "logo": "Nvidia.png"
    },
    {
        "companyName": "General Motors Company",
        "ticker": "GM",
        "logo": "GeneralMotors.png"
    },
    {
        "companyName": "O'Reilly Automotive",
        "ticker": "ORLY",
        "logo": "Oriellys.png"
    },
    {
        "companyName": "Disney",
        "ticker": "DIS",
        "logo": "disney.png"
    },
    {
        "companyName": "AT&T",
        "ticker": "T",
        "logo": "at&t.png"
    },
    {
        "companyName": "Coca-Cola",
        "ticker": "COKE",
        "logo": "coke.png"
    },
    {
        "companyName": "PepsiCo Inc",
        "ticker": "PEP",
        "logo": "pepsi.png"
    },
    {
        "companyName": "PayPal Holding",
        "ticker": "PYPL",
        "logo": "paypal.png"
    },
    {
        "companyName": "QUALCOMM Incorporated",
        "ticker": "QCOM",
        "logo": "qualcomm.png"
    },
    {
        "companyName": "FedEx",
        "ticker": "FDX",
        "logo": "fedex.png"
    },
    {
        "companyName": "Hilton",
        "ticker": "HLT",
        "logo": "hilton.png"
    },
    {
    "companyName": "Robinhood",
    "ticker": "HOOD"
},
]

class Command(BaseCommand):
    def handle(self,*args,**options):
        Stock.objects.all().delete()
        print("scrape stocks ")
        for stock in stockList:
            startyear = 2019
            startmonth = 1
            startday = 1
            start = dt.datetime(startyear, startmonth, startday)
            now = dt.datetime.now()
            df = pdr.get_data_yahoo(stock['ticker'], start, now)
            closingPrice = None
            stockInstance = Stock.objects.create(
                companyName=stock['companyName'],
                ticker=stock['ticker'],
                logo=stock['logo'],
                mostRecentPrice=None
            )
            
            for row in df.index:
                high = df["High"][row]
                low = df["Low"][row]
                open = df["Open"][row]
                close = df["Close"][row]
                volume = df["Volume"][row]
                adjclose = df["Adj Close"][row]
                date = str(row)
                year = date[0:4]
                month = date[5:7]
                day = date[8:10]
                closingPrice = close
                print("high: ",high," low: ",low," open: ",open," close: ",close," volume: ",volume
                ," adjClose: ",adjclose, " year: ",year," month: ",month," day: ",day)

                
                StockPrice.objects.create(
                    stock=stockInstance,
                    open=open,
                    high=high,
                    low=low,
                    close=close,
                    adjclose=adjclose,
                    day=day,
                    month=month,
                    year=year
                )
            stockInstance.mostRecentPrice = closingPrice
            stockInstance.save()
            
