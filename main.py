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

tempOperation = []
finalLst = []
finalStr = ""
def encoding():
    '''This function will take the userinput and encode it as per the instructions'''
    lst = userInput.split(" ")
    for i in range(len(lst)):
        
        randomStr1 = "".join(random.choice(string.ascii_lowercase) for i in range(3))
        randomStr2 = "".join(random.choice(string.ascii_lowercase) for i in range(3))
        tempOperation = list(lst[i])
        if len(lst[i]) >= 3:
            poppedElement = tempOperation.pop(0)
            tempOperation.append(poppedElement)
            result = randomStr1 + "".join(tempOperation) + randomStr2
            finalLst.append(result) 
            # lst[i] = randomStr1+"".join(lst[i])+randomStr2
            # print(lst[i])
        else:
            tempOperation.reverse()
            result = randomStr1+"".join(tempOperation)+randomStr2
            finalLst.append(result)
def decoding():
    '''This function will take the userinput and decode it as per the instructions'''
    lst = userInput.split(" ")
    for i in range(len(lst)):
        tempOperation = list(lst[i])
        if len(lst[i]) >= 3:
            del tempOperation[:3]
            del tempOperation[-3:]
            popped = tempOperation.pop()
            tempOperation.insert(0, popped)
            result = "".join(tempOperation)
            finalLst.append(result)
        else:
            del tempOperation[:3]
            del tempOperation[-3:]
            tempOperation.reverse()
            finalLst.append(tempOperation)
if userMode == 1:
    encoding()
    finalStr = " ".join(finalLst)
    print(finalStr)
elif userMode == 2:
    decoding()
    finalStr = " ".join(finalLst)
    print(finalStr)
else:
    raise ValueError("Invalid mode selected.")

