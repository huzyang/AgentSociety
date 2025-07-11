from typing import Any, Awaitable, Callable, List, Optional, Union

from pydantic import BaseModel, Field, field_serializer

from ..environment import MapConfig, SimulatorConfig
from ..llm import LLMConfig
from .agent import AgentConfig, InstitutionAgentClass
from .env import EnvConfig
from .exp import (
    AgentFilterConfig,
    EnvironmentConfig,
    ExpConfig,
    MetricExtractorConfig,
    MetricType,
    WorkflowStepConfig,
    WorkflowType,
)
from .utils import load_config_from_file

__all__ = [
    "EnvConfig",
    "AgentConfig",
    "WorkflowStepConfig",
    "ExpConfig",
    "MetricExtractorConfig",
    "EnvironmentConfig",
    "Config",
    "load_config_from_file",
    "InstitutionAgentClass",
    "MetricType",
    "WorkflowType",
    "AgentFilterConfig",
]


class AgentsConfig(BaseModel):
    """Configuration for different types of agents in the simulation."""

    citizens: list[AgentConfig] = Field(..., min_length=1)
    """Citizen Agent configuration"""

    firms: list[AgentConfig] = Field(default=[])
    """Firm Agent configuration"""

    banks: list[AgentConfig] = Field(default=[])
    """Bank Agent configuration"""

    nbs: list[AgentConfig] = Field(default=[])
    """NBS Agent configuration"""

    governments: list[AgentConfig] = Field(default=[])
    """Government Agent configuration"""

    others: list[AgentConfig] = Field([])
    """Other Agent configuration"""

    supervisor: Optional[AgentConfig] = Field(None)
    """Supervisor Agent configuration"""

    init_funcs: list[Callable[[Any], Union[None, Awaitable[None]]]] = Field([])
    """Initialization functions for simulation, the only one argument is the AgentSociety object"""

    @field_serializer("init_funcs")
    def serialize_init_funcs(self, init_funcs, info):
        return [func.__name__ for func in init_funcs]


class AdvancedConfig(BaseModel):
    """Advanced configuration for the simulation."""

    simulator: SimulatorConfig = Field(
        default_factory=lambda: SimulatorConfig.model_validate({})
    )
    """Simulator configuration"""

    logging_level: str = Field("INFO")
    """Logging level"""


class Config(BaseModel):
    """Configuration for the simulation."""

    llm: List[LLMConfig] = Field(..., min_length=1)
    """List of LLM configurations"""

    env: EnvConfig
    """Environment configuration"""

    map: MapConfig
    """Map configuration"""

    agents: AgentsConfig
    """Configuration for different types of agents in the simulation."""

    exp: ExpConfig
    """Experiment configuration"""

    advanced: AdvancedConfig = Field(
        default_factory=lambda: AdvancedConfig.model_validate({})
    )
    """Advanced configuration for the simulation (keep it empty if you don't need it)"""
