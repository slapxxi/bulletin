from users.models import User


def create_user():
  user = User(username='user')
  user.set_password('password')
  user.save()
  return user

def destroy_users():
  return User.objects.all().delete()
