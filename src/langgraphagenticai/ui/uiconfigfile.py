from configparser import ConfigParser

class Congfig:
    def __init__(self,conif_file="./src/langgraphagenticai/ui/uiconfigfile.ini"):
        self.config=ConfigParser()
        self.config.read(conif_file)
    
    def get_llms_options(self):
        return self.config["DEFAULT"].get("LLM_OPTIONS").split(", ")
    
    def get_usecase_options(self):
        return self.config["DEFAULT"].get("USECASE_OPTIONS").split(", ")
    
    def get_groq_model_options(self):
        return self.config["DEFAULT"].get("GROQ_MODEL_OPTIONS").split(", ")
    
    def get_page_title(self):
        return self.config["DEFAULT"].get("PAGE_TITLE")
    
    
