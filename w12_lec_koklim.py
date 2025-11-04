
#======================================================
# Non-OOP Vector
#======================================================

def vec_length(vec):
    return (vec[0]**2 + vec[1]**2) ** 0.5

def vec_normalize(vec):  # input vector will be mutated
    magnitude = vec_length(vec)
    if magnitude > 0:
        vec[0] /= magnitude
        vec[1] /= magnitude

def vec_add(vec1, vec2):  # returns a new vector
    return [ vec1[0] + vec2[0], vec1[1] + vec2[1] ]

def vec_print(vec):
    print(f"vector: ({vec[0]}, {vec[1]})")

# Example run
v1 = [1, 2]
v2 = [4, 7]
vec_print(v1)
vec_print(v2)

v3 = vec_add(v1, v2)
vec_print(v3)

print("vec_length(v2):", vec_length(v2))
vec_normalize(v2)
print("vec_length(v2):", vec_length(v2))



#======================================================
# MyVector Class
#======================================================

class MyVector:  # use UpperCamelCase for class name

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def length(self):
        return (self.x**2 + self.y**2) ** 0.5

    def normalize(self):  # self will be mutated
        magnitude = self.length()
        if magnitude > 0:
            self.x /= magnitude
            self.y /= magnitude

    def add(self, other):  # returns new MyVector instance
        if isinstance(other, MyVector):
            return MyVector(self.x + other.x, self.y + other.y)
        else:
            print("Error!")

    def print(self):
        print(f"MyVector: ({self.x}, {self.y})")

# Example run
v1 = MyVector(1, 2)
v2 = MyVector(4, 7)
v1.print()
v2.print()

v3 = v1.add(v2)
v3.print()

print("v2.length():", v2.length())
v2.normalize()
print("v2.length():", v2.length())



#======================================================
# MyVector2 Class
#======================================================

class MyVector2:  # use UpperCamelCase for class name

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def length(self):
        return (self.x**2 + self.y**2) ** 0.5

    def normalize(self):  # self is mutated
        magnitude = self.length()
        if magnitude > 0:
            self.x /= magnitude
            self.y /= magnitude

    def __add__(self, other):  # returns new MyVector instance
        if isinstance(other, MyVector2):
            return MyVector2(self.x + other.x, self.y + other.y)
        else:
            print("Error!")

    def __str__(self):
        return f"MyVector2: ({self.x}, {self.y})"

# Example run
v1 = MyVector2(1, 2)
v2 = MyVector2(4, 7)
print("v1:", v1)
print("v2:", v2)

v3 = v1 + v2
print("v3:", v3)

print("v2.length():", v2.length())
v2.normalize()
print("v2.length():", v2.length())




#======================================================
# Inheritance Example -- Before
#======================================================

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        self.running = False

    def speak(self):
        print(f'{self.name} says "Woof!"')

    def run(self):
        self.running = True
        print(f'{self.name} is running.')

    def stop_run(self):
        self.running = False
        print(f'{self.name} stops running.')

class Parrot:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        self.flying = False

    def speak(self):
        print(f'{self.name} says "Hello!"')

    def fly(self):
        self.flying = True
        print(f'{self.name} is flying.')

    def stop_fly(self):
        self.flying = False
        print(f'{self.name} stops flying.')


# Example run:

dog1 = Dog("Buddy", "Labrador")
dog2 = Dog("Luna", "Chihuahua")
parrot1 = Parrot("Rainbow", "Macaw")
parrot2 = Parrot("Cookie", "Parakeet")

dog1.run()
dog1.stop_run()
parrot1.fly()
parrot1.stop_fly()
dog2.speak()
parrot2.speak()


#======================================================
# Inheritance Example -- After
#======================================================

class Pet:
    # THE superclass - a generalisation which other classes can inherit from
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def speak(self):
        print(f'{self.name} says nothing...')


class Dog(Pet):
    # Pet is the superclass / parent class / base class of Dog
    # Dog is a subclass / child class / derived class of its parent class (Pet)
    # Dog (and Parrot below) are specialisations of the superclass (I think)
    def __init__(self, name, breed):
        super().__init__(name, breed)
        self.running = False

    def speak(self):
        print(f'{self.name} says "Woof!"')

    def run(self):
        self.running = True
        print(f'{self.name} is running.')

    def stop_run(self):
        self.running = False
        print(f'{self.name} stops running.')


class Parrot(Pet):
    def __init__(self, name, breed):
        super().__init__(name, breed)
        self.flying = False

    def speak(self):
        print(f'{self.name} says "Hello!"')

    def fly(self):
        self.flying = True
        print(f'{self.name} is flying.')

    def stop_fly(self):
        self.flying = False
        print(f'{self.name} stops flying.')


# Example run:

print("issubclass(Dog, Pet):", issubclass(Dog, Pet))
print("issubclass(Pet, Dog):", issubclass(Pet, Dog))
print("issubclass(Parrot, Pet):", issubclass(Parrot, Pet))
print("issubclass(Pet, Parrot):", issubclass(Pet, Parrot))

pet1 = Pet("Generic", "Pettable")
dog1 = Dog("Buddy", "Labrador")
parrot1 = Parrot("Rainbow", "Macaw")

print("isinstance(pet1, Pet):", isinstance(pet1, Pet))
print("isinstance(pet1, Dog):", isinstance(pet1, Dog))
print("isinstance(pet1, Parrot):", isinstance(pet1, Parrot))

print("isinstance(dog1, Pet):", isinstance(dog1, Pet))
print("isinstance(dog1, Dog):", isinstance(dog1, Dog))
print("isinstance(dog1, Parrot):", isinstance(dog1, Parrot))

print("isinstance(parrot1, Pet):", isinstance(parrot1, Pet))
print("isinstance(parrot1, Dog):", isinstance(parrot1, Dog))
print("isinstance(parrot1, Parrot):", isinstance(parrot1, Parrot))

pets = [pet1, dog1, parrot1]

for pet in pets:
    pet.speak()


#======================================================
