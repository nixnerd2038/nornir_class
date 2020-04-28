import os
from nornir import InitNornir
from nornir.core.filter import F
from nornir.plugins.tasks.networking import netmiko_send_command
from nornir.plugins.functions.text import print_result

def exercise_2a():
    nr = InitNornir(config_file="config.yaml")
    arista_hosts = nr.filter(name="arista1")
    for host in arista_hosts.inventory.hosts: 
        print(f"ARISTA1 HOST: {host}")

def exercise_2b():
    nr = InitNornir(config_file="config.yaml")
    wan_hosts = nr.filter(role="WAN")
    for i, host in enumerate(wan_hosts.inventory.hosts): 
        print(f"WAN HOST {i+1}: {host}")

def exercise_2c():
    nr = InitNornir(config_file="config.yaml")
    sfo_filt = F(groups__contains="sfo")
    sfo_hosts = nr.filter(sfo_filt)
    for i, host in enumerate(sfo_hosts.inventory.hosts): 
        print(f"SFO HOST {i+1}: {host}")

def main():
    exercise_2a()
    exercise_2b()
    exercise_2c()

if __name__=="__main__":
    main()