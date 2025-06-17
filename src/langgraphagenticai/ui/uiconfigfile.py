from configparser import ConfigParser  # helps to read the ".ini" file

class Config:
    def __init__(self, config_file="./src/langgraphagenticai/ui/uiconfigfile.ini"):
        self.config=ConfigParser()
        self.config.read(config_file)
        
    def get_llm_options(self):
        return self.config['default'].get("LLM_OPTIONS").split(", ")
    
    def get_usecase_options(self):
        return self.config['default'].get("USECASES_OPTIONS").split(', ')
    
    def get_groq_model_options(self):
        return self.config['default'].get("GROQ_MODEL_OPTIONS").split(", ")
    
    def get_page_title(self):
        return self.config['default'].get("PAGE_TITLE")