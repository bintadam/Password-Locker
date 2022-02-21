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
