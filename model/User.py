

class User:
    def __init__(self):
        self.firstname = ''
        self.secondname = ''
        self.middlename = ''
        self.email = ''
        self.phone = ''
        self.roles = [] 

    def set_firstname(self, firstname: str = ''):
        self.firstname = firstname

    def set_secondname(self, secondname: str = ''):
        self.secondname = secondname

    def set_middlename(self, middlename: str = ''):
        self.middlename = middlename

    def set_email(self, email: str = ''):
        self.email = email

    def set_phone(self, phone: str = ''):
        self.phone = phone

    def add_role(self, rolename: str = ''):
        self.roles.append(rolename)

    def remove_role(self, rolename: str = ''):
        self.roles.remove(rolename)

    def get_firstname(self) -> str:
        return self.firstname

    def get_secondname(self) -> str:
        return self.secondname

    def get_middlename(self) -> str:
        return self.middlename

    def get_email(self) -> str:
        return self.email

    def get_phone(self) -> str:
        return self.phone

    def get_roles(self) -> list:
        return self.roles

    def user_has_role(self, value) -> bool:
        '''Check if user has role or list of roles

        Args:
            value -- name of role or list of those
        Returns:
            bool
        '''
        roles = self.get_roles()
        if value is list:
            return all([role in roles for role in value])
        elif value is str:
            return value in self.get_roles()
        else:
            raise TypeError('Value should be string or list')
