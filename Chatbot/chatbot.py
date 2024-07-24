from responses import get_response

class Chatbot:
    def __init__(self):
        self.bot_name = "HealthBot"

    def respond_to_user(self, user_input):
        response = get_response(user_input)
        return response
