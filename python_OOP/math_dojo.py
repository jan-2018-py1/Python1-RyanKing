class MathDojo(object):
    def __init__(self):
        self.total = 0

    def add(self, *args):
        for arg in args:
            if isinstance(arg, list) or isinstance(arg, tuple):
                for i in arg:
                    self.total += i
            else:
                self.total += arg
        return self

    def subtract(self, *args):
        for arg in args:
            if isinstance(arg, list) or isinstance(arg, tuple):
                for i in arg:
                    self.total -= i
            else:
                self.total -= arg
        return self

    def result(self):
        print "Total:", self.total

md = MathDojo()
md.add(2).add(2,5).subtract(3,2).result()

md2 = MathDojo()
md2.add([1], 3,4).add([3,5,7,8], (2,4.3,1.25)).subtract(2, (2,3), [1.1,2.3]).result()
