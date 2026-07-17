
class ConversationService:
    def __init__(self) -> None:
        self.conversations = {}

    def add_message(self, phone, role, content):
        if phone not in self.conversations:
            self.conversations[phone] = []

        self.conversations[phone].append(
            {
                "role": role,
                "content": content
            }
        )

    def get_message(self, phone):
        return self.conversations.get(phone, [])
