#!/usr/bin/env python

from nornir import InitNornir

def main():

    nr = InitNornir()

    for host_name, host_attr in nr.inventory.hosts.items():
        print(f"host: {host_name}")
        print(f"hostname: {host_attr.hostname}")
        print(f"platform: {host_attr.platform}")
        print(f"groups: {host_attr.groups}")
        print(f"user: {host_attr.username}")
        print(f"passwd: {host_attr.password}")
        print(f"port: {host_attr.port}")
main()
