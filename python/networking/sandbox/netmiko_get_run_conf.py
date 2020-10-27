from netmiko import ConnectHandler


access = {"host": "ios-xe-mgmt.cisco.com", "port": "8181", 
          "username": "developer", "password": "C1sco12345", 
          "device_type": "cisco_ios"}


try:
    connection = ConnectHandler(**access)
    connection.enable()
    sh_run = connection.send_command("show run")
    connection.disconnect()
except Exception as ex:
    print(ex)
else:
    print(sh_run)