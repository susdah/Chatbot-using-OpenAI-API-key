# NAME OF PROJECT: Chatbot using OpenAI API key
## Files available in folder: 
1. **chatbot.py**: Contain the program.
2. **README.md**: This file.
## Files not available in this folder:
1. The .env file that contains my private API key.

## Description:
This chatbot is a simple one. It uses an API-key provided by OpenAI to generate and print a computer's text responses to a human user's text input. 

### About the API-key:
The API key is private and therefore stored in a .env file that is not shared here. The program imports libraries with functions that allows it to read .env and import the API key from that file. For this to work the .env file must be located in the same repository as the file chatbot.py. I have chosen not to share that publically as it is my personal API-key. 

### How to use this program:
You will need to use your own OpenAI API-key to use this program. Log in to https://openai.com/, generate an API-key and save it in your own .env file. It is important that the .env file is stored in the same location as chatbot.py. 

## List of links to documentation used:
1. os: https://docs.python.org/3/library/os.html
2. OpenAI: https://platform.openai.com/docs/libraries
3. OpenAI API references: https://platform.openai.com/docs/api-reference/introduction
4. dotenv: https://pypi.org/project/python-dotenv/
