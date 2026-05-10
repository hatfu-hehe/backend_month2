#OOP - Static methods. Git - sliyanie? of branches. CLass attributes and methods.
# Class variables or attributes

# rewatch the lesson on platform
# __init__ read some info
# git init - creating repository
# git log, git switch -c, git branch, git push origin ___ (branch name)

"""CLass variables (attributes)"""
class User:
    # class's attributes
    user_count = 0
    default_password = '12345678'

    def __init__(self, name, phone):
        # object's attributes
        self.name = name
        self.phone = phone
        self.role = 'user'
        self.password = User.default_password
        User.user_count += 1

    """Class methods"""
    @classmethod
    def create_admin(cls, name, phone):
        # for special creating objects
        admin = cls(name, phone)
        admin.role = 'admin'
        admin.password = 'qwerty'
        print(User.user_count)
        return admin

    @classmethod
    def get_user_count(cls):
        return User.user_count
        # return cls.user_count

    @staticmethod
    def validate_password(password):
        # for monitoring password's length
        if len(password) < 8:
            return False
        else:
            return True
        # shorter way
        # return len(password) >= 8

    # @staticmethod
    def test(self):        # may be static
        print(User.user_count, User.default_password)

    def change_password(self, new_password):         # also may be staticmethod if there wasn't used 'self'
        if not User.validate_password((new_password)):
            raise ValueError('Password is not long enough!')
        self.password = new_password

print(f"Users' quantity: {User.user_count}")
user1 = User('Alele', '4895893502')
print(f"Users' quantity: {User.user_count}")
user2 = User('Shama', '0349204955')
print(f"Users' quantity: {User.user_count}")
user1.test()
user2.test()
print(f'Passwords: {user2.password}, {user1.password}')
print(f'Class attributes: {User.user_count}, {User.default_password}')
admin1 = User.create_admin("Marsel", "996508040430")
print(f"Admin user: {admin1.name}, {admin1.phone}, {admin1.password}, {admin1.role}")
# print(User.get_user_count())
print(User.validate_password('[[[[[[[[[[[[[['))
user1.change_password('1')