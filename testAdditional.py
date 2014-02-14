import unittest
import os
import testLib

SUCCESS = 1
ERR_BAD_CREDENTIALS = -1 
ERR_USER_EXISTS = -2
ERR_BAD_USERNAME = -3
ERR_BAD_PASSWORD = -4
MAX_USERNAME_LENGTH = 128
MAX_PASSWORD_LENGTH = 128

class TestAdd(testLib.RestTestCase):
    
    def testAdd_success(self):
        data = self.makeRequest("/users/add", method="POST", data = {'user': 'test', 'password': 'password'})
        self.assertTrue('errCode' in data)
        self.assertEqual(data['errCode'], SUCCESS)
        self.assertTrue('count' in data)
        self.assertEqual(data['count'], 1)

    def testAdd_empty(self):
        data = self.makeRequest("/users/add", method="POST", data = {'user': '', 'password': 'password'})
        self.assertTrue('errCode' in data)
        self.assertEqual(data['errCode'], ERR_BAD_USERNAME)
        self.assertTrue('count' not in data)
    
    def testAdd_emptypw(self):
        data = self.makeRequest("/users/add", method="POST", data={'user': 'test', 'password': ''})
        self.assertTrue('errCode' in data)
        self.assertEqual(data['errCode'], SUCCESS)
        self.assertTrue('count' in data)
        self.assertEqual(data['count'], 1)

    def testAdd_long(self):
        data = self.makeRequest("/users/add", method="POST", data = {'user': 'loremipsumsitametdolorloremipsumsitametdolorloremipsumsitametdolorloremipsumsitametdolorloremipsumsitametdolorloremipsumsitametdolorloremipsumsitametdolorloremipsumsitametdolor', 'password': 'password'})
        self.assertTrue('errCode' in data)
        self.assertEqual(data['errCode'], ERR_BAD_USERNAME)
        self.assertTrue('count' not in data)        

    def testAdd_longpw(self):
        data = self.makeRequest("/users/add", method="POST", data = {'user': 'test', 'password': 'loremipsumsitametdolorloremipsumsitametdolorloremipsumsitametdolorloremipsumsitametdolorloremipsumsitametdolorloremipsumsitametdolorloremipsumsitametdolorloremipsumsitametdolor'})
        self.assertTrue('errCode' in data)
        self.assertEqual(data['errCode'], ERR_BAD_PASSWORD)
        self.assertTrue('count' not in data)       

    def testAdd_exist(self):
        data = self.makeRequest("/users/add", method="POST", data = {'user': 'test', 'password': 'password'})
        data = self.makeRequest("/users/add", method="POST", data = {'user': 'test', 'password': 'password'})
        self.assertTrue('errCode' in data)       
        self.assertEqual(data['errCode'], ERR_USER_EXISTS)
        self.assertTrue('count' not in data)

class TestLogin(testLib.RestTestCase):

    def testLogin_success(self):
        data = self.makeRequest("/users/add", method="POST", data = {'user': 'test', 'password': 'password'})
        data = self.makeRequest("/users/login", method="POST", data = {'user': 'test', 'password': 'password'})
        self.assertTrue('errCode' in data)
        self.assertEqual(data['errCode'], SUCCESS)

    def testLogin_failure(self):
        data = self.makeRequest("/users/login", method="POST", data = {'user': 'test', 'password': 'password'})
        self.assertTrue('errCode' in data)
        self.assertEqual(data['errCode'], ERR_BAD_CREDENTIALS)
        self.assertTrue('count' not in data)