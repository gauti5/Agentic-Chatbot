import streamlit as st
from src.langgraphagenticai.ui.uiconfigfile import Config


class LoadStreamlitUI:
    def __init__(self):
        self.config = Config()

    def load_streamlit_ui(self):
        st.set_page_config(page_title="👽  " + self.config.get_page_title(), layout="wide")
        st.header("👽  " + self.config.get_page_title())

        with st.sidebar:
            llm_options = self.config.get_llm_options()
            usecase_options = self.config.get_usecase_options()

            selected_llm = st.selectbox("Select LLM", llm_options, key="selected_llm")
            selected_usecase = st.selectbox("Select Usecase", usecase_options, key="selected_usecase")

            user_controls = {
                "selected_llm": selected_llm,
                "selected_usecase": selected_usecase
            }

            if selected_llm == "groq":
                model_options = self.config.get_groq_model_options()
                selected_model = st.selectbox("Select Groq Model", model_options, key="selected_groq_model")
                api_key = st.text_input("GROQ API Key", type="password", key="groq_api_key")

                user_controls["selected_groq_model"] = selected_model
                user_controls["GROQ_API_KEY"] = api_key

                if not api_key:
                    st.warning("Please enter your GROQ API key. Get one at https://console.groq.com/keys")

            return user_controls