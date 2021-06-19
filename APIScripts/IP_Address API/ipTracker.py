import requests #We'll Extract data using requests module
                #If writing this statement gives you an error, then this module isn't installed in your system
                #To install, type : pip install requests

from simple_colors import * #A module to print bold/italic/underlined texts of different colours
                            #To install, type : pip install simple-colors  

url= "http://ip-api.com/json/" #This URL is related to info about IP Address
url2= "http://8xgcd1gizl6s04w7a300wyxathwtrt5l.edns.ip-api.com/json/" #This URL is related to info about DNS Server

ip=input(cyan("Enter any IP Address (Just hit enter if you want info about your current IP Address)\n","bold"))
print()

data=requests.get(url+ip).json() #No API key required
    
if ip=='': 
    dns_data=requests.get(url2).json() #We can only find info about DNS Server of the IP Address that is currently been used 
        
if data['status']=='fail':
    print(red("You entered a wrong IP Address ","bold"))
        
else:
    print(f'IP ADDRESS: {green(data["query"],"bold")} \n')
    
    print(f'COUNTRY: {green(data["country"],"bold")} \n')
    
    print(f'CITY: {green(data["city"],"bold")} \n')
    
    print(f'REGION: {green(data["regionName"],"bold")} \n')
    
    o=str(data["lat"]) + " degrees"
    print(f'LATITUDE: {green(o,"bold")} \n')
    
    q=str(data["lon"]) + " degrees"
    print(f'LONGITUDE: {green(q,"bold")} \n')
    
    print(f'TIMEZONE: {green(data["timezone"],"bold")}\n')
    
    print(f'ISP: {green(data["isp"],"bold")} \n')
    
    print(f'ORGANISATION: {green(data["org"],"bold")} \n')

    if ip=='':
            
        for i in range(len(dns_data["dns"]["geo"])):
            if dns_data["dns"]["geo"][i]=='-':
                break
            
        dns_name = dns_data["dns"]["geo"][i+2:]
        
        dns_country = dns_data["dns"]["geo"][:i-1]
        
        j=dns_name +" (" + dns_country + ")"
        print(f'YOUR DNS SERVER: {green(j,"bold")} \n')
        
        print(f'IP ADDRESS OF YOUR DNS SERVER: {green(dns_data["dns"]["ip"],"bold")}')
        
