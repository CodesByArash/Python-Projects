def decoratorfunction(input_str):
    def decorator(func):
        
        str = input_str + "arash"

        def wrapper_func(string):
            return func(string) + str
        
        return wrapper_func
    return decorator


@decoratorfunction("str")
def arash(string):
    return string

