from PyQt5.QtWidgets import QStatusBar


class StatusBar(QStatusBar):

    def show_message(self, message, timeout=5000):

        self.showMessage(message, timeout)