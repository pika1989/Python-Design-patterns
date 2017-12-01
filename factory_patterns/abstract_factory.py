from abc import ABCMeta, abstractmethod


class PizzaFactory(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def createVegPizza(self):
        pass

    @abstractmethod
    def createNonVegPizza(self):
        pass


class IndianPizzaFactory(PizzaFactory):
    def createVegPizza(self):
        return DeluxVeggiePizza()

    def createNonVegPizza(self):
        return ChickenPizza()


class USPizzaFactory(PizzaFactory):
    def createVegPizza(self):
        return MexicanVegPizza()

    def createNonVegPizza(self):
        return HamPizza()


class VegPizza(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def prepare(self, VegPizza):
        pass


class NonVegPizza(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def serve(self, VegPizza):
        pass


class DeluxVeggiePizza(VegPizza):
    def prepare(self):
        print 'Prepare %s' % (type(self).__name__)


class ChickenPizza(NonVegPizza):
    def serve(self, VegPizza):
        print '%s is served with Chicken on %s' % (type(self).__name__,
                                                   type(VegPizza).__name__)


class MexicanVegPizza(VegPizza):
    def prepare(self):
        print 'Prepare %s' % (type(self).__name__)


class HamPizza(NonVegPizza):
    def serve(self, VegPizza):
        print '%s is served with Ham on %s' % (type(self).__name__,
                                               type(VegPizza).__name__)


class PizzaStore(object):
    def makePizzas(self):
        for factory in [IndianPizzaFactory(), USPizzaFactory()]:
            self.factory = factory
            self.NonVegPizza = self.factory.createNonVegPizza()
            self.VegPizza = self.factory.createVegPizza()
            self.VegPizza.prepare()
            self.NonVegPizza.serve(self.VegPizza)


pizza = PizzaStore()
pizza.makePizzas()
