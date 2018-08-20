class linear_regression:
    def __init__(self,o0,o1):
        self.f = {'o0': o0, 'o1': o1}

    def training(self,trainig_set,n_test):
        a=0.001
        f=self.f
        o0=f['o0']
        o1=f['o1']
        m=int(len(trainig_set['x']))
        for i in range(n_test):
            o0 = o0 - a* (self.som(m, trainig_set,'o0')/m)
            o1 = o1 - a* (self.som(m, trainig_set,'o1')/m)
            self.f['o0'] = o0
            self.f['o1'] = o1

    def som(self,m,training_set,theta):
        som=0
        for i in range(m):
            if theta == 'o0':
                x = 1
            else:
                x =training_set['x'][i]
            som+=(self.error(training_set,i)*x)
        return som

    def out(self,x):
        y=x*self.f['o1']+self.f['o0']
        return y

    def error(self,trainig_set,i):
        return self.out(trainig_set['x'][i])-trainig_set['y'][i]


trainig_set = {'x':[1,2,3,4,5],'y':[6,7,8,9,10]}

h=linear_regression(0,0)
h.training(trainig_set,10000)
print(h.f)
print(h.out(float(input('x'))))
