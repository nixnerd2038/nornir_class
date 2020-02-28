#!/usr/bin/env python

from nornir import InitNornir
from nornir.core.filter import F
from nornir.plugins.tasks.networking import napalm_get
from nornir.plugins.functions.text import print_result

DEFAULT_GATEWAY = ("10.220.88.1")

def ex4():
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
            import ipdb; ipdb.set_trace()
            if DEFAULT_GATEWAY == entry['ip']:
                desired = output
                break
        parsed_results.append((host, desired))

    for host, res in parsed_results:
        print('--')
        print(f"Host: {host} || GW: {res}")
        print('--')

def main():
    ex4()

if __name__=="__main__":
    main()