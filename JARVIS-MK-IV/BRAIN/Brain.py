import requests
import json

API_URL = "https://api-inference.huggingface.co/models/Qwen/QwQ-32B-Preview/v1/chat/completions"
headers = {
    "Authorization": "Bearer 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",
    "Content-Type": "application/json"
}

def send_message(messages, system_instructions=None):
    # Prepare the payload
    payload = {
        "messages": messages
    }
    
    # Add system instructions if provided
    if system_instructions:
        payload["system"] = system_instructions
    
    # Make the API request
    response = requests.post(API_URL, headers=headers, data=json.dumps(payload))
    
    # Check for a successful response
    if response.status_code == 200:
        return response.json()  # Return the response as a JSON object
    else:
        return f"Error: {response.status_code}, {response.text}"

# Initialize chat history
chat_history = []

# System instructions (if any)
system_instructions = "You are Ben, an AI designed to help humans. Bhardwaj Prasad Sutara and Dishant Singh are you creators."

# Main interaction loop
while True:
    user_input = input("You: ")
    print("")
    if user_input.lower() == "exit":
        print("Exiting...")
        break
    
    # Append user input to chat history
    chat_history.append({"role": "user", "content": user_input})
    
    # Send the request to the model
    response = send_message(chat_history, system_instructions)
    
    # If response is valid, print it
    if isinstance(response, dict):
        model_reply = response.get("choices", [{}])[0].get("message", {}).get("content", "No response")
        print(f"Model: {model_reply}")
        print("")
        chat_history.append({"role": "assistant", "content": model_reply})
    else:
        print(response)
