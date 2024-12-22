#mistral 7B
from huggingface_hub import InferenceClient
import random
import time
import requests

API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.1"
headers = {"Authorization": "Bearer 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"}

def format_prompt(message, custom_instructions = None, chat_history=None):
    prompt = ""
    if custom_instructions:
        prompt += f"[INST] {custom_instructions} [/INST]"

    if chat_history:
        prompt += "\n".join(chat_history) + "\n"

    prompt += f"[INST] {message} [/INST]"
    return prompt

def generate(prompt, chat_history=None, temperature=0.9, max_new_tokens=8192, top_p=0.95, repetition_penalty=1.0):
    temperature = float(temperature)
    if temperature < 1e-2:
        temperature = 1e-2

    top_p = float(top_p)

    generate_kwargs = dict(
        temperature=temperature,
        max_new_tokens=max_new_tokens,
        top_p=top_p,
        repetition_penalty=repetition_penalty,
        do_sample=True,
        seed=random.randint(0, 10 ** 7),
    )

    custom_instructions = """You are JARVIS(Just A Responsive Virtual Artificial Intelligence), a virtual artificial intelligence created by Bhardwaj Prasad Sutara. Be short and accurate with your responses.

"""
    formatted_prompt = format_prompt(prompt, chat_history, custom_instructions)
    client = InferenceClient(API_URL, headers=headers)
    response = client.text_generation(formatted_prompt, **generate_kwargs)
    return response


hi = generate("Hi, who are you?")
print(hi)
while True:
    query = input(">>> ")
    if "exit" in query:
        bye = generate("Goodbye JARVIS")
        print(bye)
        break
    else:
        output = generate(query)
        print(output)
