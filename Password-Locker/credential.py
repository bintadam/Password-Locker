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
    def find_by_number(cls,number):
        '''
        Method that takes in a number and returns a contact that matches that number.

        Args:
            number: Phone number to search for
        Returns :
            Contact of person that matches the number.
        '''

        for contact in cls.contact_list:
            if contact.phone_number == number:
                return contact
    