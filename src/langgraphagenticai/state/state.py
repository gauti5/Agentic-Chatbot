from typing_extensions import TypedDict

from langgraph.graph.message import add_messages
from typing import Annotated

class state(TypedDict):
    """
        represent the structure of the state used in graph
    """
    message: Annotated[list, add_messages]