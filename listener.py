from events import subscribe

def handle_user_registered_event(user):
    print(f"Wow, a new user has registerd: {user}")

def setup_event_handler():
    subscribe("user_registered", handle_user_registered_event)