class Father:
    def fn(self):
        print('Tera Baap hu mei !')

class Mother(Father):
    pass

class Child(Mother):
    pass

Baccha = Child()
Baccha.fn()
