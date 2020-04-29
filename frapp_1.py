#!/bin/bash/env python3
# -*- coding: utf-8 -*-

def my_logo():
    print("\033[1;33mXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxX\n")
    print("\033[1;34mcreated fatih kılavuz  [https://github.com/fatihklavuz]\n")
    print("\033[1;33mooooooooooooooooooooooooooooooooooo")
    print("\033[1;33mo                                 o")
    print("\033[1;33mo           frapp                 o   ")
    print("\033[1;33mo                                 o")
    print("\033[1;33mo     Password Generator          o   ")
    print("\033[1;33mo                                 o")
    print("\033[1;33mooooooooooooooooooooooooooooooooooo")
    print("\n")


my_logo()


import random
import string



print(" What do you have your password: ")
print("*********************************")
print("1==> Numbers Only")
print("2==> Letters Only")
print("3==> Numbers and Letters")
print("4==> Numbers Letters and Specials Characters")
print("5==> Give Me Five :)")
print("6==> I want to set the criteria ")
cho=int(input("Make your Choice : ") )

if cho == 1:
        chr_lng=int(input((" How many digits do you want? : ")))
        def rndstr(crclng=chr_lng):
            passw=string.digits
            return ''.join(random.choice(passw) for i in range(crclng)) 
elif cho == 2:
         chr_lng=int(input((" How many digits do you want? : ")))
         def rndstr(crclng=chr_lng):
            passw=string.ascii_letters
            return ''.join(random.choice(passw) for i in range(crclng))        
elif cho == 3:
          chr_lng=int(input((" How many digits do you want? : ")))
          def rndstr(crclng=chr_lng):
            passw=string.digits+string.ascii_letters
            return ''.join(random.choice(passw) for i in range(crclng)) 
        
elif cho == 4:
          chr_lng=int(input((" How many digits do you want? : ")))
          def rndstr(crclng=chr_lng):
            spc_crc="!#$%&_-{}"
            passw=string.digits+string.ascii_letters+spc_crc
            return ''.join(random.choice(passw) for i in range(crclng))
elif cho == 5:
          chr_lng=10
          def rndstr(crclng):
            spc_crc="!#$%&_-{}"
            passw=string.digits+string.ascii_letters+spc_crc
            return ''.join(random.choice(passw) for i in range(crclng))          
        
print("\n")        
print("\033[1;36m","****************\n")       
print("\033[1;36m"," ",rndstr(chr_lng))
print("\n") 
print("\033[1;36m","****************")


 

 

