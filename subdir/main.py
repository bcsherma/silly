import wandb

with wandb.init():
    wandb.log({"hello": "world"})
