import random
import string

#conditons
# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

userMode = int(input("Select a mode (1: Encoding| 2: Decoding)\n>>> "))

userInput = input("Enter input\n>>> ").lower()

randomStr1 = "".join(random.choice(string.ascii_lowercase) for i in range(3))
randomStr2 = "".join(random.choice(string.ascii_lowercase) for i in range(3))

def encoding():
    '''This function will take the userinput and encode it as per the instructions'''
    global result
    result = ""
    lst = list(userInput)
    if len(str(userInput)) >= 3:
        x = lst.pop(0)
        lst.append(x)
        return randomStr1+result.join(lst)+randomStr2
    else:
        lst.reverse()
        return randomStr1+result.join(lst)+randomStr2
    
def decoding():
    '''This function will take the userinput and decode it as per the instructions'''
    global result
    result = ""
    lst = list(userInput)
    if len(str(userInput)) >= 3:
        lst = lst[3:-3]
        x = lst.pop()
        lst.insert(0, x)
        return result.join(lst)
    else:
        lst = lst[3:-3]
        lst.reverse()
        return result.join(lst)


if userMode == 1:
    print(encoding())
elif userMode == 2:
    print(decoding())
else:
    raise ValueError("Invalid mode selected.")