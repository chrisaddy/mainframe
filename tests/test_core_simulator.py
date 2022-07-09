"""testing the base simulator class"""
import pytest
from mainframe.core import Simulator


def test_simulator():
    """simple setup"""
    simulator = Simulator()

    assert simulator.num_samples == 1000

    with pytest.raises(NotImplementedError):
        simulator.model()
