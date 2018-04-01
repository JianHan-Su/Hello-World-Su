class Employee():
    def __init__(self,first,last,year):
        self.first_name=first
        self.last_name=last
        self.year=year

    def give_raise(self,add=5000):
        self.year+=add
        print("The name is "+self.first_name+" "+
          self.last_name+".")
        print("The year is "+str(self.year))
