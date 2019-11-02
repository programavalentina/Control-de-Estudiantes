from rolepermissions.roles import AbstractUserRole

class Supervisor(AbstractUserRole):
    available_permissions = {

    }

class Teacher(AbstractUserRole):
    available_permissions = {
        
    }

class Student(AbstractUserRole):
    available_permissions = {
        
    }
