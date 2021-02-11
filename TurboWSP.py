import requests
import time
import fake_useragent


print(f""" 

      ____   
     /___/\_                                
    _\   \/_/\__                 ________________       
  __\       \/_/\               |    TurboWSP    |
  \   __    __ \ \              |Version: 1.0   |    
 __\  \_\   \_\ \ \   __        |Author: opostal1|
/_/\\   __   __  \ \_/_/\        ------------------  
\_\/_\__\/\__\/\__\/_\_\/         
   \_\/_/\       /_\_\/              
      \_\/       \_\/               
                   
""")

time.sleep(1)

print("[1] WebSite Parser (in terminal)")
print("[2] WebSite Parser (in html file)")

opt = int(input("select: "))

if opt ==1:
	time.sleep(1)

	user = fake_useragent.UserAgent().random
	header = {'user-agent': user}
	link = (input("Enter link with http or https: "))
	user = fake_useragent.UserAgent().random
	header = {'user-agent': user}

	responce = requests.get(link).text
	print(responce)

	print("Exiting...")
	time.sleep(0.8)
elif opt ==2:
	user = fake_useragent.UserAgent().random
	header = {'user-agent': user}


	link = input("Enter link with http or https: ")
	responce1 = requests.get(link).text
	
	with open ("1.html", "w", encoding="utf-8") as file:
		file.write(responce1)
	print("Html file saved!")
	time.sleep(0.4)	
	print("Exiting...")
	time.sleep(0.8)
else:
	print("Not correct argument!")