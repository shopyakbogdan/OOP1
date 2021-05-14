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


    @classmethod
    def set_raise_amt(cls,amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls,emp_str):
        name, model, value = emp_str.split('-')
        return cls(name,model,value)


emp_1 = Cars('Bugati','Veyrone',50000)
emp_2 = Cars('Chevrolet','Camaro',20000)

emp_str_1 = "BMW-M3-80000"
emp_str_2 = "BMW-M5-40000"

new_emp_1 = Cars.from_string(emp_str_1)
print(new_emp_1.cod)
print(new_emp_1.value)