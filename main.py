import wandb
import yaml
from wandb.sdk.launch.template import ConfigFile, WandbConfigKeys, add_parameter

config = {
    "controllable": 1,
    "uncontrollable": 2
}

run = wandb.init(config=config)

add_parameter(WandbConfigKeys(include=["controllable"]))
add_parameter(ConfigFile("test.yaml"))

wandb.config.update(yaml.load(open("test.yaml"), Loader=yaml.FullLoader))

run.finish()
