import sys
from PyQt5.QtWidgets import QApplication
from gui.dashboard import Dashboard
from utils.logger import setup_logger
from config import WINDOW_WIDTH, WINDOW_HEIGHT


def main():

    setup_logger()

    app = QApplication(sys.argv)

    from utils.theme_manager import ThemeManager
    theme_manager = ThemeManager(app)

    window = Dashboard(theme_manager)

    window.resize(
        WINDOW_WIDTH,
        WINDOW_HEIGHT,
    )

    window.show()

    sys.exit(
        app.exec_()
    )


if __name__ == "__main__":

    main()