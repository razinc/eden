# src: https://www.youtube.com/watch?v=FsAPt_9Bf3U

############
# function #
############

def decorator_func(original_func):

    # *args, **kwargs is used when variable is passed
    def wrapper_func(*args, **kwargs):
        print(f"wrapper executed this before {original_func.__name__}")
        return original_func(*args, **kwargs)
    return wrapper_func

def display():
    print("display func without decorator ran")

decorated_func = decorator_func(display)
decorated_func()

@decorator_func
def display_dec():
    print("display func with decorator ran")

display_dec()

@decorator_func
def display_info(name, age):
    print(f"Name: {name}, Age: {age}")

display_info("John", 21)

#########
# class #
#########

class decorator_class(object):

    def __init__(self, original_func):
        self.original_func = original_func

    def __call__(self, *args, **kwargs):
        print(f"__call__ executed this before {self.original_func.__name__}")
        return self.original_func(*args, **kwargs)
        
@decorator_class
def display_dec():
    print("display func with decorator ran")

display_dec()

@decorator_class
def display_info(name, age):
    print(f"Name: {name}, Age: {age}")

display_info("John", 21)

######################
# decorator as timer #
######################

def my_timer(ori_func):
    import time

    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = ori_func(*args, **kwargs)
        t2 = time.time() - t1
        print(f"{ori_func.__name__} run in {t2}s")
        return result

    return wrapper

@my_timer
def display_info(name, age):
    print(f"Name: {name}, Age: {age}")

display_info("John", 21)

