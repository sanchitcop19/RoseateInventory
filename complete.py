from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys


class SearchWindow(QWidget):

    switch_window = pyqtSignal(str)

    def __init__(self, store):
        QWidget.__init__(self)
        layout = QGridLayout()
        self.setLayout(layout)
        self.layout = layout
        self.spec_depth = 0
        self.store = store
        completer = QCompleter([spec for spec in store])
        completer.setCaseSensitivity(Qt.CaseInsensitive)

        self.lineedit = LineEdit(parent = self, comp=completer)
        self.lineedit.setCompleter(completer)
        self.lineedit.returnPressed.connect(self.search)
        layout.addWidget(self.lineedit)

    def search(self):
        self.switch_window.emit(self.lineedit.text())


class LineEdit(QLineEdit):
    tabPressed = pyqtSignal()

    def __init__(self, parent=None, comp=None):
        super().__init__(parent)
        self._compl = comp
        self.tabPressed.connect(self.next_completion)

    def next_completion(self):
        index = self._compl.currentIndex()
        self._compl.popup().setCurrentIndex(index)
        start = self._compl.currentRow()
        if not self._compl.setCurrentRow(start + 1):
            self._compl.setCurrentRow(0)

    def event(self, event):
        if event.type() == QEvent.KeyPress and event.key() == Qt.Key_Tab:
            self.tabPressed.emit()
            return True
        return super().event(event)

