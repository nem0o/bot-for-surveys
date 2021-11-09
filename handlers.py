import re


def handler_hello_logic(text, state, context):
    if re.match(r'да', text, re.IGNORECASE):
        context[state] = 'confirm=true'
        return True
    elif re.match(r'нет', text, re.IGNORECASE):
        context[state] = 'confirm=false'
        return True
    elif re.match(r'Еще раз', text, re.IGNORECASE):
        context[state] = 'repeat=true'
        return True
    elif re.match(r'Занят', text, re.IGNORECASE):
        context[state] = 'wrong_time=true'
        return True
    elif re.match(r'\r?\n', text, re.IGNORECASE):
        context[state] = 'NULL'
        return True
    else:
        context[state] = 'DEFAULT'
        return True

def handler_main_logic(text, state, context):
    if re.match(r'[0-8]', text):
        context[state] = 'recommendation_score=[0…8]'
        return True
    elif re.match(r'[9]*$', text):
        context[state] = 'recommendation_score=[9…10]'
        return True
    elif re.match(r'да', text, re.IGNORECASE):
        context[state] = 'recommendation=positive'
        return True
    elif re.match(r'нет', text, re.IGNORECASE):
        context[state] = 'recommendation=negative'
        return True
    elif re.match(r'возможно', text, re.IGNORECASE):
        context[state] = 'recommendation=neutral'
        return True
    elif re.match(r'Не знаю', text, re.IGNORECASE):
        context[state] = 'recommendation=dont_know'
        return True
    elif re.match(r'Еще раз', text, re.IGNORECASE):
        context[state] = 'repeat=true'
        return True
    elif re.match(r'Вопрос', text, re.IGNORECASE):
        context[state] = 'question=true'
        return True
    elif re.match(r'Занят', text, re.IGNORECASE):
        context[state] = 'wrong_time=true'
        return True
    elif re.match(r'\r?\n', text, re.IGNORECASE):
        context[state] = 'NULL'
        return True
    else:
        context[state] = 'DEFAULT'
        return True