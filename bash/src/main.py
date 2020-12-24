import sys
from _func_executor import _FuncExecuter
from _func_storage import _FuncStorage
from _parser import _Parser
from _yf_help import print_yf_help

if len(sys.argv) == 1 or (len(sys.argv) == 2 and (sys.argv[1] == "-h" or sys.argv[1] == "--help")):
    print_yf_help()
    sys.exit()

func_store = _FuncStorage()
parser = _Parser(func_store)

if len(sys.argv) == 2 and sys.argv[1] in parser.subparsers.choices:
    parser.subparsers.choices[sys.argv[-1]].print_help()
    sys.exit()

args = parser.get_args()
_FuncExecuter.run(func_store, args)
