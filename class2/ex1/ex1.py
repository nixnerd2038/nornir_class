from nornir import InitNornir

nr = InitNornir()
print(nr.config.core.num_workers)

nr = InitNornir(config_file="config.yaml", core={"num_workers": 15})
print(nr.config.core.num_workers)
