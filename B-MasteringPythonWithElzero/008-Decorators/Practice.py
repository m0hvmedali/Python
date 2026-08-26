# بما ان ال func حوا ال python تعتبر object ف نقدر نحط او نمرر داله جوا داله ك argument وهو ده الاساس اللي مبني عليه ال Decorator
# نفهم المشكله الاول عندنا :
# say_hello()
# احنا عايزين قبل ما ينفذ اللي جوا الداله يطبع staring...
# وبعد ما يخلص اللي جوة يطبع finished
 
def logger(func):

    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")

        result = func(*args, **kwargs)

        print("Done")

        return result

    return wrapper

@logger
def say_hello():
    print("Hello")

say_hello()

