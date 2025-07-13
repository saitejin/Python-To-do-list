import tkinter as tk
from tkinter import messagebox

# Create main app window
root = tk.Tk()
root.title("To-Do List App")
root.geometry("400x400")

# Task list
tasks = []

# ===== Functions =====
def add_task():
    task = entry.get()
    if task:
        tasks.append(task)
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Enter a task first.")

def delete_task():
    selected = listbox.curselection()
    if selected:
        task_index = selected[0]
        listbox.delete(task_index)
        tasks.pop(task_index)
    else:
        messagebox.showwarning("Warning", "Select a task to delete.")

def mark_done():
    selected = listbox.curselection()
    if selected:
        task_index = selected[0]
        task_text = listbox.get(task_index)
        listbox.delete(task_index)
        listbox.insert(task_index, f"✔️ {task_text}")
        listbox.itemconfig(task_index, fg="green")
    else:
        messagebox.showwarning("Warning", "Select a task to mark as done.")

# ===== UI Components =====
entry = tk.Entry(root, width=30, font=("Arial", 12))
entry.pack(pady=10)

add_btn = tk.Button(root, text="Add Task", command=add_task)
add_btn.pack(pady=5)

listbox = tk.Listbox(root, width=40, height=10, font=("Arial", 12))
listbox.pack(pady=10)

done_btn = tk.Button(root, text="Mark as Done", command=mark_done)
done_btn.pack(pady=5)

delete_btn = tk.Button(root, text="Delete Task", command=delete_task)
delete_btn.pack(pady=5)

# Run the app
root.mainloop()
