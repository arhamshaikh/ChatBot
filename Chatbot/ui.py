from tkinter import *
from chatbot import Chatbot

BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"

FONT = "Helvetica 14"
font_bold = "Helvetica 13 bold"

class ChatApplication:
    def __init__(self):
        self.window = Tk()
        self.chatbot = Chatbot()
        self.is_fullscreen = False  # Track full-screen mode
        self._setup_main_window()

    def run(self):
        self.window.mainloop()

    def _setup_main_window(self):
        self.window.title("Healthcare Chatbot")
        self.window.geometry("470x550")  # Set the initial size
        self.window.configure(bg=BG_COLOR)

        # Create a custom header frame
        header_frame = Frame(self.window, bg=BG_COLOR)
        header_frame.pack(fill=X)

        # Add minimize and close buttons to the header frame


        

        head_label = Label(self.window, bg=BG_COLOR, fg=TEXT_COLOR,
                           text="Welcome to the Healthcare Chatbot", font=font_bold, pady=10)
        head_label.pack(fill=X)

        line = Label(self.window, width=450, bg=BG_GRAY)
        line.pack(fill=X)

        self.text_widget = Text(self.window, width=20, height=2, bg=BG_COLOR, fg=TEXT_COLOR,
                                font=FONT, padx=5, pady=5)
        self.text_widget.pack(fill=BOTH, expand=True)

        scrollbar = Scrollbar(self.text_widget)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.text_widget.configure(yscrollcommand=scrollbar.set)
        scrollbar.configure(command=self.text_widget.yview)

        bottom_label = Label(self.window, bg=BG_GRAY, height=2)
        bottom_label.pack(fill=X)

        self.msg_entry = Entry(bottom_label, bg="#2C3E50", fg=TEXT_COLOR, font=FONT)
        self.msg_entry.pack(side=LEFT, fill=X, padx=10, pady=5, expand=True)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self._on_enter_pressed)

        send_button = Button(bottom_label, text="Send", font=font_bold, bg=BG_GRAY,
                             command=lambda: self._on_enter_pressed(None))
        send_button.pack(side=LEFT, padx=5, pady=5)

    def _on_enter_pressed(self, event):
        user_input = self.msg_entry.get()
        if user_input:
            self._insert_message(user_input, "You")
            bot_response = self.chatbot.respond_to_user(user_input)
            self._insert_message(bot_response, self.chatbot.bot_name)
        self.msg_entry.delete(0, END)

    def _insert_message(self, msg, sender):
        if not msg:
            return
        msg1 = f"{sender}: {msg}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg1)
        self.text_widget.configure(state=DISABLED)
        self.text_widget.see(END)

    def _minimize_window(self):
        self.window.iconify()  # Minimize the window

if __name__ == "__main__":
    app = ChatApplication()
    app.run()
