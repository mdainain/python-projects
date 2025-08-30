import openai

openai.api_key = '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'


completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "user",
            "content": "what is coding?"
        }
    ]
)

print(completion.choices[0].message['content'])
