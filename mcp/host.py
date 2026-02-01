import os

from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

anthropic_client = Anthropic(api_key=LLM_API_KEY)

GOODBYE = "goodbye"

print(f"Hello world, Type '{GOODBYE}' to quit.")

def main():
    while True:
        prompt = input("You: ")
        if prompt.lower() == GOODBYE:
            print(f"AI ASsistent: {GOODBYE.capitalize()}!")
            break
        message = anthropic_client.messages.create(
            max_tokens=4096,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model="claude-haiku-4-5",
        )
        for response in message.content:
            print(f"Assistant: {response.text}")


if __name__ == "__main__":
    main()
