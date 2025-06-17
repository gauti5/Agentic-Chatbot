import streamlit as st 
import os, sys

from src.langgraphagenticai.ui.uiconfigfile import Config


class LoadStreamlitUI:
    def __init__(self):
        self.config=Config()
        self.user_controls={}
        
    def load_streamlit_ui(self):
        st.set_page_config(page_title="👽  " + self.config.get_page_title(), layout="wide")
        st.header("👽  " + self.config.get_page_title())
        
        with st.sidebar:
            # get options from config
            llm_options=self.config.get_llm_options()
            usecase_options=self.config.get_usecase_options()
            
            # LLM Selection
            self.user_controls['selected_llm']=st.selectbox("select LLM", llm_options)
            
            if self.user_controls['selected_llm']=='groq':
                # Model Selection
                
                model_options=self.config.get_groq_model_options()
                self.user_controls['selected_groq_model']=st.selectbox("select model", model_options)
                self.user_controls['GROQ_API_KEY']=st.session_state['GROQ_API_KEY']=st.text_input("API Key", type="password")
                
                # Validate API Key
                
                if not self.user_controls['GROQ_API_KEY']:
                    st.warning("Please enter your groq api key to proceed. Dont have? please refer : https://console.groq.com/keys")
            
            # use case selection
            
            self.user_controls['selected_usecase']=st.selectbox("select usecases", usecase_options)
            
        return self.user_controls