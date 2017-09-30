from PyQt5.QtWidgets import QMainWindow
from window_editaccount import Ui_EditAccount

class TMail_EditAccount(QMainWindow):

    def __init__(self, parent=None):
        super().__init__()
        self.ui = Ui_EditAccount()
        self.ui.setupUi(self)
        self.ui.actionClose.triggered.connect(self.close)