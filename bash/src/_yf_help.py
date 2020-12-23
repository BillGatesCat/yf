yf_usage_message = "usage: yf [SUBCOMMAND] ..."

yf_subcommand_message = """program:
  SUBCOMMAND needs to be specified as one of the following: actions, calendar, dividends, history, holders, sustain
  Add -h after [SUBCOMMAND] for more details on usage. Ex. yf [SUBCOMMAND] -h"""

yf_options_message = """optional arguments:
  -h, --help            show this help message and exit"""

def print_yf_help():
    print(yf_usage_message)
    print()
    print(yf_subcommand_message)
    print()
    print(yf_options_message)
