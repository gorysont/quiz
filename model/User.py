

class User:
    def __init__():
        self.firstname = ''
        self.secondname = ''
        self.middlename = ''
        self.email = ''
        self.roles = [] 

    def set_firstname(self, value):
        self.firstname = value

    def set_secondname(self, value):
        self.secondname = value

    def set_middlename(self, value):
        self.middlename = value

    def set_email(self, email):
        self.email = email

    def add_role(self, value):
        self.roles.append(value)

    def get_firstname(self) -> str:
        return self.firstname

    def get_secondname(self) -> str:
        return self.secondname

    def get_middlename(self) -> str:
        return self.middlename

    def get_roles(self) -> list:
        return self.roles



