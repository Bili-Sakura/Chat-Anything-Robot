# sidebar.py
import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv(override=True)


class SidebarManager:
    def __init__(self):

        self.info_display = InfoDisplay()
        self.llm_config_manager = LLMConfigManager()

    def display(self):
        # Info Section
        st.sidebar.title("Chat Anything Robot")

        # LLM Configs Section
        if st.sidebar.button("⚙️ LLM Configs"):
            st.session_state["show_llm_configs"] = not st.session_state.get(
                "show_llm_configs", True
            )
        if st.session_state.get("show_llm_configs", True):
            self.llm_config_manager.display()
        st.sidebar.markdown("---")


class InfoDisplay:
    def __init__(self):
        pass

    def display(self):
        pass


class LLMConfigManager:
    def __init__(self):
        pass
        # st.session_state.GLOBAL_TEMPERATURE = 0.5
        # st.session_state.GLOBAL_API_KEY = ""
        # st.session_state.GLOBAL_BASE_URL = ""
        # st.session_state.GLOBAL_MODEL_NAME = "gpt-3.5-turbo"
        # st.session_state.INIT_LLM = False

    def display(self):

        st.sidebar.slider(
            "Temperature",
            min_value=0.0,
            max_value=1.0,
            value=0.5,
            step=0.01,
            key="GLOBAL_TEMPERATURE",
            on_change=self.handle_llm_config_change,
        )
        st.sidebar.text_input(
            "API Key",
            value=os.getenv("OPENAI_API_KEY") or "",
            key="GLOBAL_API_KEY",
            on_change=self.handle_llm_config_change,
            type="password",
        )
        st.sidebar.text_input(
            "Base URL (Optional)",
            key="GLOBAL_BASE_URL",
            on_change=self.handle_llm_config_change,
        )
        model_options = ["gpt-3.5-turbo", "gpt-3.5-turbo-0125"]
        st.sidebar.selectbox(
            "Model Name",
            model_options,
            key="GLOBAL_MODEL_NAME",
            on_change=self.handle_llm_config_change,
        )

    def handle_llm_config_change(self):
        st.session_state["INIT_LLM"] = True
