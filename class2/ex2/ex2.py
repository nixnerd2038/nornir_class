#!/usr/bin/env python

from nornir import InitNornir
from nornir.core.filter import F

filt = F(groups__contains="ios")
nr = InitNornir(config_file="config.yaml")
nr = nr.filter(filt)
print(nr.inventory.hosts)

