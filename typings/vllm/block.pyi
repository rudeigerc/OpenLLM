from typing import List

from _typeshed import Incomplete
from vllm.utils import Device as Device

class LogicalTokenBlock:
    block_number: Incomplete
    block_size: Incomplete
    token_ids: Incomplete
    num_tokens: int
    def __init__(self, block_number: int, block_size: int) -> None: ...
    def is_empty(self) -> bool: ...
    def get_num_empty_slots(self) -> int: ...
    def is_full(self) -> bool: ...
    def append_tokens(self, token_ids: List[int]) -> None: ...
    def get_token_ids(self) -> List[int]: ...
    def get_last_token_id(self) -> int: ...

class PhysicalTokenBlock:
    device: Incomplete
    block_number: Incomplete
    block_size: Incomplete
    ref_count: int
    def __init__(self, device: Device, block_number: int, block_size: int) -> None: ...
