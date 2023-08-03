from collections.abc import Generator

from _typeshed import Incomplete
from vllm.model_executor.parallel_utils.parallel_state import (
    get_tensor_model_parallel_rank as get_tensor_model_parallel_rank,
)

class CudaRNGStatesTracker:
    states_: Incomplete
    seeds_: Incomplete
    def __init__(self) -> None: ...
    def reset(self) -> None: ...
    def get_states(self): ...
    def set_states(self, states) -> None: ...
    def add(self, name, seed) -> None: ...
    def fork(self, name=...) -> Generator[None, None, None]: ...

def get_cuda_rng_tracker(): ...
def model_parallel_cuda_manual_seed(seed) -> None: ...
