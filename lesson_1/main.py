# class A:
#     def __init__(self, name):
#         self.name = name

# class B(A):
#     def __init__(self, age):
#         self.age = age
#         super().__init__(name="bardiya")

#     def call(self):
#         return f"my name is: {self.name} and my age is : {self.age}"
# b = B(22)
# print(b.name)
# print(b.age)
# print(b.call())
# ====================================
# class Profile:
#     def __init__(self, name, familly):
#         self.name = name
#         self.familly = familly
#         # self.email = f"{self.name}_{self.familly}@gmail.com"
#     @property
#     def email(self):
#         return(f"{self.name}_{self.familly}@gmail.com")


# p = Profile("bardiya", "davodi")
# p.name = "korush"
# print(p.email)
# ====================================
class Profile:
    def __init__(self, name):
        self.name = name
    
    def show(self):
        return f"my name is : {self.name}"

    @staticmethod
    def is_age(age):
        if age > 18:
            print(f"I am young pepole")
        elif age < 18 and age > 10:
            print(f"I am teenager ")
        else:
            print(f"I am seniur")

profile = Profile("bardiya")
print(profile.show())
profile.is_age(20)