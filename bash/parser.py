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
        self._set_balance_parser(func_store)
        self._set_calendar_parser(func_store)
        self._set_cashflow_parser(func_store)
        self._set_dividends_parser(func_store)
        self._set_earnings_parser(func_store)
        self._set_financials_parser(func_store)
        self._set_history_parser(func_store)
        self._set_holders_parser(func_store)
        self._set_sustainability_parser(func_store)

    def get_args(self):
        return self.master_parser.parse_args()

    def _set_actions_parser(self, func_store):
        self._set_subparser("actions", "holders stuff")
        func_store.insert_function("actions", lambda args : yf.Ticker(args.ticker).actions)

    def _set_dividends_parser(self, func_store):
        self._set_subparser("dividends", "holders stuff")
        func_store.insert_function("dividends", lambda args : yf.Ticker(args.ticker).dividends)

    def _set_financials_parser(self, func_store):
        parser = self._set_subparser("financials", "financial stuff")
        parser.add_argument("--quarterly", "-q", default=False, action='store_true', help="Flag to do something")

        func_store.insert_function("financials", lambda args : yf.Ticker(args.ticker).quarterly_financials if args.quarterly else yf.Ticker(args.ticker).financials)

    def _set_holders_parser(self, func_store):
        parser = self._set_subparser("holders", "holders stuff")

        group = parser.add_mutually_exclusive_group()
        group.add_argument("--major", "-m", default=False, action="store_true" , help="Flag to do something")
        group.add_argument("--institutional", "-i", default=False, action="store_true" , help="Flag to do something")

        func_store.insert_function("holders", lambda args : yf.Ticker(args.ticker).major_holders if args.major else yf.Ticker(args.ticker).institutional_holders)

    def _set_balance_parser(self, func_store):
        parser = self._set_subparser("balance", "balance stuff")
        parser.add_argument("--quarterly", action="store_true", default=False, help="Flag to do something")

        func_store.insert_function("balance", lambda args : yf.Ticker(args.ticker).quarterly_balance_sheet if args.quarterly else yf.Ticker(args.ticker).balance_sheet)

    def _set_cashflow_parser(self, func_store):
        parser = self._set_subparser("cashflow", "calendar stuff")
        parser.add_argument("--quarterly", "-q", nargs='?')

        func_store.insert_function("cashflow", lambda args : yf.Ticker(args.ticker).quarterly_cashflow if args.quarterly else yf.Ticker(args.ticker).cashflow)

    def _set_earnings_parser(self, func_store):
        self._set_subparser("earnings", "earnings stuff")
        func_store.insert_function("earnings", lambda args : yf.Ticker(args.ticker).quarterly_earnings if args.quarterly else yf.Ticker(args.ticker).earnings)

    def _set_sustainability_parser(self, func_store):
        self._set_subparser("sustainability", "sustainability stuff")
        func_store.insert_function("sustainability", lambda args : yf.Ticker(args.ticker).sustainability)

    def _set_calendar_parser(self, func_store):
        self._set_subparser("calendar", "calendar stuff")
        func_store.insert_function("calendar", lambda args : yf.Ticker(args.ticker).calendar)

    def _set_history_parser(self, func_store):
        self._set_subparser("history", "history")
    
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