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


   
   