import streamlit as st
from utils import LLM


class ChatWindow:
    def __init__(self):
        self.chat_history = []
        self.llm = None  # Initialize llm as None initially

        if "conversation" not in st.session_state:
            st.session_state.conversation = [
                ("User", "Hello!"),
                ("Model", "Hi there! How can I assist you?"),
            ]

    def display(self):
        if st.session_state.get("INIT_LLM"):
            self.update_llm_instance()
            # st.session_state["INIT_LLM"] = False  # Reset the flag

        self.display_chat_window()
        self.display_user_input_box()

    def display_chat_window(self):
        chat_container = st.empty()
        chat_messages = "".join(
            [
                f"<div style='float: {'left' if role != 'User' else 'right'}; color: {'black' if role != 'User' else 'white'}; background-color: {'#E0E0E0' if role != 'User' else '#4C8BF5'}; padding: 10px; border-radius: 10px; margin: 10px 0; word-wrap: break-word; font-size: 16px; max-width: 70%; clear: both;'>{message}</div>"
                for role, message in st.session_state.conversation
            ]
        )
        chat_container_html = f"<div style='height: 500px; overflow-y: auto; border: 1px solid #ccc; border-radius: 5px; padding: 10px;'>{chat_messages}</div>"
        chat_container.markdown(chat_container_html, unsafe_allow_html=True)

    def handle_input(self, user_input_key):
        user_input = st.session_state[user_input_key]
        if user_input and self.llm:
            self.handle_send(user_input)
        st.session_state[user_input_key] = ""

    def display_user_input_box(self):
        user_input_key = "user_input_key"
        user_input = st.text_input(
            label="Type your message here...",
            key=user_input_key,
            on_change=self.handle_input,
            args=(user_input_key,),
            label_visibility="hidden",
            disabled=not self.llm,  # Disable input if llm is not configured properly
        )

    def handle_send(self, user_input):
        if user_input:
            st.session_state.conversation.append(("User", user_input))
            if self.llm:
                model_reply = self.llm.get_answer(user_input)
                st.session_state.conversation.append(("Model", model_reply))

    def update_llm_instance(self):

        self.llm = LLM(
            api_key=st.session_state["GLOBAL_API_KEY"],
            base_url=st.session_state["GLOBAL_BASE_URL"],
            base_model=st.session_state["GLOBAL_MODEL_NAME"],
            temperature=st.session_state["GLOBAL_TEMPERATURE"],
        )
