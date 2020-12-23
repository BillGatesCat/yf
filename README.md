# yf
## Yahoo! Finance market data downloader for Bash

## Why? [![start with why](https://img.shields.io/badge/start%20with-why%3F-brightgreen.svg?style=flat)](http://www.ted.com/talks/simon_sinek_how_great_leaders_inspire_action)

**yf** is a bash tool that allows for quick and easy access to Yahoo! Finance market data through the terminal.

### Requirements for installation
- [Python][1] >= 3.4+
- [Pyinstaller][2] >= 4.0+
- [Yfinance][3] == 0.1.55

[1]: https://www.python.org/
[2]: https://pypi.org/project/pyinstaller/
[3]: https://github.com/ranaroussi/yfinance/

### Installation
    sudo apt install pip
    pip install "pyinstaller>=4.0,<5.0"
    pip install yfinance==0.1.55

    sudo ./bash/install.sh

### Uninstall
    ./bash/uninstall.sh

### Run tests
    ./bash/test/test.sh