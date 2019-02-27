class employee:

    
    increase=2

    def __init__(self, pay, name, age):
        self.pay= pay
        self.name = name
        self.age =age

    def fullname(self):
        return '{} {}'.format(self.name, self.age)

    def salery_hike(self):
        self.pay = int(self.pay * employee.increase)


lohit = employee(2, 'lohit', 21)
me  = employee(3,'me',23)


print(lohit.pay) 
lohit.increase = 10

lohit.salery_hike() #計算された
print(lohit.pay)
print(lohit.__dict__)


print(lohit.__dict__)
print(lohit.increase)
print(lohit.name)

print(me.pay)
print(me.__dict__)
me.wihi =100
print(me.__dict__)
