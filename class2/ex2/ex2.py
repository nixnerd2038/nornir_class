#!/usr/bin/env python

from nornir import InitNornir
from nornir.core.filter import F
from nornir.plugins.tasks.networking import netmiko_send_command
from nornir.plugins.functions.text import print_result


def exercise_2a():
    """Intro to filters
    """
    filt = F(groups__contains="ios")
    nr = InitNornir(config_file="config.yaml")
    nr = nr.filter(filt)
    print(nr.inventory.hosts)

def exercise_2bcd():
    """filtering and result methods
          takeaways: results have five special methods:
            - host (str) the hostname
            - name (str) thte task name
            - result (dict-like obj called MultiResult) the output of the task
            - failed (bool)
    """
    filt = F(groups__contains="ios")
    nr = InitNornir(config_file="config.yaml")
    nr = nr.filter(filt)
    cmd = "show run | include hostname"
    result = nr.run(
        task=netmiko_send_command,
        command_string=cmd
    )
    print_result(result)
    print(type(result))
    print(result.keys())
    print(result.items())
    print(result.values())
    host_results = result['cisco3']
    print(host_results[0])
    print([x for x in host_results])
    task_result = host_results[0]
    print(type(task_result))
    print(task_result.host)
    print(task_result.name)
    print(task_result.result)
    print(task_result.failed)

def main():
    exercise_2a()
    exercise_2bcd()


if __name__=="__main__":
    main()
