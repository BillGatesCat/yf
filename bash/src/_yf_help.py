YF_USAGE_MESSAGE = "usage: yf [SUBCOMMAND] ..."

YF_SUBCOMMAND_MESSAGE = """program:
  SUBCOMMAND needs to be specified as one of the following: actions, calendar, dividends, history, holders, sustain
  Add -h after [SUBCOMMAND] for more details on usage. Ex. yf [SUBCOMMAND] -h"""

YF_OPTIONS_MESSAGE = """optional arguments:
  -h, --help            show this help message and exit"""

def print_yf_help():
    print(YF_USAGE_MESSAGE)
    print()
    print(YF_SUBCOMMAND_MESSAGE)
    print()
    print(YF_OPTIONS_MESSAGE)
