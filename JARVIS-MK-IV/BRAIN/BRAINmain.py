import requests
import re
import json

def generate_response(prompt: list, system_prompt: str = "Be Helpful and Friendly", model: str = "Phind Instant", stream_chunk_size: int = 12, stream: bool = True) -> str:
    """
    Generates a response from the Phind Instant model based on the given prompt.

    Parameters:
    - prompt (list): A list containing the conversation history with the user. Each entry is a dictionary with 'role' and 'content'.
    - system_prompt (str, optional): The system prompt to use for the model. Defaults to "Be Helpful and Friendly".    
    - model (str, optional): The model to use for generating the response. Available options:
        - "Phind-34B"
        - "Phind Instant"
    - stream_chunk_size (int, optional): The number of bytes to read from the response stream. Defaults to 12.
    - stream (bool, optional): Whether to stream the response or return it all at once. Defaults to True.
                                            
    Returns:
    - str: The generated text response from the model.

    This function sends a POST request to the Phind Instant API, streams the response, 
    and collects the generated text to return as a single string.
    """
    
    headers = {"User-Agent": ""}
    
    # Insert system prompt at the beginning of the conversation history
    prompt.insert(0, {"role": "system", "content": system_prompt})
    
    # Prepare the payload for the POST request
    payload = {
        "additional_extension_context": "",
        "allow_magic_buttons": True,
        "is_vscode_extension": True,
        "message_history": prompt,
        "requested_model": model,
        "user_input": prompt[-1]["content"],
    }

    # API endpoint
    chat_endpoint = "https://https.extension.phind.com/agent/"
    
    # Send the POST request and stream the response
    try:
        response = requests.post(chat_endpoint, headers=headers, json=payload, stream=True)
        response.raise_for_status()  # Check for any HTTP errors

        # Collect the streamed text content
        streaming_text = ""
        for chunk in response.iter_lines(decode_unicode=True, chunk_size=stream_chunk_size):
            # Clean the data prefix
            cleaned_chunk = re.sub("data:", "", chunk)
            if cleaned_chunk:
                try:
                    # Parse the JSON response and extract the content
                    json_chunk = json.loads(cleaned_chunk)
                    content = json_chunk["choices"][0]["delta"]["content"]
                    if stream:
                        streaming_text += content  # Accumulate the content without printing
                except (KeyError, json.JSONDecodeError) as e:
                    # Handle errors gracefully if response format is unexpected
                    continue

        return streaming_text

    except requests.exceptions.RequestException as e:
        print(f"Error during request: {e}")
        return ""


'''
if __name__ == "__main__":
    # Predefined system prompt
    system_prompt = ("Talk like JARVIS from the Iron Man movies, call me sir, "
                     "my name is Bhardwaj, I am born in New Delhi, India. "
                     "Keep your response straightforward, short, and concise. "
                     "You are a very sophisticated and advanced AI assistant capable of doing most tasks as best as you can.")

    # User input prompt
    user_input = input(">>> ")
    user_prompt = {"role": "user", "content": user_input}

    # Define the conversation history
    prompt = [user_prompt]

    # Generate the response from the model
    response = generate_response(prompt=prompt, system_prompt=system_prompt, model="Phind-34B", stream=True)
    
    # Output the final response (only once)
    if response:
        print(response)
    else:
        print("No response received.")

'''
