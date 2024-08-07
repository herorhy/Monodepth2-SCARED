# Copyright Niantic 2019. Patent Pending. All rights reserved.
#
# This software is licensed under the terms of the Monodepth2 licence
# which allows for non-commercial use only, the full terms of which are made
# available in the LICENSE file.

from __future__ import absolute_import, division, print_function

from trainer import Trainer
from options import MonodepthOptions
import torch

options = MonodepthOptions()
opts = options.parse()


if __name__ == "__main__":

    torch.hub.set_dir('/home/ubuntu/disk1/RHY/.cache')
    trainer = Trainer(opts)
    trainer.train()
