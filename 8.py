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

    def add_car(self, car):
        if car not in self.carses:
            self.carses.append(car)

    def remove_car(self, car):
        if car in self.carses:
            self.carses.remove(car)

emp_1 = Designer('Bugati','Veyrone',50000,'bgt')
emp_2 = Designer('Chevrolet','Camaro',20000, 'cvrl')

mgr_1 = Manager('FGFR','QQQ',1515151,[emp_1])

print('DODATU AUTO')




#print(mgr_1.cod)
mgr_1.add_car(emp_2)
print(mgr_1.fullinfo())
#mgr_1.remove_car(emp_1)
#mgr_1.print_cars()
#emp_str_1 = "BMW-M3-80000"
#emp_str_2 = "BMW-M5-40000"
#des_1 = Designer('BMW','M5',460000,'bmv')
#print(des_1.fullinfo())
#print(des_1.brand)