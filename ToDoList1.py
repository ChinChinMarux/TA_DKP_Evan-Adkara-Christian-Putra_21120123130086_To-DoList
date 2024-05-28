import json
import tkinter as tk
from tkinter import simpledialog
from PIL import Image, ImageTk

class TaskManagerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Manager")
        self.root.geometry("685x390")
        self.root.resizable(False, False)

        self.background_image = Image.open("...\Assets\stl.jpg") 
        self.background_photo = ImageTk.PhotoImage(self.background_image)
        self.background_label = tk.Label(root, image=self.background_photo)
        self.background_label.place(relwidth=1, relheight=1)

        self.tasks = self.load_tasks()

        self.create_widgets()

    def create_widgets(self):
        self.task_label = tk.Label(self.root, pady=2, text="List Tugas Kamu Hari Ini :)", font=(15), bg="white", highlightthickness=0)
        self.task_label.pack()
        self.task_listbox = tk.Listbox(self.root, width=50, height=15)
        self.task_listbox.pack(pady=5)

        self.refresh_tasks()

        add_button = tk.Button(self.root, text="Tambah Tugas", command=self.add_task, bg="white", highlightthickness=0)
        add_button.pack(pady=5)

        done_button = tk.Button(self.root, text="Tandai Selesai", command=self.mark_done, bg="white", highlightthickness=0)
        done_button.pack(pady=5)

        delete_button = tk.Button(self.root, text="Hapus Tugas", command=self.delete_task, bg="white", highlightthickness=0)
        delete_button.pack(pady=5)

    def load_tasks(self):
        try:
            with open("tugas.json", "r") as file:
                tasks = json.load(file)
        except FileNotFoundError:
            tasks = []
        return tasks

    def save_tasks(self):
        with open("tugas.json", "w") as file:
            json.dump(self.tasks, file)

    def refresh_tasks(self):
        self.task_listbox.delete(0, tk.END)
        for idx, task in enumerate(self.tasks, 1):
            status = "Selesai" if task['done'] else "Belum Selesai"
            self.task_listbox.insert(tk.END, f"{idx}. {task['description']} - {status}")

    def add_task(self):
        description = simpledialog.askstring("Tambah Tugas", "Masukkan deskripsi tugas baru:")
        if description:
            task = {"description": description, "done": False}
            self.tasks.append(task)
            self.save_tasks()
            self.refresh_tasks()

    def mark_done(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            self.tasks[index]["done"] = True
            self.save_tasks()
            self.refresh_tasks()

    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            deleted_task = self.tasks.pop(index)
            self.save_tasks()
            self.refresh_tasks()

    def run(self):
        self.root.mainloop()

def main():
    root = tk.Tk()
    app = TaskManagerGUI(root)
    app.run()

if __name__ == "__main__":
    main()
