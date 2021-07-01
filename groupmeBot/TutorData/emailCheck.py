# Python program to validate an Email 
import re 
  
# Make a regular expression 
# for validating an Email 
regex = "^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$"
      
# Define a function for 
# for validating an Email 
def check(email):  
  
    # pass the regualar expression 
    # and the string in search() method 
    if(re.search(regex,email)):  
        return True 
          
    else:  
        return False
      
  
# Testing 
if __name__ == '__main__' :  
      
    # Enter the email  
    email = "brjoande@iu.edu"
      
    # calling run function  
    check(email) 

#   does not follo pattern
    email = "hello world"
    check(email) 
  
#   this is shown as valid, it follows pattern
    email = "blahbalhblah@gmail.com"
    check(email)