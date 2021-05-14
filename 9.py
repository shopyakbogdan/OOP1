class Cars:

    raise_amount = 1.04
    def __init__(self,name,model,value):
        self.name = name
        self.model = model
        self.value = value
        self.cod = name +" " '00132123' + 'cd'



    def fullinfo(self):
        return '{}  {}'.format(self.name,self.model)

    def apply_raise(self):
        self.value = int(self.value * self.raise_amount)

    def __str__(self):
        return '{} - {}'.format(self.fullinfo(),self.model)

    def __add__(self, other):
        return self.value + other.value

    def __len__(self):
        return len(self.fullinfo())


emp_1 = Cars('Bugati','Veyrone',50000)
emp_2 = Cars('Chevrolet','Camaro',20000)

print(len(emp_1))
