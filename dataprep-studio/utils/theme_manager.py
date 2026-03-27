from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtCore import Qt
import matplotlib.pyplot as plt

class ThemeManager:
    def __init__(self, app):
        self.app = app
        self.is_dark = True
        self.app.setStyle("Fusion")
        self.apply_dark_theme()

    def toggle_theme(self):
        self.is_dark = not self.is_dark
        if self.is_dark:
            self.apply_dark_theme()
        else:
            self.apply_light_theme()

    def apply_dark_theme(self):
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(13, 17, 23))      
        palette.setColor(QPalette.WindowText, QColor(201, 209, 217))
        palette.setColor(QPalette.Base, QColor(9, 12, 16))         
        palette.setColor(QPalette.AlternateBase, QColor(22, 27, 34))
        palette.setColor(QPalette.ToolTipBase, QColor(13, 17, 23))
        palette.setColor(QPalette.ToolTipText, QColor(201, 209, 217))
        palette.setColor(QPalette.Text, QColor(201, 209, 217))
        palette.setColor(QPalette.Button, QColor(33, 38, 45))
        palette.setColor(QPalette.ButtonText, Qt.white)
        palette.setColor(QPalette.BrightText, QColor(255, 123, 114))
        palette.setColor(QPalette.Link, QColor(88, 166, 255))
        palette.setColor(QPalette.Highlight, QColor(31, 111, 235))
        palette.setColor(QPalette.HighlightedText, Qt.white)
        self.app.setPalette(palette)
        
        self.app.setStyleSheet("""
            QMainWindow, QSplitter {
                background-color: #0d1117;
            }
            QWidget {
                font-family: 'Segoe UI', 'Inter', 'Roboto', sans-serif;
            }
            QLabel {
                color: #c9d1d9;
                font-size: 14px;
                font-weight: 500;
            }
            QPushButton {
                background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #1f6feb, stop:1 #388bfd);
                border: none;
                color: #ffffff;
                font-weight: bold;
                font-size: 14px;
                padding: 10px 20px;
                border-radius: 8px;
            }
            QPushButton:hover {
                background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #388bfd, stop:1 #58a6ff);
            }
            QPushButton:pressed {
                background-color: #1f6feb;
            }
            QLineEdit, QComboBox, QSpinBox, QDoubleSpinBox {
                background-color: rgba(255, 255, 255, 0.05);
                border: 1px solid rgba(255, 255, 255, 0.1);
                color: #c9d1d9;
                padding: 10px;
                border-radius: 8px;
                font-size: 14px;
            }
            QLineEdit:focus, QComboBox:focus, QSpinBox:focus {
                border: 1px solid #58a6ff;
                background-color: rgba(255, 255, 255, 0.08);
            }
            QComboBox::drop-down { border: none; }
            QComboBox QAbstractItemView {
                background-color: #161b22;
                color: #c9d1d9;
                selection-background-color: #1f6feb;
                border-radius: 8px;
            }
            QTableWidget {
                background-color: #0d1117;
                gridline-color: rgba(255, 255, 255, 0.05);
                color: #c9d1d9;
                border: 1px solid rgba(255, 255, 255, 0.1);
                border-radius: 10px;
                font-size: 13px;
            }
            QHeaderView::section {
                background-color: #161b22;
                color: #8b949e;
                padding: 10px;
                font-weight: 700;
                border: none;
                border-right: 1px solid rgba(255, 255, 255, 0.05);
                border-bottom: 1px solid rgba(255, 255, 255, 0.05);
            }
            QTableCornerButton::section { background-color: #161b22; }
            
            QListWidget#Sidebar {
                background-color: transparent;
                border: none;
                border-right: 1px solid rgba(255, 255, 255, 0.1);
                outline: none;
                padding: 15px 10px;
            }
            QListWidget#Sidebar::item {
                padding: 12px 20px;
                color: #8b949e;
                font-size: 15px;
                font-weight: 600;
                border-radius: 8px;
                margin: 4px 0px;
            }
            QListWidget#Sidebar::item:hover {
                background-color: rgba(255, 255, 255, 0.05);
                color: #c9d1d9;
            }
            QListWidget#Sidebar::item:selected {
                background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #1f6feb, stop:1 #388bfd);
                color: #ffffff;
                font-weight: bold;
                border-left: 5px solid #79c0ff;
            }
            
            QSplitter::handle {
                background-color: rgba(255, 255, 255, 0.05);
                margin: 2px;
            }
        """)

        plt.style.use('dark_background')
        plt.rcParams['figure.facecolor'] = '#0d1117'
        plt.rcParams['axes.facecolor'] = '#161b22'
        plt.rcParams['savefig.facecolor'] = '#0d1117'
        plt.rcParams['text.color'] = '#c9d1d9'
        plt.rcParams['axes.labelcolor'] = '#c9d1d9'
        plt.rcParams['xtick.color'] = '#8b949e'
        plt.rcParams['ytick.color'] = '#8b949e'
        plt.rcParams['grid.color'] = '#30363d'
        plt.rcParams['axes.edgecolor'] = '#30363d'
        plt.rcParams['font.family'] = 'sans-serif'

    def apply_light_theme(self):
        palette = self.app.style().standardPalette()
        self.app.setPalette(palette)
        
        self.app.setStyleSheet("""
            QPushButton { border-radius: 4px; padding: 6px; border: 1px solid #ccc; background-color: #f0f0f0; color: black;}
            QPushButton:hover { background-color: #e0e0e0; }
            QPushButton:pressed { background-color: #d0d0d0; }
            
            QListWidget#Sidebar {
                background-color: #f7f7f7;
                border: none;
                border-right: 1px solid #ddd;
                outline: none;
                padding-top: 5px;
            }
            QListWidget#Sidebar::item {
                padding: 10px 15px;
                color: #333333;
                font-size: 14px;
                border-radius: 6px;
                margin: 2px 8px;
            }
            QListWidget#Sidebar::item:hover {
                background-color: #e6e6e6;
            }
            QListWidget#Sidebar::item:selected {
                background-color: #0078d7;
                color: #ffffff;
                font-weight: bold;
            }
        """)
        
        plt.style.use('default')
        plt.rcParams['figure.facecolor'] = 'white'
        plt.rcParams['axes.facecolor'] = 'white'
        plt.rcParams['savefig.facecolor'] = 'white'
