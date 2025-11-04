### Prompt: why did my lecturer define the speak method in Pet since he overrode it in all the child classes?

Defining the `speak` method in the base class **`Pet`** is a common practice in **Object-Oriented Programming (OOP)**, specifically to enable **polymorphism** and provide a **default behavior** or a **method signature**.

-----

### 💡 The Role of the Base Method

The primary reasons your lecturer included `speak` in `Pet` are:

  * **1. Enabling Polymorphism:** This is the most important reason. **Polymorphism** (meaning "many forms") allows you to treat objects of different classes (like `Dog` and `Parrot`) **uniformly** if they share a common ancestor and a common method signature.

      * Since all child classes inherit from `Pet` and implement their own version of `speak`, you can create a list of different pets and call `speak()` on *each one* without needing to know its exact type.

    > For example:

    > ```python
    > pets = [Dog("Buddy", "Labrador"), Parrot("Polly", "African Grey")]
    > for pet in pets:
    >     pet.speak() # Calls Dog.speak() or Parrot.speak() automatically
    > ```

      * If `speak` wasn't defined in `Pet`, the Python interpreter wouldn't know that all `Pet` objects (and its subclasses) are guaranteed to have a `speak` method, which could lead to an **`AttributeError`** if you tried to call it on a generic `Pet` or a list of `Pet` subclasses.

  * **2. Providing a Default/Fallback Behavior:** The implementation in `Pet` (`print(f'{self.name} says nothing...')`) serves as a **default** behavior for any subclass that **doesn't** explicitly override the `speak` method. While you've shown that `Dog` and `Parrot` *do* override it, if you later created a `Snake` class that didn't override `speak`, it would safely inherit and use the `Pet` version.

  * **3. Defining the Contract (Interface):** By including `speak` in `Pet`, it establishes an **interface** or **contract** that all subclasses are *expected* to fulfill (to "speak"). Even if the base method just had a `pass` statement, its presence indicates that "all objects descended from `Pet` *can* be spoken to."

### 📝 Abstract Base Classes (Alternative)

In more complex scenarios, if the `Pet.speak` method was *only* meant to be a contract and *never* meant to be called (i.e., every pet *must* have a unique speak sound), your lecturer might have used an **Abstract Base Class (ABC)**.

In Python, you can use the `abc` module and the `@abstractmethod` decorator to define a method that **must** be overridden by concrete subclasses.

> ```python
> from abc import ABC, abstractmethod
> ```

> class Pet(ABC):
> \# ... other methods ...

> ```
> @abstractmethod
> def speak(self):
>     pass # Must be overridden
> ```

> # If a subclass like Dog didn't define speak, it would raise a TypeError.
>
> ```
> ```

However, the approach your lecturer used (defining a simple concrete method) is a common and practical way to demonstrate polymorphism and provide a safe default in standard inheritance.