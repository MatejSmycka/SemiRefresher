import json
import requests
import re
import URLs
import time
import datetime

def main(): 

 
   def prihlaseni():
    for i in URLs.urls:
       try:
          response = requests.get(i,  cookies=URLs.cookies) 
       except HTTPError as http_err:
          print(f'HTTP error occurred: {http_err}')
       except Exception as err:
          print(f'Other error occurred: {err}')
       else:
          print("Zadost byla podana")
          
       obsah= str(response.content)
       string= "semin.xc3.xa1rn.xc3.xad skupiny p.xc5.x99ihl.xc3.xa1.xc5.xa1en.a"
       
       try:
          search = re.search(string,obsah).group()
          if search:
             print("Prihlaseno nebo nezmeneno")
       except: 
             print("NEPRIHLASENO")
             prihlaseni()

   def odpocet():
    Check = False
    
    while Check == False:
     t = time.localtime()
     current_time = time.strftime("%H%M%S", t)  
     current_time = int(current_time)+60000      
     print(current_time)   
      
     if current_time >= 170000:
       prihlaseni()
       Check = True 
     
    
   odpocet()      
   
     
   
if __name__ == '__main__':
    main()
    
    
    
