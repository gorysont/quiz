

class User:
    def __init__(self):
        self.firstname = ''
        self.secondname = ''
        self.middlename = ''
        self.email = ''
        self.phone = ''
        self.roles = []

    @property
    def firstname(self) -> str:
        return self.firstname
    
    @property
    def secondname(self) -> str:
        return self.secondname

    @property
    def middlename(self) -> str:
        return self.middlename

    @property
    def email(self) -> str:
        return self.email

    @property
    def phone(self) -> str:
        return self.phone

    @property
    def roles(self) -> list:
        return self.roles

    @firstname.setter
    def firstname(self, firstname: str = ''):
        self.firstname = firstname

    @secondname.setter
    def secondname(self, secondname: str = ''):
        self.secondname = secondname

    @middlename.setter
    def middlename(self, middlename: str = ''):
        self.middlename = middlename

    @email.setter
    def email(self, email: str = ''):
        self.email = email

    @phone.setter
    def phone(self, phone: str = ''):
        self.phone = phone

    def add_role(self, rolename: str = ''):
        self.roles.append(rolename)

    def remove_role(self, rolename: str = ''):
        self.roles.remove(rolename)

    def has_roles(self, roles_for_check: list = []) -> bool:
        '''Check if user has roles from list

        Keyword arguments:
            roles_for_check -- list of role names (default [])
        Returns:
            bool
        '''
        return all([role in self.roles for role in roles_for_check])
