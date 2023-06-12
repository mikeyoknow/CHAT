import openai

openai.api_key = "###"

print("Hi there, how can I be of service?")
command = input("Ask here... ")

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": command}])
print(completion.choices[0].message.content)