import math
import pyro.distributions as dist
import torch
from mainframe.components.core import deterministic, stochastic


def test_stochastic():
    normal = stochastic("normal", dist.Normal(0, 1))

    assert isinstance(normal, torch.Tensor)


def test_deterministic():
    number = deterministic("number", 5 + torch.tensor([3]))

    assert isinstance(number, torch.Tensor)
    assert number == torch.Tensor([8])


def test_deterministic_and_stochastic():
    noise = stochastic("noise", dist.Normal(0, 1))

    trend = deterministic("trend", 5 + noise)

    assert isinstance(noise, torch.Tensor)
    assert isinstance(trend, torch.Tensor)

    assert trend.reshape([1]) - torch.tensor([5]) == noise
