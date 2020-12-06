from _func_executor import _FuncExecuter
from _func_storage import _FuncStorage
from _parser import _Parser

func_store = _FuncStorage()
parser = _Parser(func_store)
args = parser.get_args()

_FuncExecuter.run(func_store, args)
