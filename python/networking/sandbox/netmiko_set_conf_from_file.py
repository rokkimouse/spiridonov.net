from netmiko import ConnectHandler


access = {"host": "ios-xe-mgmt.cisco.com", "port": "8181", 
          "username": "developer", "password": "C1sco12345", 
          "device_type": "cisco_ios"}


try:
    connection = ConnectHandler(**access)
    connection.enable()
    connection.send_config_from_file(config_file='conf_for_netmiko.txt')
    sh_run = connection.send_command("show run | beg loopback")
    connection.send_config_from_file(config_file='del_conf_from_dev.txt')
    connection.disconnect()
except Exception as ex:
    print(ex)
else:
    print(sh_run)