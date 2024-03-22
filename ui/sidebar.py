# sidebar.py
import streamlit as st


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

    def display(self):

        temperature = st.sidebar.slider(
            "Temperature", min_value=0.0, max_value=1.0, value=0.5, step=0.01
        )
        api_key = st.sidebar.text_input("API Key", "")
        base_url = st.sidebar.text_input("Base URL (Optional)", "")
        model_options = ["gpt-3.5-turbo", "gpt-3.5-turbo-0125"]  # Example model names
        model_name = st.sidebar.selectbox("Model Name", model_options)
