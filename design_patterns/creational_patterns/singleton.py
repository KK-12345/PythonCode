
# python 3
# class Singleton(type):
#     instance = None
#     def __init__(cls, name, bases, attrs, **kwargs):
#         super(Singleton, cls).__init__(name, bases, attrs)
#         cls._instance = None
#
#     def __call__(cls, *args, **kwargs):
#         if cls._instance is None:
#             cls._instance = super(Singleton, cls).__call__(*args, **kwargs)
#         return cls._instance

# python 2
class Singleton(object):
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not isinstance(cls._instance, cls):
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance


class MyClass(Singleton):
    pass


# class MyClass(metaclass=Singleton):
#     pass


if __name__ == '__main__':
    m1 = MyClass()
    m2 = MyClass()
    assert m1 is not m2
