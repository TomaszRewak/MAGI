import openai
import re


def is_yes_or_no_question(question: str, key: str):
    openai.api_key = key
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        logit_bias={
            9642: 100,  # Yes
            2822: 90  # No
        },
        max_tokens=1,
        messages=[
            {'role': 'system', 'content': 'You answer questions with a simple "yes" or "no".'},
            {'role': 'user', 'content': f'Is the following question a boolean question? \n {question}'},
        ]
    )

    content = response['choices'][0]['message']['content']

    if content == 'Yes':
        return True

    if content == 'No':
        return False

    raise Exception(f'Invalid question annotation response: {content}')


def get_answer(question: str, personality: str, key: str):
    openai.api_key = key
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[
            {'role': 'system', 'content': f'{personality} Your answers are rather concise.'},
            {'role': 'user', 'content': question},
        ]
    )

    return response['choices'][0]['message']['content']


def classify_answer(question: str, personality: str, answer: str, key: str):
    openai.api_key = key
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[
            {'role': 'system', 'content': f'{personality} Your answers are rather concise.'},
            {'role': 'user', 'content': question},
            {'role': 'system', 'content': answer},
            {'role': 'user', 'content': 'Summarize you answer with a simple "yes" or "no" (answering with a single word). If (and only if) that\'s not possible, instead of answering with "yes" or "no", list conditions under which the answer would be "yes".'},
        ]
    )

    content = response['choices'][0]['message']['content']

    if re.match('^\W*yes\W*$', content, re.IGNORECASE):
        return {'status': 'yes', 'conditions': None}

    if re.match('^\W*no\W*$', content, re.IGNORECASE):
        return {'status': 'no', 'conditions': None}

    return {'status': 'conditional', 'conditions': content}
