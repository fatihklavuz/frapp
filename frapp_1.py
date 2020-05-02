#!/bin/bash/env python3
# -*- coding: utf-8 -*-



def mylogo():
    
    print("""
     \033[1;33mXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxX\n  
           \033[1;34mcreated fatih kılavuz\n
      \033[1;34mhttps://github.com/fatihklavuz\n
     \033[1;33mooooooooooooooooooooooooooooooooooo
     \033[1;33mo                                 o
     \033[1;33mo           frapp                 o
     \033[1;33mo                                 o
     \033[1;33mo    Simple Password Generator    o
     \033[1;33mo                                 o
     \033[1;33mooooooooooooooooooooooooooooooooooo
     \n
          
          """)

mylogo()

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
adt=int(input("Have many password : "))
wrt=str(input("You Want a Wordlist File y or n : "))
chr_lng=int(input((" How many digits do you want? : ")))


#Choice 1 start#

if cho == 1 and wrt == 'y':
     
        def rndstr(crclng=chr_lng):
            passw=string.digits
            return ''.join(random.choice(passw) for i in range(crclng))
        for i in range (adt):
            print("file processing...")
            wrt_out_num=open("frappwlistnum.txt","a")
            wrt_out_num.write(rndstr(chr_lng))
            wrt_out_num.write("\n")
            wrt_out_num.close()
if wrt == 'n':
         def rndstr(crclng=chr_lng):
            passw=string.digits
            return ''.join(random.choice(passw) for i in range(crclng))
              
         for i in range (adt):
          print("\033[1;36m"," ",rndstr(chr_lng))
         
#Choice 1 end#        


#Choice 2 start#
 
elif cho == 2 and wrt== 'y':
         
          def rndstr(crclng=chr_lng):
            passw=string.ascii_letters
            return ''.join(random.choice(passw) for i in range(crclng))
            
          for i in range (adt):
            print("file processing...")
            wrt_out_lett=open("frappwlistlett.txt","a")
            wrt_out_lett.write(rndstr(chr_lng))
            wrt_out_lett.write("\n")
            wrt_out_lett.close()
            
if wrt == 'n' :
    
    def rndstr(crclng=chr_lng):
            passw=string.ascii_letters
            return ''.join(random.choice(passw) for i in range(crclng))
        
    for i in range (adt):
          print("\033[1;36m"," ",rndstr(chr_lng))
            
#Choice 2 end#          
          
#Choice 3 start# 
          
elif cho == 3 and wrt =='y':
         
          def rndstr(crclng=chr_lng):
            passw=string.digits+string.ascii_letters
            return ''.join(random.choice(passw) for i in range(crclng))
          for i in range (adt):
            print("file processing...")
            wrt_out_numlet=open("frappwlistnumlet.txt","a")
            wrt_out_numlet.write(rndstr(chr_lng))
            wrt_out_numlet.write("\n")
            wrt_out_numlet.close()

if wrt == 'n':
     def rndstr(crclng=chr_lng):
            passw=string.digits+string.ascii_letters
            return ''.join(random.choice(passw) for i in range(crclng))
     for i in range (adt):
          print("\033[1;36m"," ",rndstr(chr_lng))
              
              
#Choice 3 end# 
 
#Choice 4 start#
         
elif cho == 4 and wrt == 'y':
         
          def rndstr(crclng=chr_lng):
            spc_crc="!#$%&_-{}"
            passw=string.digits+string.ascii_letters+spc_crc
            return ''.join(random.choice(passw) for i in range(crclng))
          for i in range (adt):
            print("file processing...")
            wrt_out_numletspc=open("frappwlistnumlesspc.txt","a")
            wrt_out_numletspc.write(rndstr(chr_lng))
            wrt_out_numletspc.write("\n")
            wrt_out_numletspc.close()
if wrt == 'n':
          def rndstr(crclng=chr_lng):
            spc_crc="!#$%&_-{}"
            passw=string.digits+string.ascii_letters+spc_crc
            return ''.join(random.choice(passw) for i in range(crclng))
          for i in range (adt):
           print("\033[1;36m"," ",rndstr(chr_lng))
           
#Choice 4 end#
       
        
        
#Choice 5 start#
           
        
elif cho == 5 and wrt == 'y':
          chr_lng=10
          def rndstr(crclng):
            spc_crc="!#$%&_-{}"
            passw=string.digits+string.ascii_letters+spc_crc
            return ''.join(random.choice(passw) for i in range(crclng))
          
          for i in range (adt):
             print("file processing...")
             wrt_out_rnd=open("frappwlistrnd.txt","a")
             wrt_out_rnd.write(rndstr(chr_lng))
             wrt_out_rnd.write("\n")
             wrt_out_rnd.close() 
             
if wrt == 'n':
     def rndstr(crclng):
            spc_crc="!#$%&_-{}"
            passw=string.digits+string.ascii_letters+spc_crc
            return ''.join(random.choice(passw) for i in range(crclng))
    
     for i in range (adt):
      print("\033[1;36m"," ",rndstr(chr_lng))     
             
#Choice 5 end#
         
#Choice 6 Start#

'to be written'



#Choice 6 end#      
             



 

 

