"""
What are classes and objects in Python?
    - Classes are a blueprint. Objects are real world concepts that are realized by classes
    a House class can have objects that are different houses (house1, house2, house3)


Create a simple class with the name "human" which would give out the name and age of the person
"""

class Human():
    name = None
    age = None

    #provide an init method if we want to initialize human programmatically
    # def __init__(self, name, age):
    #     self.name = name
    #     self.age = age
    
    ### These functions are for getting user input from the console to give the human a name and age
    def get_name(self):
        self.name = input("Enter a name for the human: ")
    
    def get_age(self):
        self.age = int(input("Enter an age for the human: "))

