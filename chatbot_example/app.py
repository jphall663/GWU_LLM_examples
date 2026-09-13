"""A minimal Azure OpenAI terminal chatbot. Copyright 2026 jphall@gwu.edu (MIT)."""

import os
from getpass import getpass

from openai import AzureOpenAI

RESOURCE = "gw-sb-01"
ENDPOINT = f"https://{RESOURCE}.openai.azure.com/"
MAX_OUTPUT_TOKENS = 600


def main():
    # Read the key securely, then create one Azure Responses API client.
    api_key = os.getenv("GW_AZURE_OPENAI_KEY") or getpass("Azure OpenAI API key: ")

    client = AzureOpenAI(
        azure_endpoint=ENDPOINT,
        api_key=api_key,
        api_version="2025-03-01-preview",
    )

    # This list is the chatbot's short-term memory: each user and assistant turn
    # is saved here and sent back with the next question.
    conversation = []

    print("Simple chatbot. Type 'quit' to exit.")

    while True:
        question = input("You: ").strip()

        if question.lower() in {"quit", "exit"}:
            break

        if not question:
            continue

        conversation.append({"role": "user", "content": question})

        # Use only the latest six exchanges (12 messages) as short-term memory.
        # This preserves recent context without letting the prompt grow forever.
        recent_conversation = conversation[-12:]

        # GPT-5 can use tokens for internal reasoning, so leave room for visible text.
        # Retry once with a larger budget only when the first response has no text.
        answer = ""

        for token_limit in (MAX_OUTPUT_TOKENS, 800):
            response = client.responses.create(
                model="gpt-5-mini",
                input=recent_conversation,
                max_output_tokens=token_limit,
            )
            answer = response.output_text.strip()

            if answer:
                break

        # Do not store an empty reply: it would make later turns confusing.
        if not answer:
            conversation.pop()
            print("Assistant: No visible response was returned. Please try again.\n")
            continue

        conversation.append({"role": "assistant", "content": answer})

        print(f"Assistant: {answer}\n")


if __name__ == "__main__":
    main()
