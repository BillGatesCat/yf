import argparse
import yfinance as yf
import json   


master_parser = argparse.ArgumentParser()
subparsers = master_parser.add_subparsers(dest='command')

get_ticker_parser = subparsers.add_parser('get', help='Get data from yahoo finance')
get_ticker_parser.add_argument("-ticker", help="The ticker symbol")
get_ticker_parser.add_argument("-data", help="The data on the security associated with the ticker")

args = master_parser.parse_args()

stock = yf.Ticker(args.ticker)

if args.data == "info":
    print(json.dumps(getattr(stock, args.data), indent = 4))
elif args.data == "actions":
    print(stock.actions.to_csv())
elif args.data == "dividends":
    print(stock.dividends.to_csv())
elif args.data == "financials":
    print(stock.financials.to_csv())
elif args.data == "quarterly_financials":
    print(stock.quarterly_financials.to_csv())
elif args.data == "major_holders":
    print(stock.major_holders.to_csv())
elif args.data == "institutional_holders":
    print(stock.institutional_holders.to_csv())
elif args.data == "balance_sheet":
    print(stock.balance_sheet.to_csv())
elif args.data == "quarterly_balance_sheet":
    print(stock.quarterly_balance_sheet.to_csv())
elif args.data == "cashflow":
    print(stock.cashflow.to_csv())
elif args.data == "quarterly_cashflow":
    print(stock.quarterly_cashflow.to_csv())
elif args.data == "earnings":
    print(stock.earnings.to_csv())
elif args.data == "quarterly_earnings":
    print(stock.quarterly_earnings.to_csv())
elif args.data == "sustainability":
    print(stock.sustainability.to_csv())
elif args.data == "recommendations":
    print(stock.recommendations.to_csv())
elif args.data == "calendar":
    print(stock.calendar.to_csv())
elif args.data == "isin":
    print(stock.isin)