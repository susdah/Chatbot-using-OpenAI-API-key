import os # As per https://docs.python.org/3/library/os.html
from openai import OpenAI # As per https://platform.openai.com/docs/libraries
from dotenv import load_dotenv # As per https://pypi.org/project/python-dotenv/

# Load varialbes from .env files.
load_dotenv()

# Initiate the OpenAI client using the API key from the .env file.
client = OpenAI(api_key = os.getenv("OPENAI_API_KEY"))

# Select the model type.
model_of_AI = "gpt-4o-mini"

# List of dicts where each dict is a line from the chat. It saves the role and the contents of the message.
conversation_history = [{"role": "system", "content": "Starting point"}]

# Print intiating message.
print("Type to make the AI respond, type bye to exit")


# While True, the user can type input.
while True:
    user_input = input("Human: ")

    # If the user uses the exit word the loop breaks.
    if user_input.lower() == "bye":
        print("Computer: Have a nice day!")
        break

    # Append the user input as a dict to the list conversation_history.
    conversation_history.append({"role": "user", "content": user_input})

    # Generate response from the AI.
    response = client.chat.completions.create(
        model = model_of_AI,
        messages = conversation_history
    )

    # Use the response to make the computer print a reply.
    reply = response.choices[0].message.content
    print(f"Computer: {reply}")

    # Append the computer's input to the conversation_history.
    conversation_history.append({"role": "assistant", "content": reply})
