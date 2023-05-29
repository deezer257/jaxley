from abc import ABC, abstractmethod
from typing import Dict, Optional, Tuple

import jax.numpy as jnp


class Synapse:
    synapse_params = None
    synapse_states = None

    def __init__(self):
        super().__init__()

    def set_params(self, key, val):
        self.params[key][:] = val

    @abstractmethod
    def step(
        self, u, dt, voltages, params
    ) -> Tuple[jnp.ndarray, Tuple[jnp.ndarray, jnp.ndarray]]:
        pass