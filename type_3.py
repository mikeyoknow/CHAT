import openai
import gradio

openai.api_key = "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"

messages = [{"role": "system", "content" : "You are a chef that knows almost all the recepies. You can be funny too!"}]

def ChefGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    GPT_reply = response["choices"][0]["messages"]["content"]
    messages.append({"role": "assistant", "content": GPT_reply})
    return GPT_reply

demo = gradio.Interface(fn=ChefGPT, inputs="text", outputs="text", title="Real Estate Pro")
demo.launch(share=True)