# positional and keyword arguments: 
def add(*args):
    """
    Returns the sum for a arbitrary number of positional arguments
    """
    sum = 0
    for n in args:
        sum += n
    return sum


# https://www.youtube.com/watch?v=9Os0o3wzS_I&ab_channel=CoreySchafer

# def all_aboard(a, *args, **kw):
#     print(a, kw, args)
    
    
# all_aboard(4, 7, 3, 0, x = 10, y = 64)


# OOP 
# class Dog:
    
#     def __init__(self):
#         self.temperament = "loyal"
        
    
# class Labrador(Dog):
    
#     def __init__(self):
#         super().__init__()
#         print(f"{self} is {self.temperament}")
#         self.temperament = "gentle"
    

# # Class inheritance, writing subclass and superclass
# doggo = Dog()
# print(f"A dog is {doggo.temperament}")

# sparky = Labrador()
# print(f"Sparky is {sparky.temperament}")



