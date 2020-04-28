import os
from nornir import InitNornir
from nornir.core.filter import F
from nornir.plugins.tasks.networking import netmiko_send_command
from nornir.plugins.functions.text import print_result

def exercise_1a():
    """Nornir Inventory data inheritance works from host > group > defaults. Calling 'data' method on a host only returns the hostvars
    """
    nr = InitNornir(config_file="config.yaml")
    print(nr.inventory.hosts['arista3'].data) # host-specific variables
    print(nr.inventory.hosts['arista3'].items()) # supports inheritance from groups and defaults

def exercise_1b():
    nr = InitNornir(config_file="config.yaml")
    for host, dataobj in nr.inventory.hosts.items():
        print(f"Host: {host}, TZ: {dataobj['timezone']}")


def main():
    exercise_1a()
    exercise_1b()

if __name__ == "__main__":
    main()