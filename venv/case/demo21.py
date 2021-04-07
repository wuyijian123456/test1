class Person:
    # Define the class parameter "name"
    name = "Person"
    def __init__(self, name=None):
        # self.name is the instance parameter
        self.name = name
jeffrey = Person("Jeff")
print("%s name is %s" % (Person.name, jeffrey.name))

nico = Person()
nico.name = "Nico"
print("%s name is %s" % (Person.name, nico.name))