def formateed_name(first_name, last_name):
    return f"{first_name.title()} {last_name.title()}"


class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def full_name(self):
        return f"{self.first_name.title()} {self.last_name.title()}"


def greetings(name):
    return f"Hello, {name.title()}!"
