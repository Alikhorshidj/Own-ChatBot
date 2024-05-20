import openai

openai.api_key = '#'

def generate_response(prompt):
    response = openai.ChatCompletion.create(
        engine="gpt-3.5-turbo",
        prompt=prompt,
        max_tokens=150
    )

    return response.choices[0].text.strip()

user_input = input("Start Chat: ")
while user_input.lower() != 'bye':
    prompt = f"user: {user_input}\nChatBot:"
    response = generate_response(prompt)
    print(response)
    user_input = input("User: ")

print("Goodbye!")