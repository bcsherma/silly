import wandb
from wandb.sdk.launch import template

config = {
    "param1": 1,
    "param2": 2,
    "param3": 3,
    "param4": [1, 2, 3],
}

run = wandb.init(config=config)

run.log_code(".", include_fn=lambda x: x.endswith("main.py"))

template.add_parameter(template.WandbConfigKeys(include=["param1", "param2"]))
template.add_parameter(template.ConfigFile("test.yaml"))

run.finish()
