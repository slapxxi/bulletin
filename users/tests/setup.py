from users.models import User


def create_user():
  user = User(username='user')
  user.set_password('password')
  user.save()
  return user

def destroy_user():
  return User.objects.get(username='user').delete()

def destroy_users():
  return User.objects.all().delete()

def user():
  return User.objects.first()
