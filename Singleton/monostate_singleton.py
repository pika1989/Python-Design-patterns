class Borg(object):
    _shared_state = {}

    def __new__(cls, *args, **kwargs):
        obj = super(Borg, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls._shared_state
        return obj


b = Borg()
b1 = Borg()

print 'Borg object "b": ', b
print 'Borg object "b1": ', b1
print 'Object state "b": ', b.__dict__
print 'Object state "b1": ', b1.__dict__

b1.x = 3
print 'Object state "b": ', b.__dict__
print 'Object state "b1": ', b1.__dict__
print b is b1

class ChidlBorg(Borg):
    pass

child = ChidlBorg()
print child.__dict__

