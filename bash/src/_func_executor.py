class _FuncExecuter:
    @staticmethod
    def run(func_store, args):
        functions = func_store.get_all_functions()

        for key, func in functions.items():
            if args.subparser_name == key:
                print(func(args), end="")
                break
