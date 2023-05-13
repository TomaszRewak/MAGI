import openai

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You answer questions with a simple 'yes' or 'no'."},
        {"role": "user", "content": "Can the following question be generally answered with a 'yes' or 'no'? \n Is C# better than Java?"},
    ]
)

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

print(response)
