import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QFileDialog, QTreeView, QDialog, QFormLayout, QInputDialog, QWidget
from model import *
from complete import *
import json

COLUMN_WIDTH_SPEC = 200
SCREEN_RESIZE_FACTOR = 2

class Controller:
    def __init__(self, app):
        with open("store.json") as store_f:
            self.store = json.load(store_f)
            self.app = app
            self.view = None

    def show_search(self):
        self.search = SearchWindow(self.store)
        self.search.switch_window.connect(self.show_store)
        self.search.show()

    def show_store(self, query):
        self.search.close()
        self.view = TreeView()
        model = QJsonModel()
        if query not in self.store:
            return
        self.store = self.store[query]
        model.loadJson(json.dumps(self.store).encode('ascii'))
        self.view.setModel(model)
        self.view.setColumnWidth(0, 5)
        screen = self.app.primaryScreen()
        size = screen.size()
        self.view.resize(size.width() // SCREEN_RESIZE_FACTOR,
                    size.height() // SCREEN_RESIZE_FACTOR)
        self.view.setColumnWidth(0, COLUMN_WIDTH_SPEC)
        self.view.expandAll()
        self.view.show()
