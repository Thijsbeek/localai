import os
import json
import argparse

from dotenv import load_dotenv
from openai import OpenAI
from prompts import system_prompt
from call_function import available_functions, call_function


load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")
if not api_key:
    raise RuntimeError("OPENROUTER_API_KEY is not set in the environment variables.")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)

parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")

args = parser.parse_args()

messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": args.user_prompt},
]

response = client.chat.completions.create(
    model="openrouter/free",
    messages=messages,
    tools = available_functions,
)

if not response.usage:
    raise RuntimeError("failed API request")

message = response.choices[0].message

if args.verbose:
    print(f"User prompt: {args.user_prompt}")
    print(f"Prompt tokens: {response.usage.prompt_tokens}")
    print(f"Response tokens: {response.usage.completion_tokens}")

if message.tool_calls:
    for tool_call in message.tool_calls:
        result_message = call_function(tool_call, verbose=args.verbose)

        if not result_message["content"]:
            raise Exception("Tool call returned an empty result")

        if args.verbose:
            print(f"-> {result_message['content']}")
else:
    print(message.content)