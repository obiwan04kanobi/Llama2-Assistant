import tkinter as tk
import subprocess

def get_response(input_text):
    command = f'ollama run llama2 "{input_text}"'
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    stdout, stderr = process.communicate()
    response =stdout.decode().strip()
    return response

def send_message(event=None):
    message = user_input.get()
    if message.strip() != '':
        user_input.delete(0, tk.END)
        response = get_response(message)
        output_text.config(state=tk.NORMAL)
        output_text.insert(tk.END, "You: " + message + '\n')
        output_text.insert(tk.END, "llama2: " + response + '\n\n')
        output_text.config(state=tk.DISABLED)

# GUI
root = tk.Tk()
root.title("Llama2")

# Input box
user_input = tk.Entry(root, font=('Helvetica', 20))
user_input.bind("<Return>", send_message)
user_input.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=10, ipady=10)

# Output box
output_text = tk.Text(root, font=('Helvetica', 20), state=tk.DISABLED)
output_text.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=10)

# Send button
send_button = tk.Button(root, text="Send", command=send_message, font=('Helvetica', 14))
send_button.pack(side=tk.BOTTOM, padx=10, pady=10)

root.mainloop()
