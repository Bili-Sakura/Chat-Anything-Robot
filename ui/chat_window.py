import streamlit as st
from utils import LLM


class ChatWindow:
    """Represents the main chat window in the application, containing both the chat history and the input box."""

    def __init__(self):

        self.llm_chat_window = LLMChatWindow()

    def display(self):
        """Displays the chat window, including the chat history and the input box."""

        # Display LLM chat history
        self.llm_chat_window.display()

        # Display user input box directly in this method
        self.display_user_input_box()

    def display_user_input_box(self):
        """Displays the user input box. Submission is handled by pressing Enter."""
        user_input_key = "user_input_key"  # Unique key for session

        # Display user input box that submits on Enter press
        user_input = st.text_input(
            label="Type your message here...",
            key=user_input_key,
            on_change=self.handle_input,
            args=(user_input_key,),
            label_visibility="hidden",
        )

    def handle_input(self, user_input_key):
        """Handles user input submission."""
        user_input = st.session_state[user_input_key]
        if user_input:
            # Handle user input using LLMChatWindow
            self.llm_chat_window.handle_send(user_input)
            # Reset input box for the next message
            st.session_state[user_input_key] = ""


class LLMChatWindow:
    def __init__(self):
        self.chat_history = []
        if "conversation" not in st.session_state:
            st.session_state.conversation = [
                ("User", "Hello!"),
                ("Model", "Hi there! How can I assist you?"),
            ]

        self.llm = LLM()

    def display(self):
        """Display the chat history."""

        chat_container = st.empty()
        chat_messages = "".join(
            [
                f"<div style='float: {'left' if role != 'User' else 'right'}; color: {'black' if role != 'User' else 'white'}; background-color: {'#E0E0E0' if role != 'User' else '#4C8BF5'}; padding: 10px; border-radius: 10px; margin: 10px 0; word-wrap: break-word; font-size: 16px; max-width: 70%; clear: both;'>{message}</div>"
                for role, message in st.session_state.conversation
            ]
        )
        chat_container_html = f"<div style='height: 300px; overflow-y: auto; border: 1px solid #ccc; border-radius: 5px; padding: 10px;'>{chat_messages}</div>"
        chat_container.markdown(chat_container_html, unsafe_allow_html=True)

    def handle_send(self, user_input):
        """
        Generates the response based on the user input message.

        Retrieves the user input message from the session state.
        Appends the user message to the conversation history.
        Simulates a model reply and appends it to the conversation history.
        Resets the text input field based on the current state.
        """

        if user_input:
            st.session_state.conversation.append(("User", user_input))

            model_reply = self.llm.get_answer(user_input)

            st.session_state.conversation.append(("Model", model_reply))
