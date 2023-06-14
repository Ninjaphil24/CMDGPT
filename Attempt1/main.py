import openai
import subprocess
import PySimpleGUI as sg

openai.api_key = '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'

def generate_response(prompt, engine='text-davinci-003'):
    response = openai.Completion.create(
        engine=engine,
        prompt=prompt,
        max_tokens=100
    )

    return response.choices[0].text.strip()

def run_command(command):
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()

    if error:
        return f"An error occurred: {error}"
    else:
        return output.decode('utf-8')

def create_interface():
    sg.theme('DarkBlue3')  # add this line to set the theme

    layout = [
        [sg.Multiline(size=(60, 4), key='-PROMPT-', enable_events=True)],
        [sg.Button('Browse', key='-BROWSE-'), sg.Button('Generate Response'), sg.Button('Run Command')],
        [sg.Output(size=(120,40), key='-OUTPUT-')],
    ]

    window = sg.Window('GPT Interface', layout, location=(None, None))

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED:
            break
        elif event == 'Generate Response':
            response = generate_response(values['-PROMPT-'])
            window['-OUTPUT-'].update(response)
        elif event == 'Run Command':
            window['-OUTPUT-'].update(f"Running command: {values['-PROMPT-']}\n")
            output = run_command(values['-PROMPT-'])
            window['-OUTPUT-'].update(output)
        elif event == '-BROWSE-':
            folder = sg.popup_get_folder('Please select a folder')
            window['-PROMPT-'].update(folder)

    window.close()

create_interface()
