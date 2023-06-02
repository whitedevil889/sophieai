import openai

# Set up your OpenAI API key
openai.api_key = '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'

# Define a function to send a message to Sophie and get a response
def send_message(message):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=message,
        temperature=0.7,
        max_tokens=100,
        n=1,
        stop=None,
        timeout=None,
        log_level='info'
    )
    return response.choices[0].text.strip()

# Interactive loop to chat with Sophie
while True:
    user_input = input("User: ")
    if user_input.lower() == 'bye':
        print("Sophie: Goodbye!")
        break
    response = send_message(user_input)
    print("Sophie:", response)
