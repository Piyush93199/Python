from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtCore import Qt
import matplotlib.pyplot as plt

class ThemeManager:
    def __init__(self, app):
        self.app = app
        self.is_dark = False
        self.app.setStyle("Fusion")
        self.apply_light_theme()



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
