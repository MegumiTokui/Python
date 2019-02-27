#要復習

class employee:

    add_emp=0
    increase=2
    def __init__(self, pay,name,age):
        self.pay=pay
        self.name=name
        self.age=age

        employee.add_emp +=1
    def fullname(self):
        return '{} {}'.format(self.name, self.age)

    def salery_hike(self):
        self.pay = int(self.pay * self.increase)

print(employee.add_emp)

lohit =employee(2,'lohit',21)
print(employee.add_emp)

rekha= employee(3,'rekha',23)
print(employee.add_emp)

lohi= employee(3,2,43)

#countes the number of employess

print(employee.add_emp)