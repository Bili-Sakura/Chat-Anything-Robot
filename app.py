from ui.sidebar import SidebarManager
from ui.chat_window import ChatWindow


def main():
    """
    This function represents the main logic of the application.
    Use the active session to determine which ChatWindow to display.
    """

    sidebar_manager = SidebarManager()
    chat_window = ChatWindow()

    # 侧边栏布局和逻辑
    sidebar_manager.display()
    # 主聊天窗口布局和逻辑
    chat_window.display()


if __name__ == "__main__":
    main()
