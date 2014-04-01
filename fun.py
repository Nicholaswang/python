class fun(object):
    def bar(self):
        print 'bar'
    def sd(self):
        self.bar()

a = fun()
a.sd()

