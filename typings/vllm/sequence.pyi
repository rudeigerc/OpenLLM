import enum
from typing import Dict
from typing import List
from typing import Optional
from typing import Union

from _typeshed import Incomplete
from vllm.block import LogicalTokenBlock as LogicalTokenBlock
from vllm.sampling_params import SamplingParams as SamplingParams

class SequenceStatus(enum.Enum):
    WAITING: Incomplete
    RUNNING: Incomplete
    SWAPPED: Incomplete
    FINISHED_STOPPED: Incomplete
    FINISHED_LENGTH_CAPPED: Incomplete
    FINISHED_ABORTED: Incomplete
    FINISHED_IGNORED: Incomplete
    @staticmethod
    def is_finished(status: SequenceStatus) -> bool: ...
    @staticmethod
    def get_finished_reason(status: SequenceStatus) -> Union[str, None]: ...

class SequenceData:
    prompt_token_ids: Incomplete
    output_token_ids: Incomplete
    cumulative_logprob: float
    def __init__(self, prompt_token_ids: List[int]) -> None: ...
    def append_token_id(self, token_id: int, logprob: float) -> None: ...
    def get_len(self) -> int: ...
    def get_output_len(self) -> int: ...
    def get_token_ids(self) -> List[int]: ...
    def get_last_token_id(self) -> int: ...

class Sequence:
    seq_id: Incomplete
    prompt: Incomplete
    block_size: Incomplete
    data: Incomplete
    output_logprobs: Incomplete
    output_tokens: Incomplete
    output_text: str
    logical_token_blocks: Incomplete
    status: Incomplete
    def __init__(self, seq_id: int, prompt: str, prompt_token_ids: List[int], block_size: int) -> None: ...
    def append_token_id(self, token_id: int, logprobs: Dict[int, float]) -> None: ...
    def get_len(self) -> int: ...
    def get_output_len(self) -> int: ...
    def get_token_ids(self) -> List[int]: ...
    def get_last_token_id(self) -> int: ...
    def get_output_token_ids(self) -> List[int]: ...
    def get_cumulative_logprob(self) -> float: ...
    def is_finished(self) -> bool: ...
    def fork(self, child_seq: Sequence) -> None: ...

class SequenceGroup:
    request_id: Incomplete
    seqs: Incomplete
    sampling_params: Incomplete
    arrival_time: Incomplete
    def __init__(self, request_id: str, seqs: List[Sequence], sampling_params: SamplingParams, arrival_time: float) -> None: ...
    def get_seqs(self, status: Optional[SequenceStatus] = ...) -> List[Sequence]: ...
    def num_seqs(self, status: Optional[SequenceStatus] = ...) -> int: ...
    def find(self, seq_id: int) -> Sequence: ...
    def is_finished(self) -> bool: ...

class SequenceGroupMetadata:
    request_id: Incomplete
    is_prompt: Incomplete
    seq_data: Incomplete
    sampling_params: Incomplete
    block_tables: Incomplete
    def __init__(self, request_id: str, is_prompt: bool, seq_data: Dict[int, SequenceData], sampling_params: SamplingParams, block_tables: Dict[int, List[int]]) -> None: ...

class SequenceOutputs:
    seq_id: Incomplete
    parent_seq_id: Incomplete
    output_token: Incomplete
    logprobs: Incomplete
    def __init__(self, seq_id: int, parent_seq_id: int, output_token: int, logprobs: Dict[int, float]) -> None: ...
    def __eq__(self, other: object) -> bool: ...
