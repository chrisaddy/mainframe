import torch
from mainframe.components.noise import gaussian


def test_gaussian():
    noise = gaussian()

    assert isinstance(noise, torch.Tensor)
