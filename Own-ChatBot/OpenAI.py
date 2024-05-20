from openai import OpenAI

openai = OpenAI()

api_key = '#'
openai.api_key = api_key


def generate_response(prompt):
    response = openai.ChatCompletion.create(
        engine="gpt-3.5-turbo",
        prompt=prompt,
        max_tokens=150
    )

    return response.choices[0].text.strip()


user_input = input("Start Chat:")
while user_input.lower() != 'by':
    prompt = f"user: {user_input}\nChatBot"
    generate_response(prompt)
    user_input = input("Who are you:")

print("by")
