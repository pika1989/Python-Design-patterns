class MyInt(type):
    def __call__(cls, *args, **kwargs):
        print "****** Here's My int ******", args
        print 'Now do whatever you want with these objects..'
        return type.__call__(cls, *args, **kwargs)


class int(object):
    __metaclass__ = MyInt
    def __init__(self, x, y):
        self.x = x
        self.y = y

i = int(4,5)


class MetaSingleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Logger(object):
    __metaclass__ = MetaSingleton


logger1 = Logger()
logger2 = Logger()

print logger1
print logger2
