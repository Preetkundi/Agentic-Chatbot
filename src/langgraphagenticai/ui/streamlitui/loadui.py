import streamlit as st
import os


from src.langgraphagenticai.ui.uiconfigfile import Congfig

class LoadStreamlitUI:
     def __init__(self):
          self.config=Congfig()
          self.user_controls={}
        
     def load_streamlit_ui(self):
          st.set_page_config(page_title="🤖 " + self.config.get_page_title(), layout="wide")
          st.header("🤖 " + self.config.get_page_title())

          with st.sidebar:
               #get options from config
               llm_options=self.config.get_llms_options()
               usecase_options=self.config.get_usecase_options()

               ## LLM selection
               self.user_controls["selected_llm"]= st.selectbox("Select LLM",llm_options)

               if self.user_controls["selected_llm"]=='Groq':
                    #Model selection
                    model_options=self.config.get_groq_model_options()
                    self.user_controls["selected_groq_model"]=st.selectbox("Select Model", model_options)
                    self.user_controls["GROQ_API_KEY"]=st.session_state["GROQ_API_KEY"]=st.text_input("API KEY",type="password")

                    if not self.user_controls["GROQ_API_KEY"]:
                         st.warning("PLEASE ENTER YOUR GROQ API KEY TO PROCEED. DON'T HAVE? REFER: https://console.groq.com/keys ")
                    
                
                ## USE CASE SELECTION
               self.user_controls["selected_usecase"]=st.selectbox("Select Usecase",usecase_options)    
            
          return self.user_controls
     
    