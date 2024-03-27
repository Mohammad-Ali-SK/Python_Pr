# Ther are 3 type of programing -----
# 1. Imperative
# 2. Functional 
# 3. Object Oriented


# Oops in python _____________________________1.0)


# class Factory:
#     def __init__(self,name,brand):
#         self.name = name
#         self.brand = brand
#     def full_details(self):
#         print(f'The car naem is {self.name} and brand name is {self.brand} ')

# class Honda:
#     pass

# # Multiple Inheritence------------------
# class Ferari_2(Factory,Honda):
#     def __init__(self, name, brand,ty):
#         super().__init__(name, brand)
#         self.ty = ty

# # Multilable inheritence________
# class Bike(Ferari_2):
#     def __init__(self, name, brand, ty):
#         super().__init__(name, brand, ty)
        
# ferari = Factory('Ferari','UK')
# lam = Ferari_2('Lamborgani','UK',4)
# splende = Bike('Hero','Hero',8)
# splende.full_details()
# ferari.full_details()
# lam.full_details()


# student1.student_info()
# def d(x):
#     return x*2


# d = lambda x : x * 2

d = lambda x,y :(x+y) / 2
print(int(d(7,9)))