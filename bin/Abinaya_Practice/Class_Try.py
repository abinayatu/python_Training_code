class Dog:

    def __init__(self, name):
        self.name = name



def breed(name):

    if name== 'Fido':
        print('pug')
        return name

    elif name=='Buddy':
        print('beagle')
        return name

d = Dog('Fido')
e = Dog('Buddy')

print(d.name)
print(e.name)



def buyDogFood(name):
    if breed(name)==('Fido'):
     print('it loves pedigree')
    elif():
        print('buy drools')


bn=breed('Fido')
fd=buyDogFood('Fido')
print("Breed name is",bn)