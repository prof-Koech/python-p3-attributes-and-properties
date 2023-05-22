#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
       def __init__(self, name ="Bosco",breed="Corgi"):
        self.name = name
        self._breed = breed

def get_name(self):
        return self._name

def set_name(self, name):
        if not isinstance(name, str):
            print("Name must be string between 1 and 25 characters.")
        elif len(name) < 1 or len(name) > 25:
            print("Name must be string between 1 and 25 characters.")
        else:
            self._name = name.title()

        name = property(get_name, set_name)



def get_breed(self):
        return self._breed

    
def set_breed(self, dog_breed):
        if dog_breed in APPROVED_BREEDS:
            self._breed = dog_breed
        else:
            print("Breed must be in the list of approved breeds.")

        breed = property(get_breed, set_breed)
