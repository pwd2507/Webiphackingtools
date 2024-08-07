print("""
                  ___.     .__           .__                         __                      
__  _  __   ____   \_ |__   |__| ______   |  |__   _____      ____   |  | __   ____   _______ 
\ \/ \/ / _/ __ \   | __ \  |  | \____ \  |  |  \  \__  \   _/ ___\  |  |/ / _/ __ \  \_  __ \
 \     /  \  ___/   | \_\ \ |  | |  |_> > |   Y  \  / __ \_ \  \___  |    <  \  ___/   |  | \/
  \/\_/    \___  >  |___  / |__| |   __/  |___|  / (____  /  \___  > |__|_ \  \___  >  |__|   
               \/       \/       |__|          \/       \/       \/       \/      \/          
               made by korea yh middle school, hojunnam
""")
print("login")
name = input("Enter your name: ")
print(f"Hello, {name}!")

from socket import gethostbyname
ip_address = gethostbyname(input("webip no http: "))
print(ip_address)
