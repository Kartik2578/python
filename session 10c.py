"""both args amnd kwargs can be used together as an argument"""
def fun(*args, **kwargs):
    print(args)
    print(kwargs)


fun(10, 20, 30, name="John", email="john@example.com")