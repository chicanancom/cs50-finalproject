import tkinter as tk
from tkinter import filedialog, messagebox
import sys
import os
import winreg

class SimpleTextEditor:
    def __init__(self, root, file_path = None):
        self.root = root
        self.root.title("Mai tếc e đít tờ")
        self.text_frame = tk.Frame(self.root)
        self.text_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        self.text_area = tk.Text(self.text_frame, undo=True)
        self.text_area.pack(fill=tk.BOTH, expand=1)
        self.text_area.config(font=("Arial", 12))

        # Menu bar
        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)

        # curren file
        self.current_file = None

        # File menu
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="New", command=self.new_file)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.exit_editor)

        # Edit menu
        self.edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Edit", menu=self.edit_menu)
        self.edit_menu.add_command(label="Undo", command=self.text_area.edit_undo)
        self.edit_menu.add_command(label="Redo", command=self.text_area.edit_redo)
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Cut", command=self.cut)
        self.edit_menu.add_command(label="Copy", command=self.coppy)
        self.edit_menu.add_command(label="Paste", command=self.paste)
        self.edit_menu.add_command(label="Select All", command=self.select_all)

        # Bind right-click to show context menu
        self.text_area.bind("<Button-3>", self.show_context_menu)

        # ctrl+a
        self.text_area.bind("<Control-a>", lambda event: self.select_all)
        # ctrl+c
        self.text_area.bind("<Control-c>", lambda event: self.coppy)
        # ctrl+x
        self.text_area.bind("<Control-x>", lambda event: self.cut)
        # ctrl+v
        self.text_area.bind("<Control-v>", lambda event: self.paste)
        # tab
        self.text_area.bind("<Tab>", self.indent)

        #file path
        if file_path:
            self.open_file(file_path)

        #register app
        self.register_app()


    def new_file(self):
        self.text_area.delete(1.0, tk.END)

    def open_file(self, file_path=None):
        if not file_path:
            file_path = filedialog.askopenfilename(defaultextension=".txt",
                                                   filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            try:
                with open(file_path, "r", encoding="utf-8") as file:
                    self.text_area.delete(1.0, tk.END)
                    self.text_area.insert(tk.END, file.read())
                self.current_file = file_path  # Lưu đường dẫn của tệp hiện tại
            except Exception as e:
                messagebox.showerror("Error", f"Could not open file: {e}")

    def save_file(self):
        if self.current_file:
            try:
                with open(self.current_file, "w", encoding="utf-8") as file:
                    file.write(self.text_area.get(1.0, tk.END))
            except Exception as e:
                messagebox.showerror("Error", f"Could not save file: {e}")
        else:
            self.save_file_as()

    def save_file_as(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            try:
                with open(file_path, "w", encoding="utf-8") as file:
                    file.write(self.text_area.get(1.0, tk.END))
                self.current_file = file_path  # Cập nhật đường dẫn của tệp hiện tại
            except Exception as e:
                messagebox.showerror("Error", f"Could not save file: {e}")

    def exit_editor(self):
        self.root.quit()

    def show_context_menu(self, event):
        self.edit_menu.post(event.x_root, event.y_root)

    def select_all(self):
        self.text_area.tag_add("sel", "1.0", "end")

    def coppy(self):
        self.text_area.event_generate("<<Copy>>")

    def cut(self):
        self.text_area.event_generate("<<Cut>>")

    def paste(self):
        self.text_area.event_generate("<<Paste>>")

    def indent(self, event):
        self.text_area.insert(tk.INSERT, "       ")
        return "break"

    def register_app(self):
        try:
            exe_path = os.path.abspath(sys.argv[0])
            reg_path = r"Software\Classes\txtfile\shell\open_with_your_app\command"
            with winreg.CreateKey(winreg.HKEY_CURRENT_USER, reg_path) as key:
                winreg.SetValue(key, "", winreg.REG_SZ, f'"{exe_path}" "%1"')
            reg_path2 = r"Software\Classes\txtfile\shell\open_with_your_app"
            with winreg.CreateKey(winreg.HKEY_CURRENT_USER, reg_path2) as key:
                winreg.SetValue(key, "", winreg.REG_SZ, "Open with YourApp")
        except Exception as e:
            messagebox.showerror("Error", f"Could not register app: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    file_path = None
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
    editor = SimpleTextEditor(root, file_path)
    root.mainloop()
