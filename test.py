import string
import random


s1 = list(string.ascii_lowercase)
random.shuffle(s1)
    
s2 = list(string. ascii_uppercase)
random.shuffle(s2)
    
s3 = list(string.digits)
random.shuffle(s3)
    
s4 = list(string.punctuation)
random.shuffle(s4)

length = int(input('Enter the Length of your password:'))
if int(length) != int :
          raise TypeError("input must be a positive integer")

if __name__  == "__main__":
    

    passwordList = []
    upperIndex = 0
    lowerIndex = 0
    numberIndex = 0
    charIndex = 0
  
    while True:
        passwordList.extend(s2[upperIndex]) 
        passwordList.extend(s1[lowerIndex])
        passwordList.extend(s3[numberIndex])
        passwordList.extend(s4[charIndex])
             
        
        if upperIndex==25:
            upperIndex = 0
        else:
            upperIndex += 1

        if lowerIndex==25:
            lowerIndex = 0
        else:
            lowerIndex += 1

        if numberIndex==9:
            numberIndex = 0
        elif numberIndex != 9:
            numberIndex += 1

        if charIndex == 31:
            charIndex = 0
        elif charIndex != 31:
            charIndex += 1

        if len(passwordList) > length:
            break
        
password = (''.join(passwordList[0:length]))
print('Your Password is',password)   
random.shuffle(passwordList)
password = (''.join(passwordList[0:length]))
print('Your Password is',password)    
save = str(input('Save(y/n):'))
if  save == 'y':
        file = open('Passwords.txt','a')
        name = input('Name:')
        file.write(f'{name} = {password}\n')
        file.close()
else:
    pass