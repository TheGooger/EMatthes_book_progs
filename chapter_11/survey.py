class AnonymousSurvey():
    """Gets anonymous answers."""

    def __init__(self, question):
        """Saves question and gets ready to save answers."""
        self.question = question
        self.responses = []

    def show_question(self):
        """Shows question."""
        print(self.question)

    def store_response(self, new_response):
        """Saves one response."""
        self.responses.append(new_response)

    def show_results(self):
        """Shows results."""
        print("Survey results:")
        for response in self.responses:
            print(" -" + response)



