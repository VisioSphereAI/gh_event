print("Hi")
print("Hello")
print("Bye")
import numpy as np
print(np.random.rand(3,3))

print("Hi")

class A:
    def __init__(self):
        print("A")
    
    def __del__(self):
        print("Destructing A")
    
    def __str__(self):
        return "A"
    
    def __repr__(self):
        return "A"

if __name__ == "__main__":
    a = A()
    print(a)
    del a