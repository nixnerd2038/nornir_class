import os
from nornir import InitNornir
from nornir.core.filter import F
from nornir.plugins.tasks.networking import netmiko_send_command
from nornir.plugins.functions.text import print_result
from pprint import pprint

def exercise_4abc():
    nr = InitNornir(config_file="config.yaml")
    arista_devices = nr.filter(F(groups__contains="eos"))
    cmd = "show int status"
    res = arista_devices.run(
        task=netmiko_send_command,
        command_string=cmd,
        use_textfsm=True
    )
    all_ints = {}
    for device, dev_res in res.items():
        all_ints[device] = {}
        for result in dev_res.result:
            all_ints[device].update({result['port']: {'status': result['status'], 'vlan': result['vlan']}})
            # all_ints.update(dm)
    pprint(all_ints)

def main():
    exercise_4abc()

if __name__ == "__main__":
    main()