#!/bin/bash/env python3
# -*- coding: utf-8 -*-

print("XXXXXXXXXXXXXXXXXXXXXXXXXXXX\n")
print("Simple Password Generator\n")
print("Created Fatih_Kılavuz\n")
print("XXXXXXXXXXXXXXXXXXXXXXXXXXXX\n")


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
        
        
        
print(rndstr(chr_lng))
        
    
      





