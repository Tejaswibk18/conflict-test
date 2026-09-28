def get_greet(name, uppercase=False):
    msg = f"Hello, {name}!"
    return msg.upper() if uppercase else msg
