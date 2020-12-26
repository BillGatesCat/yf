# yf
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
![Build](https://github.com/BillGatesCat/yf/workflows/Build/badge.svg)

### Yahoo! Finance market data downloader for Bash
**yf** is a bash tool that allows for quick and easy access to Yahoo! Finance market data.

## Quick Start
    yf history -t MSFT
The history subcommand outputs historical prices, volume, dividends, and stock splits.
The following command outputs the Microsoft stock data from the past month on a daily interval.
(Run `yf history --help` for an explanation on the subcommand.)

To run same command for the uncompiled Python source code, run `python bash/src/main.py history -t MSFT`

Other subcommands in yf include: `actions`, `calendar`, `dividends`, `holders`, `sustain`

### Requirements and tested platforms
***Ubuntu Linux And MacOS***
- [Python][1] >= 3.4+
- [Pyinstaller][2] >= 4.0+
- [Yfinance][3] == 0.1.55
- [Pip][4]

[1]: https://www.python.org/
[2]: https://pypi.org/project/pyinstaller/
[3]: https://github.com/ranaroussi/yfinance/
[4]: https://pip.pypa.io/en/stable/reference/pip_install/

### Installation
    pip install "pyinstaller>=4.0,<5.0"
    pip install yfinance==0.1.55

    sudo ./bash/install.sh

### Uninstall
    ./bash/uninstall.sh

### Run tests
    #Install bats dependency
    git clone https://github.com/sstephenson/bats.git
    sudo ./bats/install.sh /usr/local

    #Run tests
    ./bash/test/test.sh

## A note on pull requests
Please do not set your pull requests to merge with `main`, instead merge them to `develop`.

### P.S.
Drop me a note if you have any feedback!

![](https://i.kym-cdn.com/entries/icons/original/000/030/157/womanyellingcat.jpg)
