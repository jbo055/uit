class Customer:
    def __init__(self, name, password, cid):
        self.name = name
        self.__password = password # the attribute password is public and can be reached from everywhere.
        self.__cid = cid
        # two _ means private. 

    @property 
    def password(self):
        return self.__password
    
    @password.setter
    def password(self, new_password): # the structure of a setter: a setter always has a parameter which is the value we want to set, and the setter never has a return value.
        self.__password = new_password

    @property
    def cid(self):
        return self.__cid
    
    @cid.setter
    def cid(self, new_cid):
        self.__cid = new_cid



    # def get_password(self): # the basic structure of a getter: a getter has no parameters and a getter has a return value
    #      return self.__password

    # def set_password(self, new_password): # the structure of a setter: a setter always has a parameter which is the value we want to set, and the setter never has a return value.
    #     self.__password = new_password
    

c1 = Customer("Ola Nordmann", "123", "1978")
c2 = Customer("John Doe", "abc", "1756")

c1.password = "1111"
c1.cid = "1265"
print(c1.password, c1.cid)

# newpass = "abcde"
# c1.set_password(newpass) # i do not want to call any functions. i want to change my private members/attributes without calling a function

# c1.__password = "blablabla" # here i change the password
# print(c1.get_password()) # here i get the password using the getter