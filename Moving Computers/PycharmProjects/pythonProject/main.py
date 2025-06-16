import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QAction, QFileDialog
from PyQt5.QtGui import QIcon, QFontDatabase
from PyQt5.QtCore import Qt


class Notepad(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set the window properties
        self.setWindowTitle('Notes')
        self.setWindowIcon(QIcon('notes_icon.png'))
        self.setGeometry(100, 100, 800, 600)

        # Load the custom stylesheet
        with open('style.qss', 'r') as f:
            stylesheet = f.read()
        self.setStyleSheet(stylesheet)

        # Create a QTextEdit widget to display and edit the notes
        self.text_edit = QTextEdit()
        self.setCentralWidget(self.text_edit)

        # Set the font
        font_db = QFontDatabase()
        font_id = font_db.addApplicationFont('SF-Pro-Text-Regular.otf')
        font_family = font_db.applicationFontFamilies(font_id)[0]
        font = self.font()
        font.setFamily(font_family)
        self.setFont(font)

        # Create a "Save" action and add it to the "File" menu
        save_action = QAction('Save', self)
        save_action.setShortcut('Cmd+S')
        save_action.triggered.connect(self.save_note)
        file_menu = self.menuBar().addMenu('File')
        file_menu.addAction(save_action)

        # Show the window
        self.show()

    def save_note(self):
        # Get the file path from the user
        file_path, _ = QFileDialog.getSaveFileName(self, 'Save Note', '', 'Text Files (*.txt)')

        if file_path:
            # Save the text in the QTextEdit widget to the file
            with open(file_path, 'w') as file:
                file.write(self.text_edit.toPlainText())
        file_path, _ = QFileDialog.getSaveFileName(self, 'Save Note', '', 'Text Files (*.txt);;All Files (*)')

if __name__ == '__main__':
    # Create a QApplication instance and show the Notepad window
    app = QApplication(sys.argv)
    notepad = Notepad()
    sys.exit(app.exec_())
