'''
Created on 2014-12-17

Copyright info: The code here comes, directly or indirectly, from Mari Wahl and her great Python book.
                I'm not the original owner of the code.
                Thanks Mari for her great work!
'''

# simulation
class Animal_Node(object):
    def __init__(self, animalName = None, animalKind = None, pointer = None):
        self.animalName = animalName
        self.animalKind = animalKind
        self.pointer = pointer
        self.timestamp = 0

class AnimalShelter(object):
    def __init__(self):
        self.headCat = None
        self.headDog = None
        self.tailCat = None
        self.tailDog = None
        # time stamp
        self.animalNumber = 0
    
    def enqueue(self, animalName, animalKind):
        self.animalNumber += 1
        new_animal = Animal_Node(animalName, animalKind)
        new_animal.timestamp = self.animalNumber
        
        if animalKind == 'cat':
            if not self.headCat:
                self.headCat = new_animal
            if self.tailCat:
                self.tailCat.pointer = new_animal
            self.tailCat = new_animal                
        elif animalKind == 'dog':
            if not self.headDog:
                self.headDog = new_animal
            if self.tailDog:
                self.tailDog.pointer = new_animal
            self.tailDog = new_animal
            
    def dequeueDog(self):
        if self.headDog:
            new_animal = self.headDog
            self.headDog = new_animal.pointer
            return str(new_animal.animalName)
        else:
            return 'No Dogs!'
    
    def dequeueCat(self):
        if self.headCat:
            new_animal = self.headCat
            self.headCat = new_animal.pointer
            return str(new_animal.animalName)
        else:
            return 'No Cats!'
    
    def dequeueAny(self):
        if self.headCat and not self.headDog:
            return self.dequeueCat()
        elif self.headDog and not self.headCat:
            return self.dequeueDog()
        elif self.headDog and self.headCat:
            if self.headDog.timestamp < self.headCat.timestamp:
                return self.dequeueDog()
            else:
                return self.dequeueCat()
        else:
            return ('No Animals!')

    def _print(self):
        print("Cats:")
        cats = self.headCat
        while cats:
            print(cats.animalName, cats.animalKind)
            cats = cats.pointer
        print("Dogs:")
        dogs = self.headDog
        while dogs:
            print(dogs.animalName, dogs.animalKind)
            dogs = dogs.pointer

if __name__ == '__main__':
    qs = AnimalShelter()
    qs.enqueue('bob', 'cat')
    qs.enqueue('mia', 'cat')
    qs.enqueue('yoda', 'dog')
    qs.enqueue('wolf', 'dog')
    qs._print()
    print("Deque one dog and one cat...")
    qs.dequeueDog()
    qs.dequeueCat()
    qs._print()