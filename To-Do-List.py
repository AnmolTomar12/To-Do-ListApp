import tkinter as tk
from tkinter import messagebox
import os

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("350x450")
        self.root.configure(bg="#2c3e50")
        
        self.tasks = []
        self.load_tasks()
        
        self.frame = tk.Frame(self.root, bg="#2c3e50")
        self.frame.pack(pady=10)
        
        self.task_input = tk.Entry(self.frame, width=25, font=("Arial", 12), bg="#ecf0f1", fg="#2c3e50", borderwidth=0, highlightthickness=0)
        self.task_input.grid(row=0, column=0, padx=5)
        
        self.add_task_btn = tk.Button(self.frame, text="Add", command=self.add_task, bg="#1abc9c", fg="white", font=("Arial", 12), borderwidth=0, highlightthickness=0)
        self.add_task_btn.grid(row=0, column=1)
        
        self.task_listbox = tk.Listbox(self.root, width=40, height=15, font=("Arial", 12), bg="#ecf0f1", fg="#2c3e50", selectbackground="#1abc9c", borderwidth=0, highlightthickness=0)
        self.task_listbox.pack(pady=10)
        
        self.delete_task_btn = tk.Button(self.root, text="Delete", command=self.delete_task, bg="#e74c3c", fg="white", font=("Arial", 12), borderwidth=0, highlightthickness=0)
        self.delete_task_btn.pack(pady=5)
        
        self.update_task_listbox()
    
    def add_task(self):
        task = self.task_input.get()
        if task != "":
            self.tasks.append(task)
            self.update_task_listbox()
            self.task_input.delete(0, tk.END)
            self.save_tasks()
        else:
            messagebox.showwarning("Warning", "You must enter a task.")
    
    def delete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            self.tasks.pop(selected_task_index)
            self.update_task_listbox()
            self.save_tasks()
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task.")
    
    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)
    
    def load_tasks(self):
        if os.path.exists("tasks.txt"):
            with open("tasks.txt", "r") as file:
                self.tasks = file.read().splitlines()
    
    def save_tasks(self):
        with open("tasks.txt", "w") as file:
            for task in self.tasks:
                file.write(task + "\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()