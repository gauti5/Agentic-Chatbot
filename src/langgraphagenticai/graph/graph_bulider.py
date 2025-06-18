
from src.langgraphagenticai.state.state import state

from langgraph.graph import StateGraph, START, END

class GraphBuilder:
    def __init__(self, model):
        self.llm=model
        self.graph_builder=StateGraph(state)
        
    def basic_chatbot_build_graph(self):
        """
        Builds a basic chatbot build graph using langchain
        This method intializes a chatbot node using the "BasicChatbotNode" class
        and integrates it into the graph. The chatbot node is set as both the entry and 
        exit point of the graph..
        """
        
        self.graph_builder.add_node("chatbot", "")
        self.graph_builder.add_edge(START, "chatbot")
        self.graph_builder.add_edge("chatbot", END)