#!/usr/bin/env python

import os
from nornir import InitNornir
from nornir.core.filter import F
from nornir.plugins.tasks.networking import netmiko_send_command
from nornir.plugins.functions.text import print_result

DEFAULT_GATEWAY = ("10.220.88.1")

def exercise_5a():
    """Get int br from ios devices
    """
    ios_filt = F(groups__contains="ios")
    nr = InitNornir(config_file="config.yaml")
    nr = nr.filter(ios_filt)
    cmd = "show ip interface brief"
    result = nr.run(
        task=netmiko_send_command,
        command_string=cmd
    )
    print_result(result)

def exercise_5b():
    """Get int br with bad password
         takeaways: printing failures
    """
    ios_filt = F(groups__contains="ios")
    nr = InitNornir(config_file="config.yaml")
    nr.inventory.hosts["cisco3"].password = 'bogus'
    nr = nr.filter(ios_filt)
    cmd = "show ip interface brief"
    result = nr.run(
        task=netmiko_send_command,
        command_string=cmd
    )
    print_result(result)
    print(result.failed_hosts)
    print(nr.data.failed_hosts)

def exercise_5cd():
    """Get int br with bad password
         takeaways: handling failures
    """
    ios_filt = F(groups__contains="ios")
    nr = InitNornir(config_file="config.yaml")
    nr.inventory.hosts["cisco3"].password = 'bogus'
    nr = nr.filter(ios_filt)
    cmd = "show ip interface brief"
    result = nr.run(
        task=netmiko_send_command,
        command_string=cmd
    )
    print_result(result)

    failed_hosts = result.failed_hosts
    if failed_hosts:
        for host, obj in failed_hosts.items():
            try:
                # Remove failed host from the Nornir connection table
                nr.inventory.hosts[host].close_connections()
            except ValueError:
                pass
            print(f"{host} : {obj.result}")
            print()
            print(f"Trying again...")
            print()
            nr.inventory.hosts[host].password = os.getenv("NORNIR_PASSWORD")
            result = nr.run(
                task=netmiko_send_command,
                command_string=cmd,
                on_failed=True
            )
            print_result(result)


            

def main():
    exercise_5a()
    exercise_5b()
    exercise_5cd()

if __name__=="__main__":
    main()
