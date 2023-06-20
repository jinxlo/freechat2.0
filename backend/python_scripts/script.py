import gpt4all
import sys
import json

def chat_with_gpt4all_model(input_text):
    model_path = './gpt4all'  # Changed this line
    gptj = gpt4all.GPT4All(model_name="nulu3.5", model_path=model_path)
    input_messages = [{"role": "system", "content": "You are a helpful assistant."},
                      {"role": "user", "content": input_text}]
    message = gptj.get_top_reply(input_messages)
    return message


if __name__ == "__main__":
    print("Python script: main")
    user_input = sys.argv[1]

    response = chat_with_gpt4all_model(user_input)
    print(f"Python script: response -> {response}")

    print(json.dumps(response))
