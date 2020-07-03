class details:
    def set_name(self,name):
        self.name=name
    def __add__(self, other):
        fname=self.name+other.name
        return fname

first_name=details()
second_name=details()
third_name=details()
first_name.set_name("indu")
second_name.set_name(" v nair")
third_name.set_name(" madura")
full_name=first_name+second_name
print(full_name)