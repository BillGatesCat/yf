# yf
## Yahoo! Finance market data downloader for Bash

**yf** is a bash tool that allows for quick and easy access to Yahoo! Finance market data through the terminal.

### Requirements for installation
- (Python)[https://www.python.org/] >= 3.4+
- (Pyinstaller)[https://pypi.org/project/pyinstaller/] >= 4.0+
- (Yfinance)[https://github.com/ranaroussi/yfinance/] == 0.1.55

### Installation
    sudo apt install pip
    pip install "pyinstaller>=4.0,<5.0"
    pip install yfinance==0.1.55

    sudo ./bash/install.sh

### Uninstall
    ./bash/uninstall.sh

### Requirements for testing
- (Bats)[https://github.com/sstephenson/bats/]

### Run tests
    ./bash/test/test.sh