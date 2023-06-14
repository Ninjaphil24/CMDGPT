import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess
import openai

class CommandLineTool:
    def __init__(self, root):
        self.root = root
        root.title("Command Line Tool")

        # Browse directory frame
        frame = tk.Frame(root, bg='darkgray')
        frame.pack()

        self.working_dir = tk.StringVar()
        self.browse_button = tk.Button(frame, text="Browse", command=self.browse_folder)
        self.browse_button.pack(side=tk.LEFT)
        
        self.directory_label = tk.Label(frame, textvariable=self.working_dir)
        self.directory_label.pack(side=tk.LEFT)

        # Conversation with AI frame
        self.conversation = tk.Text(root, state='disabled', height=15, width=100, bg='black', fg='white', insertbackground='white')
        self.conversation.pack()

        self.ai_input = tk.Text(root, height=5, bg='black', fg='white', insertbackground='white')
        self.ai_input.pack()
        
        self.send_button = tk.Button(root, text="Send", command=self.talk_to_ai)
        self.send_button.pack()

        # Command line frame
        self.cmd_input = tk.Text(root, height=5, bg='black', fg='white', insertbackground='white')
        self.cmd_input.pack()
        
        self.run_button = tk.Button(root, text="Run", command=self.run_command)
        self.run_button.pack()

        self.cmd_output = tk.Text(root, state='disabled', height=15, width=100, bg='black', fg='white', insertbackground='white')
        self.cmd_output.pack()

        self.copy_output_button = tk.Button(root, text="Copy Output to Prompt", command=self.copy_output_to_prompt)
        self.copy_output_button.pack()

    def browse_folder(self):
        self.working_dir.set(filedialog.askdirectory())

    def talk_to_ai(self):
        instruction = self.ai_input.get("1.0", tk.END).strip()
        response = self.get_ai_suggestion(instruction)
        self.conversation.config(state='normal')
        self.conversation.insert(tk.END, "You: " + instruction + "\n")
        self.conversation.insert(tk.END, "AI: " + response + "\n")
        self.conversation.config(state='disabled')
        self.ai_input.delete("1.0", tk.END)

    def run_command(self):
        command = self.cmd_input.get("1.0", tk.END).strip()
        try:
            folder = self.working_dir.get()
            process = subprocess.Popen(command, cwd=folder, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output, error = process.communicate()
            if error:
                raise Exception(error.decode("utf-8"))
            self.cmd_output.config(state='normal')
            self.cmd_output.insert(tk.END, output.decode('utf-8') + "\n")
            self.cmd_output.config(state='disabled')
            self.cmd_input.delete("1.0", tk.END)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def copy_output_to_prompt(self):
        output = self.cmd_output.get("1.0", tk.END).strip()
        self.ai_input.insert(tk.END, "\nCMD Output:\n" + output)

    def get_ai_suggestion(self, instruction):
        conversation = self.conversation.get("1.0", tk.END) + "You: " + instruction
        openai.api_key = 'API'
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=conversation,
            temperature=0.5,
            max_tokens=200
        )
        return response.choices[0].text.strip()

root = tk.Tk()
tool = CommandLineTool(root)
root.mainloop()
