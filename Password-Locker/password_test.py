import unittest # Importing the unittest module
from password import User # Importing the password class

class TestUser(unittest.TestCase):

    def setUp(self):
      '''
      Set up method to run before each test cases.
      '''
      self.new_user = User("Bintadam","password") # create contact object


    def test_init(self):
      '''
      test_init test case to test if the class has been initialized properly
      '''

      self.assertEqual(self.new_user.username, "Bintadam")
      self.assertEqual(self.new_user.password,"password")
        

if __name__ == '__main__':
    unittest.main()
    
    def test_save_user(self):
        '''
        test_save_user test case to test if the new user is saved into
         the user list
        '''
        self.new_user.test_save_user() # saving the new user
        self.assertEqual(len(User.user_list),1)


   