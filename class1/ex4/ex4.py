#!/usr/bin/env python

from nornir import InitNornir

def my_task(task):
    import ipdb; ipdb.set_trace()
    print(task.host.hostname)
    print('---')

if __name__ == "__main__":
    nr = InitNornir()
    nr.run(task=my_task) # is this recursive...?
