import openai
import re


def is_yes_or_no_question(question: str, key: str):
    openai.api_key = key
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[
            {'role': 'system', 'content': 'You answer questions with a simple "yes" or "no".'},
            {'role': 'user', 'content': f'Can the following question be generally answered with a "yes" or "no"? \n {question}'},
        ]
    )

    content = response['choices'][0]['message']['content']

    if re.match('^\W*yes\W*$', content, re.IGNORECASE):
        return True

    if re.match('^\W*no\W*$', content, re.IGNORECASE):
        return False

    raise Exception(f'Invalid question annotation response: {content}')


def get_answer(question: str, personality: str, key: str):
    openai.api_key = key
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[
            {'role': 'system', 'content': personality},
            {'role': 'system', 'content': 'Your answers are rather concise.'},
            {'role': 'user', 'content': question},
        ]
    )

    return response['choices'][0]['text']


def classify_answer(question: str, personality: str, answer: str, key: str):
    openai.api_key = key
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[
            {'role': 'system', 'content': personality},
            {'role': 'system', 'content': 'Your answers are rather concise.'},
            {'role': 'user', 'content': question},
            {'role': 'system', 'content': answer},
            {'role': 'user', 'content': 'Summarize you answer with a simple "yes" or "no" (answering with a single word). If (and only if) that\'s not possible, instead of answering with "yes" or "no", list conditions under which the answer would be "yes".'},
        ]
    )

    content = response['choices'][0]['message']['content']

    if re.match('^\W*yes\W*$', content, re.IGNORECASE):
        return {'classification': True, 'conditions': None}

    if re.match('^\W*no\W*$', content, re.IGNORECASE):
        return {'classification': False, 'conditions': None}

    return {'classification': True, 'conditions': content}
