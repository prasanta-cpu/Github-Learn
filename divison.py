class MyClass:
    def __init__(self, value):
        self.value = value
 
    def __truediv__(self, other):
        return MyClass(self.value and other.value)
 
a = MyClass(True)
b = MyClass(False)
c = a / b  # c.value is False
print(c.value)