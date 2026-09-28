def get_greeting(name, title="", uppercase=False):
    if title:
        msg = f"Hello, {title} {name}!"
    else:
        msg = f"Hello, {name}!"
    return msg.upper() if uppercase else msg
