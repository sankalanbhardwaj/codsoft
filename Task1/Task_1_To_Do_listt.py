from tkinter import*
from tkinter import messagebox


# Functions
def add_task():
    task=entry.get()
    if task:
        listbox.insert(END,task)
        entry.delete(0,END)
        save_tasks()
    else:
        messagebox.showwarning("Input Error", "Please add task")

def delete_task():
    try:
        selected_task_index=listbox.curselection()[0]
        listbox.delete(selected_task_index)
        save_tasks()
    except:
        messagebox.showwarning("Error", "Please select task to delete!")

def clear_all():
    if messagebox.askyesno("Confirm","Are you sure to clear all tasks?"):
        listbox.delete(0, END)
        save_tasks()

# Save tasks
def save_tasks():
    with open("my_tasks_list.txt","w") as f:
        for count in range(listbox.size()):
            f.write(listbox.get(count)+ "\n")

def load_tasks():
    try:
        with open("my_tasks_list.txt","r") as f:
            my_tasks_list=f.read().splitlines()
            for task in my_tasks_list:
                listbox.insert(END,task)
    except FileNotFoundError:
        pass

# Create window
window=Tk()

window.title("To-Do List")
window.geometry("400x400")
window.config(bg="lightgrey")
label=Label(window,text="To-Do List",font=("Arial,15"),fg="black",bg="light grey")
label.pack()

entry = Entry(window, width=20, borderwidth=5, font=("Arial", 20), justify='right')
entry.pack(pady=10, padx=20, fill=X)

# Buttons Frame
button_frame = Frame(window, bg="lightgrey")
button_frame.pack(pady=10)

# Add Button
button = Button(button_frame, text="Add Task", width=12, command=add_task, bg="blue", fg="white")
button.grid(row=0, column=0, padx=5)

# Delete Button
button = Button(button_frame, text="Delete Task", width=12, command=delete_task, bg="orange", fg="white")
button.grid(row=0, column=1, padx=5)

# Clear All Button
button = Button(button_frame, text="Clear All", width=12, command=clear_all, bg="red", fg="white")
button.grid(row=0, column=2, padx=5)

# Listbox for tasks
listbox = Listbox(window, font=("Arial", 14), height=8, selectbackground="light green", activestyle='none')
listbox.pack(pady=7, padx=14, fill=BOTH, expand=True)


load_tasks()
window.mainloop()


