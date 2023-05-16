import openai

questions = [
    'Is love more important than science?',
    'Should one follow emotions instead of reason?',
    'Is 3 > 2?',
    'How are you?',
    'Is Robert in today?',
    'Can you describe Robert for me?',
    'What is most important in life?',
]

for question in questions:
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

    print(response['choices'][0]['message']['content'])

# {
#   "choices": [
#     {
#       "finish_reason": "stop",
#       "index": 0,
#       "message": {
#         "content": "Yes.",
#         "role": "assistant"
#       }
#     }
#   ],
#   "created": 1684003959,
#   "id": "chatcmpl-7Foe7sKt2SqEWcjmI5VG9Jc5ndRrd",
#   "model": "gpt-3.5-turbo-0301",
#   "object": "chat.completion",
#   "usage": {
#     "completion_tokens": 2,
#     "prompt_tokens": 50,
#     "total_tokens": 52
#   }
# }
