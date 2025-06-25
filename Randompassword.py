import random
import string

if __name__ == "__main__":
 
#include all type of elements to make a strong password
    t1 = string.punctuation
    t2 = string.ascii_letters
    t3 = string.digits

#Taking length of password
    pass_len = int(input("Enter Password Length: "))

#Joining all the elements in one list
    p = []
    p.extend(list(t1))
    p.extend(list(t2))
    p.extend(list(t3))

#Shuffling all elements for strong password
    random.shuffle(p)

#Creating and printing the password
    print("Password: ", "".join(p[0:pass_len]))
