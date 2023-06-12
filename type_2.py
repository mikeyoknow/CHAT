import openai

openai.api_key = "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"
messages = []

system_msg = input("What type of assistant would you like to have? (describe the bots emotion and character)\n")
messages.append({"role": "system", "content": system_msg})

print("Your new assistant is ready!")
while input != "quit()":
    message = input()
    messages.append({"role": "user", "content": message})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages = messages
    )
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})
    print("\n" + reply + "\n")