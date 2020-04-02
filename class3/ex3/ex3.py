import os
from nornir import InitNornir
from nornir.core.filter import F
from nornir.plugins.tasks.networking import netmiko_send_command
from nornir.plugins.functions.text import print_result

def exercise_3a():
    nr = InitNornir(config_file="config.yaml")
    agg_filter = F(role__contains="AGG")
    agg_hosts = nr.filter(agg_filter)
    for host in agg_hosts.inventory.hosts:
        print(f"AGG HOST: {host}")

def exercise_3b():
    nr = InitNornir(config_file="config.yaml")
    seasfo_filter = F(groups__contains="sfo")|F(groups__contains="sea")
    seasfo_hosts = nr.filter(seasfo_filter)
    for i, host in enumerate(seasfo_hosts.inventory.hosts):
        print(f"SEA_SFO Host {i+1}: {host}")

def exercise_3c():
    nr = InitNornir(config_file="config.yaml")
    wrc_filter = F(role__contains="WAN")&F(site_details__wifi_password__contains="racecar")
    wrc_hosts = nr.filter(wrc_filter)
    for i, host in enumerate(wrc_hosts.inventory.hosts):
        print(f"WRC Host {i+1}: {host}")


def main():
    exercise_3a()
    exercise_3b()
    exercise_3c()

if __name__=="__main__":
    main()