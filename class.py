class Dog:
    kind = "canine"#类变量
    tricks = []
    def __init__(self,name,age):
        self.name = name#实例变量  在类初始化时才有意义
        self.age = age

    @classmethod
    def add_trick(cls,trick):
        cls.tricks.append(trick)

d = Dog('FIDO',14)
E = Dog('BUDDY',13)
# print(d.name)
print(Dog.add_trick(1))
