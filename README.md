# Command Line Helper using OpenAI GPT-3

This application assists you in understanding and interacting with your command line, providing command suggestions based on your queries. It utilizes OpenAI's GPT-3 AI model to generate the responses. You can also run command line commands directly from the application, making it a versatile tool for command line interaction.

## Features

- Browse and select your working directory
- Interact with OpenAI's GPT-3 for command suggestions
- Execute command line commands
- View command execution output

## Setup

1. **API Key Setup**

    In order to use the OpenAI GPT-3, you need to acquire an API key from OpenAI. After acquiring the key:

    - Create a Python file in the same directory as your main Python application file and name it `config.py`.
    - In `config.py`, declare a variable `API_KEY` and assign your OpenAI API key to it like so:

    ```python
    API_KEY = 'your-openai-api-key'
    ```

    - This `API_KEY` will be imported into the main application file for use.

2. **Install Required Libraries**

    This application uses tkinter for the GUI, and the OpenAI API for interacting with GPT-3. Install these libraries using pip:

    ```bash
    pip install openai
    pip install tk
    ```

    Note: Tkinter comes pre-installed with standard Python distributions. 

3. **Running the Application**

    Simply navigate to the directory of the application in your terminal and run:

    ```bash
    python main.py
    ```

## How to Use

1. **Selecting a Working Directory**

    Use the 'Browse' button to select the directory in which you want to run command line commands.

2. **Interacting with the AI**

    Type your question or instruction in the 'Talk to AI' field and hit the Enter key or click the 'Send' button. For instance, you could ask "What does the app in this folder do?" or "What is the command to list all files in a directory?".

    The AI will generate a response which will be displayed in the 'Talk to AI' field.

3. **Running Command Line Commands**

    You can run command line commands directly from the app. Copy the command suggested by the AI (or type your own) in the 'CMD Command' field, then hit the Enter key or click the 'Run' button. The command will be executed in the currently selected directory.

    The output of the command will be displayed in the 'CMD Output' field.

---

The application is a versatile tool for understanding and interacting with the command line, particularly beneficial for beginners unfamiliar with command line operations. It combines the power of OpenAI's GPT-3 and Python's capability to execute system commands, creating a user-friendly interface for command line operations.
# CMDGPT
