

from src.langgraphagenticai.state.state import state

class BasicChatbotNode:
    def __init__(self, model):
        self.llm=model   # loading the model
        
    # assistant functionality
    def process(self, state:state)->dict:    # return type in the form of dictonary
        """"
        process the input state and generates a chatbot response
        """
        
        return {"messages": self.llm.invoke(state['messages'])}
        