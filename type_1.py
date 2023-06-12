import openai

openai.api_key = "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"

print("Hi there, how can I be of service?")
command = input("Ask here... ")

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": command}])
print(completion.choices[0].message.content)