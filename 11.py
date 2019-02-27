class Person:
    def __init__(self, first,last):
        self.first =first
        self.last =last

    def self_intro(self):
        #return '{} {}'.format(self.first, self.last)
        return f'I am {self.last} {self.first}.'
        #print("I am" + self.last + self.first )

    @staticmethod
    def hello():
        print("Hello")

person1 =Person("Megu", "Tokui")
person2= Person("Lohit", "Tanaka")


print(person1.self_intro())
print(person2.self_intro())
