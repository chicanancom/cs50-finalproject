# MY TEXT EDITOR
#### Video Demo:  <URL HERE>
#### Description: my personal text editor
## Overview:
This project is a simple text editor application built using Python and the Tkinter library. It provides basic text editing features such as creating new files, opening existing files, saving files, cutting, copying, and pasting text, selecting all text, and indenting text. Additionally, it supports keyboard shortcuts for common tasks.

## Components Explanation:
#### Main Window:

The main window of the application contains a text area where users can input and edit text.
#### File Menu:
```
New: Clears the text area, allowing the user to start a new document.
Open: Opens a file dialog window for the user to select an existing text file to open.
Save: Saves the current document. If the document has not been saved before, it prompts the user to specify a file name and location.
Save As...: Allows the user to specify a file name and location to save the current document.
Exit: Closes the application.
```
#### Edit Menu:
```
Undo: Undoes the last edit action.
Redo: Redoes the last undone action.
Cut: Cuts the selected text and places it on the clipboard.
Copy: Copies the selected text to the clipboard.
Paste: Pastes the text from the clipboard into the text area.
Select All: Selects all text in the text area.
```
####Context Menu (Right-click Menu):
```
Provides quick access to cut, copy, paste, and select all actions via right-click.
```
#### Keyboard Shortcuts:

Ctrl + A: Selects all text in the text area.
Ctrl + X: Cuts the selected text.
Tab: Indents the selected line(s) or inserts a tab character at the cursor position.
Font Customization:

Users can customize the font of the text area to improve readability.
#### Text Area Adjustments:

Users can adjust the text area size by resizing the main window to suit their preferences.
#### Building the Application:
To build the application, Python and the Tkinter library are used. The code is organized into a class named SimpleTextEditor, which handles the main functionality of the application. The application is launched by creating an instance of this class and calling the mainloop() method.

## Conclusion:
Overall, this software provides a straightforward and user-friendly interface for basic text editing tasks. It is lightweight, easy to use, and can be further customized or extended based on user requirements.
