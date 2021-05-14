class Cars:
    num_of_emps=0
    raise_amount = 1.04
    def __init__(self,name,model,value):
        self.name = name
        self.model = model
        self.value = value
        self.cod = name +" " '00132123' + 'cd'

        Cars.num_of_emps += 1

    def fullinfo(self):
        return '{}  {}'.format(self.name,self.model)

    def apply_raise(self):
        self.value = int(self.value * self.raise_amount)

class Designer(Cars):
    raise_amount = 1.10

    def __init__(self,name,model,value,brand):
       super(). __init__(name,model, value)
       self.brand = brand

class Manager(Cars):

    def __init__(self,name,model,value,carses= None):
       super().__init__(name,model, value)
       if carses is None:
           self.carses = []
       else:
           self.carses = carses

emp_1 = Cars('Bugati','Veyrone',50000)
emp_2 = Cars('Chevrolet','Camaro',20000)

emp_str_1 = "BMW-M3-80000"
emp_str_2 = "BMW-M5-40000"
des_1 = Designer('BMW','M5',460000,'bmv')
print(des_1.fullinfo())
print(des_1.brand)