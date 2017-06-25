# -*- coding=utf-8 -*-
# file =  control
# time = 2017/6/18 22:23 
# user = "W.Tj"
# email = "wangtengjiao1@gmail.com"

# 加密工具
from django.contrib.auth.hashers import make_password, check_password




class Validator(object):

    def __init__(self, name, password):
        self.name = name
        self.password =password

    def existence(self):
        from models import User
        if User.objects.filter( NameID=self.name):
            return True
        else:
            return False

class EncryptionDevice(object):
    def __init__(self, clear, cipher):
        self.clear = clear
        self.cipher = cipher
