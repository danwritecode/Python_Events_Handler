from events import post_event, subscribe
from crud import create_user
from listener import setup_event_handler

# Initialize the event handler
setup_event_handler()


def register_new_user(name: str, password: str, email: str):
    """Function creates a new user"""
    user = create_user(name, password, email)
    post_event("user_registered", user)


register_new_user("John Doe", "SuperSecretPassword", "jdoe@email.com")



