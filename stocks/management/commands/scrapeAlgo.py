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
    "ticker": "HOOD",
    "logo": "robinhood.png"
    },
{
    "companyName": "Johnson & Johnson",
    "ticker": "JNJ",
    "logo": "JNJ.png"
},    {
    "companyName": "Walmart",
    "ticker": "WMT",
    "logo": "WMT.png"
},    {
    "companyName": "Visa",
    "ticker": "V",
    "logo": "V.png"
},    {
    "companyName": "Exxon Mobil",
    "ticker": "XOM",
    "logo": "XOM.png"
},    {
    "companyName": "Procter & Gamble",
    "ticker": "PG",
    "logo": "PG.png"
},    {
    "companyName": "Mastercard",
    "ticker": "MA",
    "logo": "MA.png"
},    {
    "companyName": "Bank of America",
    "ticker": "BAC",
    "logo": "BAC.png"
},    {
    "companyName": "Home Depot",
    "ticker": "HD",
    "logo": "HD.png"
},    {
    "companyName": "Pfizer",
    "ticker": "PFE",
    "logo": "PFE.png"
},    {
    "companyName": "AbbVie",
    "ticker": "ABBV",
    "logo": "ABBV.png"
},    {
    "companyName": "Toyota Motor",
    "ticker": "TM",
    "logo": "TM.png"
},    {
    "companyName": "Alibaba Group",
    "ticker": "BABA",
    "logo": "BABA.png"
},    {
    "companyName": "McDonald's",
    "ticker": "MCD",
    "logo": "MCD.png"
},    {
    "companyName": "Nike",
    "ticker": "NKE",
    "logo": "NKE.png"
},    {
    "companyName": "Philip Morris",
    "ticker": "PM",
    "logo": "PM.png"
},    {
    "companyName": "Wells Fargo",
    "ticker": "WFC",
    "logo": "WFC.png"
},    {
    "companyName": "United Parcel Service",
    "ticker": "UPS",
    "logo": "UPS.png"
},    {
    "companyName": "T-Mobile",
    "ticker": "TMUS",
    "logo": "TMUS.png"
},    {
    "companyName": "Texas Instruments",
    "ticker": "TXN",
    "logo": "TXN.png"
},    {
    "companyName": "Morgan Stanley",
    "ticker": "MS",
    "logo": "MS.png"
},    {
    "companyName": "CVS Health",
    "ticker": "CVS",
    "logo": "CVS.png"
},    {
    "companyName": "Lowe's Companies",
    "ticker": "LOW",
    "logo": "LOW.png"
},    {
    "companyName": "Charles Schwab Corporation",
    "ticker": "SCHW",
    "logo": "SCHW.png"
},    {
    "companyName": "International Business Machines",
    "ticker": "IBM",
    "logo": "IBM.png"
},    {
    "companyName": "Lockheed Martin",
    "ticker": "LMT",
    "logo": "LMT.png"
},    {
    "companyName": "American Express Company",
    "ticker": "AXP",
    "logo": "AXP.png"
},
    {
    "companyName": "Deere & Company",
    "ticker": "DE",
    "logo": "DE.png"
},    {
    "companyName": "Catepillar",
    "ticker": "CAT",
    "logo": "CAT.png"
},    {
    "companyName": "Sony Group Corporation",
    "ticker": "SONY",
    "logo": "SONY.png"
},    {
    "companyName": "Goldman Sachs Group",
    "ticker": "GS",
    "logo": "GS.png"
},    {
    "companyName": "Target",
    "ticker": "TGT",
    "logo": "TGT.png"
},    {
    "companyName": "CitiGroup",
    "ticker": "C",
    "logo": "C.png"
},    {
    "companyName": "3M company",
    "ticker": "MMM",
    "logo": "MMM.png"
},    {
    "companyName": "Estee Lauder Companies",
    "ticker": "EL",
    "logo": "EL.png"
},    {
    "companyName": "General Electric Company",
    "ticker": "GE",
    "logo": "GE.png"
},    {
    "companyName": "Starbucks Corporation",
    "ticker": "SBUX",
    "logo": "SBUX.png"
},    {
    "companyName": "Sherwin-Williams",
    "ticker": "SHW",
    "logo": "SHW.png"
},    {
    "companyName": "Airbnb",
    "ticker": "ABNB",
    "logo": "ABNB.png"
},    {
    "companyName": "Waste Management",
    "ticker": "WM",
    "logo": "WM.png"
},
{
    "companyName": "Fidelity National Information Services",
    "ticker": "FIS",
    "logo": "FIS.png"
},
{
    "companyName": "MetLife",
    "ticker": "MET",
    "logo": "MET.png"
},
{
    "companyName": "The Hershey Company",
    "ticker": "HSY",
    "logo": "HSY.png"
},
{
    "companyName": "Uber",
    "ticker": "UBER",
    "logo": "UBER.png"
},
{
    "companyName": "Twitter",
    "ticker": "TWTR",
    "logo": "TWTR.png"
},
{
    "companyName": "Honda Motor",
    "ticker": "HMC",
    "logo": "HMC.png"
},
{
    "companyName": "Sysco Corporation",
    "ticker": "SYY",
    "logo": "SYY.png"
},
{
    "companyName": "Warner Bros. Discovery",
    "ticker": "WBD",
    "logo": "WBD.png"
},
{
    "companyName": "Kroger Company",
    "ticker": "KR",
    "logo": "KR.png"
},
{
    "companyName": "HP Inc",
    "ticker": "HP",
    "logo": "HP.png"
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
            
