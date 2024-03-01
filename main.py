import wandb
import yaml
from wandb.sdk.launch import template

config = {
    "param1": 1,
    "param2": 2,
}

run = wandb.init(config=config)

template.add_parameter(template.WandbConfigKeys(include=["param1", "param2"]))
template.add_parameter(template.ConfigFile("test.yaml"))

wandb.config.update(yaml.load(open("test.yaml"), Loader=yaml.FullLoader))

run.finish()
