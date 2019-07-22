# 2017 by Gregor Engberding , MIT License

import sys
from PyQt5.QtWidgets import QApplication
from controller import *
import json

def main():
    app = QApplication(sys.argv)
    controller = Controller(app)
    controller.show_search()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
