

class User:
    def __init__(self):
        self._firstname = ''
        self._secondname = ''
        self._middlename = ''
        self._email = ''
        self._phone = ''
        self._roles = []

    @property
    def firstname(self) -> str:
        return self._firstname
    
    @property
    def secondname(self) -> str:
        return self._secondname

    @property
    def middlename(self) -> str:
        return self._middlename

    @property
    def email(self) -> str:
        return self._email

    @property
    def phone(self) -> str:
        return self._phone

    @property
    def roles(self) -> list:
        return self._roles

    @firstname.setter
    def firstname(self, firstname: str = ''):
        self._firstname = firstname

    @secondname.setter
    def secondname(self, secondname: str = ''):
        self._secondname = secondname

    @middlename.setter
    def middlename(self, middlename: str = ''):
        self._middlename = middlename

    @email.setter
    def email(self, email: str = ''):
        self._email = email

    @phone.setter
    def phone(self, phone: str = ''):
        self._phone = phone

    def add_role(self, rolename: str = ''):
        self._roles.append(rolename)

    def remove_role(self, rolename: str = ''):
        self._roles.remove(rolename)

    def has_roles(self, roles_for_check: list = []) -> bool:
        '''Check if user has roles from list

        Keyword arguments:
            roles_for_check -- list of role names (default [])
        Returns:
            bool
        '''
        return all([role in self.roles for role in roles_for_check])
