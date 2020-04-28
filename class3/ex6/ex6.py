import os
from nornir import InitNornir
from nornir.core.filter import F
from nornir.plugins.tasks.networking import napalm_get
from nornir.plugins.tasks.networking import netmiko_send_command
from nornir.plugins.functions.text import print_result
from pprint import pprint

def exercise_6ab():
    nr = InitNornir(config_file='config.yaml')
    nxos_devices = nr.filter(F(groups__contains='nxos'))
    cmd = ['config']
    result = nxos_devices.run(
        task=napalm_get,
        getters=cmd,
        getters_options={'config':{'retrieve': 'running'}}
    )
    print_result(result)

def exercise_6c():
    nr = InitNornir(config_file='config.yaml')
    nxos_devices = nr.filter(F(groups__contains='nxos'))
    cmd = ['config', 'facts']
    result = nxos_devices.run(
        task=napalm_get,
        getters=cmd,
        getters_options={'config':{'retrieve': 'running'}}
    )
    print_result(result)

def exercise_6d():
    nr = InitNornir(config_file='config.yaml')
    nxos_devices = nr.filter(F(groups__contains='nxos'))
    cmd = ['config', 'facts']
    result = nxos_devices.run(
        task=napalm_get,
        getters=cmd,
        getters_options={'config':{'retrieve': 'all'}}
    )
    output = {}
    for device, agg_result in result.items():
        output[device] = {}
        output[device]['start_running_match'] = bool(agg_result.result['config']['startup'] == agg_result.result['config']['running'])
        output[device]['model'] = agg_result.result['facts']['model']
        output[device]['vendor'] = agg_result.result['facts']['vendor']
        output[device]['uptime'] = agg_result.result['facts']['uptime']
    pprint(output)

def main():
    exercise_6ab()
    exercise_6c()
    exercise_6d()

if __name__ == "__main__":
    main()