import argparse
import yfinance as yf
import json   

class FuncExecuter:
    @staticmethod
    def run(func_store, args):
        functions = func_store.get_all_functions()

        for key, func in functions.items():
            if args.subparser_name == key:
                print(func(args))
                break

class FuncStore:
    def __init__(self):
        self._function_map = {}

    def insert_function(self, name, function):
        self._function_map[name] = function

    def get_all_functions(self):
        return self._function_map

class Parser:
    def __init__(self, func_store):
        self.master_parser = argparse.ArgumentParser()
        self.subparsers = self.master_parser.add_subparsers(dest='subparser_name', help='sub-command help')

        self._set_actions_parser(func_store)
        #self._set_balance_parser(func_store)
        self._set_calendar_parser(func_store)
        #self._set_cashflow_parser(func_store)
        self._set_dividends_parser(func_store)
        #self._set_earnings_parser(func_store)
        #self._set_financials_parser(func_store) new yfinance update being rolled out to fix issue https://github.com/ranaroussi/yfinance/pull/480
        self._set_history_parser(func_store)
        self._set_holders_parser(func_store)
        self._set_sustainability_parser(func_store)

    def get_args(self):
        return self.master_parser.parse_args()

    def _set_actions_parser(self, func_store):
        self._set_subparser("actions", "Prints a csv file with the schema (Date, Dividends, Stock Splits)")
        func_store.insert_function("actions", lambda args : yf.Ticker(args.ticker).actions.to_csv(header=True))

    def _set_dividends_parser(self, func_store):
        self._set_subparser("dividends", "Prints a csv file with the schema (Date, Dividends)")
        func_store.insert_function("dividends", lambda args : yf.Ticker(args.ticker).dividends.to_csv(header=True))

    def _set_financials_parser(self, func_store):
        parser = self._set_subparser("financials", "financial stuff")
        parser.add_argument("--quarterly", "-q", default=False, action='store_true', help="Flag to do something")

        func_store.insert_function("financials", lambda args : yf.Ticker(args.ticker).quarterly_financials if args.quarterly else yf.Ticker(args.ticker).financials)

    def _set_holders_parser(self, func_store):
        parser = self._set_subparser("holders", "Prints a csv file containing the major/institutional holders of this stock")

        group = parser.add_mutually_exclusive_group()
        group.add_argument("--major", "-m", default=False, action="store_true" , help="Flag to do something")
        group.add_argument("--institutional", "-i", default=False, action="store_true" , help="Flag to do something")

        func_store.insert_function("holders", lambda args : yf.Ticker(args.ticker).major_holders.to_csv(header=True) if args.major else yf.Ticker(args.ticker).institutional_holders.to_csv(header=True))

    def _set_balance_parser(self, func_store):
        parser = self._set_subparser("balance", "balance stuff")
        parser.add_argument("--quarterly", action="store_true", default=False, help="Flag to do something")

        func_store.insert_function("balance", lambda args : yf.Ticker(args.ticker).quarterly_balance_sheet if args.quarterly else yf.Ticker(args.ticker).balance_sheet)

    def _set_cashflow_parser(self, func_store):
        parser = self._set_subparser("cashflow", "calendaasdfr")
        parser.add_argument("--quarterly", "-q", nargs='?')

        func_store.insert_function("cashflow", lambda args : yf.Ticker(args.ticker).quarterly_cashflow if args.quarterly else yf.Ticker(args.ticker).cashflow)

    def _set_earnings_parser(self, func_store):
        parser = self._set_subparser("earnings", "earnings stuff")
        parser.add_argument("--quarterly", "-q", default=False, action='store_true', help="Flag to do something")

        func_store.insert_function("earnings", lambda args : yf.Ticker(args.ticker).quarterly_earnings if args.quarterly else yf.Ticker(args.ticker).earnings)

    def _set_sustainability_parser(self, func_store):
        self._set_subparser("sustainability", "Environmental, social, and governance issues which may be relevant to the specified company. Prints a csv file.")
        func_store.insert_function("sustainability", lambda args : yf.Ticker(args.ticker).sustainability.to_csv(header=True))

    def _set_calendar_parser(self, func_store):
        self._set_subparser("calendar", "Prints a csv file showing the next event on earnings calendar data")
        func_store.insert_function("calendar", lambda args : yf.Ticker(args.ticker).calendar.to_csv(header=False))

    def _set_history_parser(self, func_store):
        parser = self._set_subparser("history", "history")
        parser.add_argument("--period", "-p", default="1mo", help="The historical period. Is one month by default.")
        parser.add_argument("--interval", "-i", default="1d", help="The historical interval. Is one day by default.")
        parser.add_argument("--start", "-s", default=None, help="The start date of the output. Needs to be in format YYYY-MM-DD.")
        parser.add_argument("--end", "-e", default=None, help="The end date of the output. Needs to be in format YYYY-MM-DD.")
        parser.add_argument("--prepost", "-pr", default=False, action='store_true', help="Include Pre and Post market data in results? Is false by default.")
        parser.add_argument("--actions", "-a", default=True, action='store_true', help="Shows the historical dividends and splits. Is true by default.")
        parser.add_argument("--autoadjust", "-ad", default=True, action='store_true', help="Adjust all OHLC automatically? Is true by default.")
        parser.add_argument("--backadjust", "-bd", default=False, action='store_true', help="Back-adjusted data to mimic true historical prices. Is false by default.")
        parser.add_argument("--proxy", "-px", default=None, help="Optional. Proxy server URL scheme. Is not set by default.")
        parser.add_argument("--rounding", "-r", default=False, action='store_true', help="Optional. Round values to 2 decimal places? Is false by default.")
        #parser.add_argument("--timezone", "-tz", default=None, help="Flag to do something")
        
        func_store.insert_function("history", lambda args: yf.Ticker(args.ticker).history(period=args.period, interval=args.interval, 
            start=args.start, end=args.end, prepost=args.prepost, actions=args.actions, auto_adjust=args.autoadjust, 
            back_adjust=args.backadjust, proxy=args.proxy, rounding=args.rounding).to_csv())
  
    def _set_subparser(self, name, help_text):
        parser = self.subparsers.add_parser(name, help=help_text)
        parser.add_argument("-ticker", "-t", help="The ticker symbol")

        return parser

func_store = FuncStore()
parser = Parser(func_store)
args = parser.get_args()

FuncExecuter.run(func_store, args)
#for name in csv_data:
    #if getattr(args, name[0]):
    #    print(getattr(stock, name[0]).to_csv())
    #    exit

#if args.info:
#    print(json.dumps(stock.info, indent = 4))
#elif args.isin:
#    print(json.dumps({"isin": stock.isin}, indent = 4))
