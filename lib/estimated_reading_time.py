import math
def estimated_reading_time(text):
    if text == None:
        raise Exception("Please enter a string")
    elif text == 123:
        raise Exception("Please enter a string")
    
    word_count = len(text)
    minutes = round(word_count / 200)
    return f'This text should take {minutes} minutes to read'