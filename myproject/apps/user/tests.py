import unittest
from myproject.apps.user.models import User

# Create your tests here.

SUCCESS = 1
ERR_BAD_CREDENTIALS = -1 
ERR_USER_EXISTS = -2
ERR_BAD_USERNAME = -3
ERR_BAD_PASSWORD = -4
MAX_USERNAME_LENGTH = 128
MAX_PASSWORD_LENGTH = 128

class TestAdd(unittest.TestCase):

    def testAdd_success(self):
        user = User.objects.add(user="hi", password="hello")
        self.assertEqual(user, 1)

    def testAdd_empty(self):
        user = User.objects.add(user="",password="")
        self.assertEqual(user, ERR_BAD_USERNAME)
        
    def testAdd_long(self):
        user = User.objects.add(user="loremipsumsitametdolorloremipsumsitametdolorloremipsumsitametdolorloremipsumsitametdolorloremipsumsitametdolorloremipsumsitametdolor", password="hi")
        self.assertEqual(user, ERR_BAD_USERNAME)
        
    def testAdd_longpw(self):
        user = User.objects.add(user="hi", password="loremipsumsitametdolorloremipsumsitametdolorloremipsumsitametdolorloremipsumsitametdolorloremipsumsitametdolorloremipsumsitametdolor")
        self.assertEqual(user, ERR_BAD_PASSWORD)

    def testAdd_exist(self):
        user1 = User.objects.add(user="hi", password="no")
        user2 = User.objects.add(user="hi", password="no")
        self.assertEqual(user2, ERR_USER_EXISTS)

class TestLogin(unittest.TestCase):

    def addUser(self):
        User.objects.add(user="hi", password="hello")
        User.objects.add(user="hi2", password="hello2")

    def testLogin_success(self):
        login1 = User.objects.login('hi', 'hello')
        self.assertEqual(login1, 2)
        login2 = User.objects.login("hi2","hello2")
        login3 = User.objects.login('hi2', 'hello2')
        self.assertEqual(login3,3)

    def testLogin_notexist(self):
        user = User.objects.login("hi3", password="hello2")
        self.assertEqual(user, ERR_BAD_CREDENTIALS)

    def testLogin_failure(self):
        user = User.objects.login("hi2", "hello")
        self.assertEqual(user, ERR_BAD_CREDENTIALS)

"""
" Reset tests
"""

class ResetTests(unittest.TestCase):

    def addUser(self):
        User.objects.add(user="hi")
        User.objects.add(user="hello")

    def testReset_success(self):
        count = User.objects.all().count()
        self.assertEqual(count, 2)
        User.objects.TESTAPI_resetFixture()
        count = User.objects.all().count()
        self.assertEqual(count, 0)