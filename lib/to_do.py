def to_do(text):
    if text == '':
        raise Exception("No string was given")
    elif text == None:
        raise Exception("Invalid value")
    elif '#TODO' in text:
        return True
    else:
        return False