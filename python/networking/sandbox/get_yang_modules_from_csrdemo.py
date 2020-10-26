from ncclient import manager


access = {"host": "ios-xe-mgmt.cisco.com", "port": "10000", 
          "username": "developer", "password": "C1sco12345"}


with manager.connect(host=access["host"], port=access["port"], username=access["username"], 
                     password=access["password"], hostkey_verify=False) as conection:
    for module in conection.server_capabilities:
        print(module)
    conection.close_conections
