import openai

openai.api_key = "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"

print("Hi there, how can I be of service?")
command = input("Ask here... ")

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": command}])
print(completion.choices[0].message.content)