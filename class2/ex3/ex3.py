#!/usr/bin/env python

from nornir import InitNornir
from nornir.core.filter import F
from nornir.plugins.tasks.networking import netmiko_send_command
from nornir.plugins.functions.text import print_result

DEFAULT_GATEWAY = ("10.220.88.1")

def exercise_3():
    """Get ip arp and format results
         takeaways: multigroup filters, netmiko_send_command, filtering parsed results
    """
    ios_filt = F(groups__contains="ios")
    eos_filt = F(groups__contains="eos")
    nr = InitNornir(config_file="config.yaml")
    nr = nr.filter(ios_filt | eos_filt)
    cmd = "show ip arp"
    result = nr.run(
        task=netmiko_send_command,
        command_string=cmd
    )

    parsed_res = []

    # get just the DG line
    for host, dd in result.items():
        output = dd[0].result
        for line in output.splitlines():
            if DEFAULT_GATEWAY in line:
                parsed_res.append({host:line}) # this is better done with a tuple, see exercise4

    # print table-like result
    # this is better done with a tuple, see exercise4
    for res in parsed_res:
        for k,v in res.items():
            print(f"Host: {k} || Gateway: {v}")

def main():
    exercise_3()

if __name__=="__main__":
    main()