from rest_framework.authtoken.models import Token
from collect.models import User

# This may just be leftover code, but you shouldn't be running something globally like this in a utils file
for user in User.objects.all():
    Token.objects.get_or_create(user=user)
