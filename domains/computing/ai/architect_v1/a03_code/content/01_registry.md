# Theory Atom: Registry & Implementations

In this atom, you will explore how **EvolveLab** centralizes diverse memory architectures under a unified `BaseMemoryProvider` abstract base class (ABC).

## The Memory Provider Interface (Listing 1)
Every memory system in EvolveLab must conform to the following protocol:

```python
class BaseMemoryProvider(ABC):
    @abstractmethod
    def provide_memory(self, request: MemoryRequest) -> MemoryResponse:
        """Handles context-aware retrieval (The 'Recall' Layer)."""
        pass

    @abstractmethod
    def take_in_memory(self, trajectory_data: TrajectoryData) -> tuple[bool, str]:
        """Handles ingestion and extraction (The 'Perception' Layer)."""
        pass
```

## The "Universal Language": Data Carriers
Interfaces are only effective if they move standardized data. EvolveLab uses:
- **TrajectoryData**: A comprehensive container for task execution history (query, traces, rewards).
- **MemoryItem**: The fundamental unit (Text, Insight, or executable API).
- **MemoryRequest/Response**: Standardized envelopes for retrieval queries.

## The Registry
Navigation: `/Users/Shared/Projects/IntelHub/EvolveLab/providers/`
All 12+ memory systems (Voyager, ExpeL, SkillWeaver, etc.) are registered in `memory_types.py`. 

## The CLI Entry Point
While the core logic lives in `IntelHub`, the primary command-line tool is located in the companion research directory:
- **CLI Path**: `/Users/Shared/AI_CORE/MemEvolve/Flash-Searcher-main/evolve_cli.py`

This separation ensures that the **School** (`IntelHub`) remains a clean, modular environment while the **Evolution Lab** (`AI_CORE`) provides the execution harness.

## Verification Check
Navigate to `IntelHub/EvolveLab/providers/`. Locate `skill_weaver_provider.py`. How does its `take_in_memory` implementation differ from a simple textual memory (like `dilu`)?
