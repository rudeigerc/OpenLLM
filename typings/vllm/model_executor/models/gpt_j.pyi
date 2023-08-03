from typing import Dict
from typing import List
from typing import Optional

import torch
from _typeshed import Incomplete
from torch import nn
from transformers import GPTJConfig as GPTJConfig
from vllm.model_executor.input_metadata import InputMetadata as InputMetadata
from vllm.model_executor.layers.activation import get_act_fn as get_act_fn
from vllm.model_executor.layers.attention import PagedAttentionWithRoPE as PagedAttentionWithRoPE
from vllm.model_executor.layers.sampler import Sampler as Sampler
from vllm.model_executor.parallel_utils.parallel_state import (
    get_tensor_model_parallel_rank as get_tensor_model_parallel_rank,
)
from vllm.model_executor.parallel_utils.parallel_state import (
    get_tensor_model_parallel_world_size as get_tensor_model_parallel_world_size,
)
from vllm.model_executor.parallel_utils.tensor_parallel import ColumnParallelLinear as ColumnParallelLinear
from vllm.model_executor.parallel_utils.tensor_parallel import RowParallelLinear as RowParallelLinear
from vllm.model_executor.parallel_utils.tensor_parallel import VocabParallelEmbedding as VocabParallelEmbedding
from vllm.model_executor.weight_utils import hf_model_weights_iterator as hf_model_weights_iterator
from vllm.model_executor.weight_utils import load_tensor_parallel_weights as load_tensor_parallel_weights
from vllm.sequence import SequenceOutputs as SequenceOutputs

KVCache: Incomplete

class GPTJAttention(nn.Module):
    total_num_heads: Incomplete
    hidden_size: Incomplete
    head_size: Incomplete
    qkv_proj: Incomplete
    out_proj: Incomplete
    num_heads: Incomplete
    attn: Incomplete
    warmup: bool
    def __init__(self, config: GPTJConfig) -> None: ...
    def forward(self, position_ids: torch.Tensor, hidden_states: torch.Tensor, kv_cache: KVCache, input_metadata: InputMetadata, cache_event: Optional[torch.cuda.Event]) -> torch.Tensor: ...

class GPTJMLP(nn.Module):
    fc_in: Incomplete
    fc_out: Incomplete
    act: Incomplete
    def __init__(self, intermediate_size: int, config: GPTJConfig) -> None: ...
    def forward(self, hidden_states: torch.Tensor) -> torch.Tensor: ...

class GPTJBlock(nn.Module):
    ln_1: Incomplete
    attn: Incomplete
    mlp: Incomplete
    def __init__(self, config: GPTJConfig) -> None: ...
    def forward(self, position_ids: torch.Tensor, hidden_states: torch.Tensor, kv_cache: KVCache, input_metadata: InputMetadata, cache_event: Optional[torch.cuda.Event]) -> torch.Tensor: ...

class GPTJModel(nn.Module):
    config: Incomplete
    embed_dim: Incomplete
    wte: Incomplete
    h: Incomplete
    ln_f: Incomplete
    def __init__(self, config: GPTJConfig) -> None: ...
    def forward(self, input_ids: torch.Tensor, position_ids: torch.Tensor, kv_caches: List[KVCache], input_metadata: InputMetadata, cache_events: Optional[List[torch.cuda.Event]]) -> torch.Tensor: ...

class GPTJForCausalLM(nn.Module):
    config: Incomplete
    transformer: Incomplete
    lm_head: Incomplete
    sampler: Incomplete
    def __init__(self, config: GPTJConfig) -> None: ...
    def forward(self, input_ids: torch.Tensor, positions: torch.Tensor, kv_caches: List[KVCache], input_metadata: InputMetadata, cache_events: Optional[List[torch.cuda.Event]]) -> Dict[int, SequenceOutputs]: ...
    def load_weights(self, model_name_or_path: str, cache_dir: Optional[str] = ..., use_np_cache: bool = ...): ...
