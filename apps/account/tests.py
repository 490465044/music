from django.test import TestCase

# Create your tests here.

from django.contrib.auth.hashers import check_password, make_password

ps = "123456"
dj_ps = make_password(ps, None, 'pbkdf2_sha256')
print dj_ps
