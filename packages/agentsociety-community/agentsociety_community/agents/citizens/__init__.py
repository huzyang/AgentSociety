"""
Lazy import like langchain-community.

How to add a new citizen:
1. Add a new file in the directory to define your citizen class.
2. add a _import_xxx function to import the citizen class.
3. add a __getattr__ function to lazy import the citizen class.
4. add the citizen class to __all__ variable.
5. add the citizen class to the return value of get_type_to_cls_dict function.
"""

from typing import TYPE_CHECKING, Callable, Dict, Type

from agentsociety.agent import CitizenAgentBase

if TYPE_CHECKING:
    from .bdsc2025_track_one_envambassador.baseline import BaselineEnvAmbassador
    from .bdsc2025_track_one_envcitizen.track_one_envcitizen import TrackOneEnvCitizen
    from .bdsc2025_track_two_envcitizen.track_two_envcitizen import TrackTwoEnvCitizen
    from .bdsc2025_track_two_rumor_spreader.rumor_spreader import RumorSpreader
    from .cityagent import SocietyAgent
    from .polarization import AgreeAgent, DisagreeAgent


def _import_track_one_env_citizen() -> Type[CitizenAgentBase]:
    from .bdsc2025_track_one_envcitizen.track_one_envcitizen import TrackOneEnvCitizen

    return TrackOneEnvCitizen


def _import_track_one_env_ambassador() -> Type[CitizenAgentBase]:
    from .bdsc2025_track_one_envambassador.baseline import BaselineEnvAmbassador

    return BaselineEnvAmbassador


def _import_track_two_env_citizen() -> Type[CitizenAgentBase]:
    from .bdsc2025_track_two_envcitizen.track_two_envcitizen import TrackTwoEnvCitizen

    return TrackTwoEnvCitizen


def _import_rumor_spreader() -> Type[CitizenAgentBase]:
    from .bdsc2025_track_two_rumor_spreader.rumor_spreader import RumorSpreader

    return RumorSpreader


def _import_polarization_agree_agent() -> Type[CitizenAgentBase]:
    from .polarization import AgreeAgent

    return AgreeAgent


def _import_polarization_disagree_agent() -> Type[CitizenAgentBase]:
    from .polarization import DisagreeAgent

    return DisagreeAgent


def _import_society_agent() -> Type[CitizenAgentBase]:
    from .cityagent import SocietyAgent

    return SocietyAgent


def __getattr__(name: str) -> Type[CitizenAgentBase]:
    if name == "TrackOneEnvCitizen":
        return _import_track_one_env_citizen()
    if name == "TrackOneEnvAmbassador":
        return _import_track_one_env_ambassador()
    if name == "TrackTwoEnvCitizen":
        return _import_track_two_env_citizen()
    if name == "RumorSpreader":
        return _import_rumor_spreader()
    if name == "SocietyAgent":
        return _import_society_agent()
    if name == "AgreeAgent":
        return _import_polarization_agree_agent()
    if name == "DisagreeAgent":
        return _import_polarization_disagree_agent()
    raise AttributeError(f"module {__name__} has no attribute {name}")


__all__ = [
    "TrackOneEnvCitizen",
    "TrackOneEnvAmbassador",
    "TrackTwoEnvCitizen",
    "RumorSpreader",
    "SocietyAgent",
    "AgreeAgent",
    "DisagreeAgent",
]


def get_type_to_cls_dict() -> Dict[str, Callable[[], Type[CitizenAgentBase]]]:
    """
    Use this function to get all the citizen classes.
    """
    return {
        "TrackOneEnvCitizen": _import_track_one_env_citizen,
        "TrackOneEnvAmbassador": _import_track_one_env_ambassador,
        "TrackTwoEnvCitizen": _import_track_two_env_citizen,
        "RumorSpreader": _import_rumor_spreader,
        "AgreeAgent": _import_polarization_agree_agent,
        "DisagreeAgent": _import_polarization_disagree_agent,
        "SocietyAgent": _import_society_agent,
    }
