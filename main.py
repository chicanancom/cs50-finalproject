import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
import sys
from tkinter import ttk
from tkinter import *
import os
import winreg


class SimpleTextEditor:

    def __init__(self, root, file_path = None):
        self.root = root
        self.root.title("Mai tếc e đít tờ")
        self.text_frame = tk.Frame(self.root)
        self.text_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=5)
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
        self.file_menu.add_command(label="New", command=self.new_file, accelerator='Ctrl+N')
        self.file_menu.add_command(label="Open", command=self.open_file, accelerator='Ctrl+O')
        self.file_menu.add_command(label="Save", command=self.save_file, accelerator='Ctrl+S')
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.exit_editor)

        # Edit menu
        self.edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Edit", menu=self.edit_menu)
        self.edit_menu.add_command(label="Undo", command=self.text_area.edit_undo, accelerator='Ctrl+Z')
        self.edit_menu.add_command(label="Redo", command=self.text_area.edit_redo, accelerator='Ctrl+Y')
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Cut", command=self.cut, accelerator='Ctrl+X')
        self.edit_menu.add_command(label="Copy", command=self.copy, accelerator='Ctrl+C')
        self.edit_menu.add_command(label="Paste", command=self.paste, accelerator='Ctrl+V')
        self.edit_menu.add_command(label="Select All", command=self.select_all, accelerator='Ctrl+A')
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Find/Replace", command=self.find_replace_dialog)

        # Bind right-click to show context menu
        self.text_area.bind("<Button-3>", self.show_context_menu)

        # ctrl+f
        self.text_area.bind("<Control-f>", lambda event: self.find_replace_dialog())
        # # ctrl+c
        # self.text_area.bind("<Control-c>", lambda event: self.copy)
        # # ctrl+x
        # self.text_area.bind("<Control-x>", lambda event: self.cut)
        # # ctrl+v
        # self.text_area.bind("<Control-v>", lambda event: self.paste)
        # # tab
        self.text_area.bind("<Tab>", self.indent)

        #file path
        if file_path:
            self.open_file(file_path)
        #register app
        self.register_app()


    def new_file(self, event=None):
        if(messagebox.askyesno("Save?", "Do you wish to save current file?")):
            self.save_file()
            self.txt.delete('1.0', END)
            self.window.title("Notepad")
            self.currentFile = "No File"
        else:
            self.txt.delete('1.0', END)
            self.window.title("Notepad")
            self.currentFile = "No File"

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

    def cut(self, event=None):
        self.copy()
        self.text_area.delete(tk.SEL_FIRST, tk.SEL_LAST)

    def copy(self, event=None):
        self.root.clipboard_clear()
        try:
            text = self.text_area.get(tk.SEL_FIRST, tk.SEL_LAST)
            self.root.clipboard_append(text)
        except tk.TclError:
            pass

    def paste(self, event=None):
        try:
            text = self.root.selection_get(selection='CLIPBOARD')
            self.text_area.insert(tk.INSERT, text)
        except tk.TclError:
            pass

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

    def find_replace_dialog(self):
        dialog = tk.Toplevel(self.root)
        dialog.title("Find and Replace")

        tk.Label(dialog, text="Find:").grid(row=0, column=0, padx=4, pady=4)
        find_entry = tk.Entry(dialog, width=30)
        find_entry.grid(row=0, column=1, padx=4, pady=4)

        tk.Label(dialog, text="Replace:").grid(row=1, column=0, padx=4, pady=4)
        replace_entry = tk.Entry(dialog, width=30)
        replace_entry.grid(row=1, column=1, padx=4, pady=4)

        def find_next():
            self.find_text(find_entry.get())

        def replace():
            self.replace_text(find_entry.get(), replace_entry.get())

        def replace_all():
            self.replace_all_text(find_entry.get(), replace_entry.get())

        tk.Button(dialog, text="Find Next", command=find_next).grid(row=2, column=0, padx=4, pady=4)
        # tk.Button(dialog, text="Replace", command=replace).grid(row=2, column=1, padx=4, pady=4)
        tk.Button(dialog, text="Replace All", command=replace_all).grid(row=2, column=1, padx=4, pady=4)

    def find_text(self, find_string):
        self.text_area.tag_remove('highlight', '1.0', tk.END)
        if find_string:
            start_pos = "1.0"
            while True:
                start_pos = self.text_area.search(find_string, start_pos, tk.END)
                if not start_pos:
                    break
                end_pos = f"{start_pos} + {len(find_string)}c"
                self.text_area.tag_add("highlight", start_pos, end_pos)
                start_pos = end_pos
            self.text_area.tag_config("highlight", background="yellow", foreground="black")

    def replace_text(self, find_string, replace_string):
        start_pos = self.text_area.index(tk.INSERT)
        start_pos = self.text_area.search(find_string, start_pos, tk.END)
        if start_pos:
            end_pos = f"{start_pos} + {len(find_string)}c"
            self.text_area.delete(start_pos, end_pos)
            self.text_area.insert(start_pos, replace_string)
            self.text_area.tag_remove('highlight', start_pos, end_pos)
            self.find_start_pos = f"{start_pos} + {len(replace_string)}c"
        self.find_text(find_string)

    def replace_all_text(self, find_string, replace_string):
        self.text_area.tag_remove('highlight', '1.0', tk.END)
        if find_string and replace_string:
            start_pos = "1.0"
            while True:
                start_pos = self.text_area.search(find_string, start_pos, tk.END)
                if not start_pos:
                    break
                end_pos = f"{start_pos} + {len(find_string)}c"
                self.text_area.delete(start_pos, end_pos)
                self.text_area.insert(start_pos, replace_string)
                start_pos = f"{start_pos} + {len(replace_string)}c"

if __name__ == "__main__":
    root = tk.Tk()
    file_path = None
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
    editor = SimpleTextEditor(root, file_path)
    root.mainloop()
