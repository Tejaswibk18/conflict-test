def get_greeting(name, uppercase=False):
    msg = f"Hello, {name}!"
    return msg.upper() if uppercase else msg
