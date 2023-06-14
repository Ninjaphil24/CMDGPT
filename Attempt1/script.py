import openai
import json

openai.api_key = 'API'

def get_prompt():
    while True:
        prompt = input("Please enter a prompt, or 'exit' to quit: ")
        if prompt.lower() == 'exit':
            return None
        return prompt

def generate_response(prompt, engine='text-davinci-003'):
    response = openai.Completion.create(
        engine=engine,
        prompt=prompt,
        max_tokens=100
    )

    return response.choices[0].text.strip()

def main():
    while True:
        prompt = get_prompt()
        if prompt is None:
            break
        response = generate_response(prompt)
        print(json.dumps(response, indent=4))

if __name__ == "__main__":
    main()
