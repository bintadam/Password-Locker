import pyperclip

class credentials:
   '''
   Class that generates new instances of credentials for users
   '''

   credentials_list = [] # Empty credentials list
 
   def __init__(self,username, account,password):
      '''
      method that defines properties of a user
      '''

      self.username = username
      self.password = password
      self.account = account

   def save_credentials(self):

      '''
      save credentials method saves credentials objects into credentials_list
      '''
        
      credentials.credentials_list.append(self)

   def delete_credentials(self):
      '''
      delete_credentIals method deletes credentials objects into credentials_list
      '''
      
      credentials.credentials_list.remove(self)

   
   @classmethod
   def find_by_account(cls,account):
      '''
      Method that looks for objects of the credential list of that account.
      '''

      for credentials in cls.credentials_list:
          if credentials.username == username:
              return credentials
    

   @classmethod
   def username_exist(cls,number):
      '''
      Method that checks if a username exists from the username list.
      '''
      for credentials in cls.credentials_list:
          if credentials.username== username:
              return True

      return False 


   @classmethod
   def display_credentials(cls):
        '''
        method that returns the credentials list
        '''
        return cls.credentials_list


   @classmethod
   def copy_password(cls, account):
        credentials_found = credentials.find_by_account(account)
        pyperclip.copy(credentials_found.password)     