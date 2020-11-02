from ncclient import manager


access = {
    "host": "ios-xe-mgmt.cisco.com", 
    "port": "10000", 
    "username": "developer", 
    "password": "C1sco12345",
    "hostkey_verify" : False 
    }


with manager.connect(**access) as conection:
    for module in conection.server_capabilities:
        print(module)
    conection.close_conections
