def import_python_func():
    print("import python func")

    
def register(name, gender, *args):
    print(name)     # Dave
    print(gender)   # male
    print(args)     # (korea, seoul, 21)

def register_kwargs(name, gender, **kwargs):
    print(name)
    print(gender)
    for key, value in kwargs.items():
        print(key, value)
    
    
def register_args_kwargs(name, gender, *args, **kwargs):
    print(name)
    print(gender)
    print(args)
    for key, value in kwargs.items():
        print(key, value)
    
