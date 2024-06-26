# MY TEXT EDITOR
#### Video Demo: https://youtu.be/pkmIQsRSivU
#### Description: my personal text editor
## Overview:
This project is a simple text editor application built using Python, Tkinter library and winreg to register application. It provides basic text editing features such as creating new files, opening existing files, saving files, cutting, copying, and pasting text, selecting all text, and indenting text. Additionally, it supports keyboard shortcuts for common tasks.  
Automatically register applications to open files on windows when open.  
With pyinstaller, we can runs without python installed.  
Users can adjust the text area size by resizing the main window to suit their preferences and customize the font of the text area to improve readability.  

## About
This project is developed as final project for Harvard University's CS50x Introduction to Computer Science Course.

This is an idea I came up while my microsoft office run out of date.  

## Components Explanation:
#### Main Window:

The main window of the application contains a text area where users can input and edit text.  
#### File Menu:

New: Clears the text area, allowing the user to start a new document.  
Open: Opens a file dialog window for the user to select an existing text file to open.  
Save: Saves the current document. If the document has not been saved before, it prompts the user to specify a file name and location.  
Save As...: Allows the user to specify a file name and location to save the current document.  
Exit: Closes the application.  
Find: Search all the text.  
Replace: replace all found.  

#### Edit Menu:

Undo: Undoes the last edit action.  
Redo: Redoes the last undone action.  
Cut: Cuts the selected text and places it on the clipboard.  
Copy: Copies the selected text to the clipboard.  
Paste: Pastes the text from the clipboard into the text area.  
Select All: Selects all text in the text area.  
   


#### Building the Application:
To build the application, Python, Tkinter library and pyinstaller are used. The code is organized into a class named SimpleTextEditor, which handles the main functionality of the application. The application is launched by creating an instance of this class and calling the mainloop() method.  

#### Register
```
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
```
## Code Structure and Implementation
The code is structured into a class (SimpleTextEditor) that encapsulates all the functionalities of the application. Here's a breakdown of the main components:  

Initialization:  
Sets up the main window, text area, and menu bar.  
Configures the title and dimensions of the window.  
Initializes the current file path to handle file operations.  

File Operations:

new_file: Clears the text area and resets the current file.  
open_file: Opens a selected file and loads its content into the text area.  
save_file: Saves the current content to the existing file or prompts for a new file name if it’s a first save.  
save_file_as: Allows the user to save the document with a new name.  
exit_editor: Exits the application, prompting to save changes if necessary.  
Edit Operations:

undo and redo: Undo and redo the last actions.  
cut, copy, and paste: Handle text manipulation operations.  
select_all: Selects all text in the document.  
find_replace_dialog: Opens a dialog for finding and replacing text.  
Additional Features:

register_app: Registers the application to handle text files via the Windows registry.
indent: Inserts a tab space when the Tab key is pressed.  

#### Weaknesses:
Lack of Advanced Features: The software lacks advanced features found in more robust text editors, such as syntax highlighting, plugin support, and advanced search functionalities. This makes it less suitable for programming and other specialized tasks.  
  
Limited File Support: It primarily supports plain text files. Users needing to work with other file formats (e.g., Rich Text Format, Markdown, or code files) might find this limiting.  
  
No Built-in Spell Check: The software does not include spell check functionality, which is a common feature in modern text editors. Users might need to rely on external tools for this purpose.  
  
Basic Error Handling: Error handling is quite basic. If a file operation fails, the software may not provide detailed feedback to the user.  
Non-Scalable for Large Projects: The software is not designed for handling large documents or complex projects. For instance, it might struggle with performance when dealing with very large text files.  
  
A bit..... slow:(( : This application is written in python( may not suitable for writing applications) and automatically register applications to open files on windows. So every time i open the app, it will automatically register again.  
  

## Conclusion:
Overall, this software provides a straightforward and user-friendly interface for basic text editing tasks. It is lightweight, easy to use.

## Update

I giveup at replace and find_next button :((

## Screenshots:

![alt text](preview/main.jpg)
![alt text](preview/open_with.jpg)

## License

This project is licensed under the [MIT License](LICENSE).

## Authors

- **Chicanancom** - [Chicanancom](https://github.com/chicanancom)
