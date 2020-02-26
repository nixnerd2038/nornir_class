#!/usr/bin/env python

from nornir import InitNornir
from nornir.core.filter import F
from nornir.plugins.tasks.networking import napalm_get
from nornir.plugins.functions.text import print_result

DEFAULT_GATEWAY = ("10.220.88.1")

def ex4():
    """Using NAPALM to get the arp table
        takeaways: NAPALM, using structured data as output and logic, storing 
        output in a list and re-referencing
    """
    ios_filt = F(groups__contains="ios")
    eos_filt = F(groups__contains="eos")
    nr = InitNornir(config_file="config.yaml")
    nr = nr.filter(ios_filt | eos_filt)
    cmd = "arp_table"
    result = nr.run(
        task=napalm_get,
        getters=cmd
    )
    parsed_results = []
    for host, dd in result.items():
        output = dd[0].result["arp_table"]
        desired = ""
        for entry in output:
            if DEFAULT_GATEWAY == entry['ip']:
                desired = entry
                break # stop checking, we found it
        parsed_results.append((host, desired)) # append as tuple for easier printing, 
                                               # would want to store as dict if further processing maybe

    for host, res in parsed_results:
        print('--')
        print(f"Host: {host} || GW: {res}")
        print('--')

def main():
    ex4()

if __name__=="__main__":
    main()