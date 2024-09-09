def import_python_func():
    print("import python func")

    
def register(name, gender, *args):
    print(name)     # Dave
    print(gender)   # male
    print(args)     # (korea, seoul, 21)

def register_kwargs(name, gender, **kwargs):
    print(name)
    print(gender)
    print(kwargs.get("city"))
    print(kwargs.get("age"))
    
    
def register_args_kwargs(name, gender, *args, **kwargs):
    print(name)
    print(gender)
    print(args)
    print(kwargs.get("age"))
    print(kwargs.get("email"))
    
