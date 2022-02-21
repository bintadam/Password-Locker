import unittest # Importing the unittest module
from password import User # Importing the password class
from credential import credentials # Importing the credential class


class TestUser(unittest.TestCase):

    def setUp(self):
      '''
      Set up method to run before each test cases.
      '''
      self.new_user = User("bint-den","password") # create contact object


    def test_init(self):
      '''
      test_init test case to test if the class has been initialized properly
      '''

      self.assertEqual(self.new_user.username, "bint-den")
      self.assertEqual(self.new_user.password,"password")
        
    
    def test_save_user(self):
        '''
        test_save_user test case to test if the new user is saved into
         the user list
        '''
        self.new_user.test_save_user() # saving the new user
        self.assertEqual(len(User.user_list),1)


    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        User.user_list = []

    def test_delete_user(self):
        '''
        test_delete_user to test if we can remove a contact from our user list
        '''
        self.new_user.save_user()
        test_user = User("bint-den","password")         
        test_user.save_user()

        self.new_user.delete_user()# Deleting a user object
        self.assertEqual(len(User.user_list),1)
    

class Testcredentials(unittest.TestCase):

    def setUp(self):
      '''
      Set up method to run before each test cases.
      '''
      self.new_credentials = credentials("bint-den","instagram","password") # create contact object
