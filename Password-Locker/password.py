import pyperclip

class User:
   '''
   Class that generates new instances of users
   '''

   user_list = [] # Empty user list
 
   def __init__(self,username,password):
      '''
      method that defines properties of a user
      '''

      self.username = username
      self.password = password

   def save_user(self):

      '''
      save user method saves contact objects into user_list
      '''
        
      User.user_list.append(self)

   def delete_user(self):
      '''
      delete_user method deletes contact objects into user_list
      '''
      
      User.user_list.remove(self)


   
   