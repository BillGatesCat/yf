class _FuncStorage:
    def __init__(self):
        self._function_map = {}

    def insert_function(self, name, function):
        self._function_map[name] = function

    def get_all_functions(self):
        return self._function_map