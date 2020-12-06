import yfinance as yf

class _YahooFunctions:
    @staticmethod
    def actions(args):
        return yf.Ticker(args.ticker).actions.to_csv(header=True)

    @staticmethod
    def dividends(args):
        return yf.Ticker(args.ticker).dividends.to_csv(header=True)

    @staticmethod
    def financials(args):
        if args.quarterly:
            return yf.Ticker(args.ticker).quarterly_financials

        return yf.Ticker(args.ticker).financials

    @staticmethod
    def holders(args):
        if args.major:
            return yf.Ticker(args.ticker).major_holders.to_csv(header=True)

        return yf.Ticker(args.ticker).institutional_holders.to_csv(header=True)

    @staticmethod
    def balance(args):
        if args.quarterly:
            return yf.Ticker(args.ticker).quarterly_balance_sheet

        return yf.Ticker(args.ticker).balance_sheet

    @staticmethod
    def cashflow(args):
        if args.quarterly:
            return yf.Ticker(args.ticker).quarterly_cashflow

        return yf.Ticker(args.ticker).cashflow

    @staticmethod
    def earnings(args):
        if args.quarterly:
            return yf.Ticker(args.ticker).quarterly_earnings

        return yf.Ticker(args.ticker).earnings

    @staticmethod
    def sustainability(args):
        return yf.Ticker(args.ticker).sustainability.to_csv(header=True)

    @staticmethod
    def calendar(args):
        return yf.Ticker(args.ticker).calendar.to_csv(header=False)

    @staticmethod
    def history(args):
        return yf.Ticker(args.ticker).history(period=args.period, interval=args.interval,
            start=args.start, end=args.end, prepost=args.prepost, actions=args.actions,
            auto_adjust=args.autoadjust, back_adjust=args.backadjust, proxy=args.proxy,
            rounding=args.rounding, tz=None).to_csv(header=True)
