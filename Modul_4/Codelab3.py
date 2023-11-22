def title_decorator(function):
    def wrapper():
        func = function()
        make_title = func.title()
        print(make_title + " - Data is converted to title case")
        return make_title
    return wrapper

def split_string_decorator(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        print(str(splitted_string) + " - Then Data is splitted")
        return splitted_string
    return wrapper

@split_string_decorator
@title_decorator
def say_hi():
    return 'Hello There '

result = say_hi()
