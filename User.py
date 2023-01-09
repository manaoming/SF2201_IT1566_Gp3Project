import shelve


class User:
    with shelve.open("Users") as users:
        count = len(users)

    def __init__(self, firstname, lastname, gender, membership, remarks):
        self.__userid = str(User.count)
        User.count += 1
        self.__firstname = firstname
        self.__lastname = lastname
        self.__gender = gender
        self.__membership = membership
        self.__remarks = remarks

    def get_userid(self):
        return self.__userid

    def get_firstname(self):
        return self.__firstname
    
    def get_lastname(self):
        return self.__lastname
    
    def get_gender(self):
        return self.__gender
    
    def get_membership(self):
        return self.__membership
    
    def get_remarks(self):
        return self.__remarks

    def set_userid(self, userid):
        self.__userid = userid
    
    def set_firstname(self, firstname):
        self.__firstname = firstname
    
    def set_lastname(self, lastname):
        self.__lastname = lastname
    
    def set_gender(self, gender):
        self.__gender = gender
    
    def set_membership(self, membership):
        self.__membership = membership

    def set_remarks(self, remarks):
        self.__remarks = remarks
    
