from users.models import User


class UserSetup:
    def create_user(self, name='user', password='password'):
        user = User(username=name)
        user.set_password(password)
        user.save()
        return user
