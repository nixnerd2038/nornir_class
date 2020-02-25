#!/usr/bin/env python

from nornir import InitNornir

def my_task(task):
    host = task.host
    print(host.hostname)
    print(f"DNS1: {host['dns1']}")
    print(f"DNS2: {host['dns2']}")
    print()


if __name__ == "__main__":
    nr = InitNornir()
    nr.run(task=my_task)
