from PyQt5.QtWidgets import QLabel, QGraphicsOpacityEffect
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve, QTimer, Qt

class AnimatedMessageLabel(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setVisible(False)
        self.setAlignment(Qt.AlignCenter)
        
        # Setup opacity effect
        self.effect = QGraphicsOpacityEffect(self)
        self.setGraphicsEffect(self.effect)
        
        # Setup animation
        self.animation = QPropertyAnimation(self.effect, b"opacity")
        self.animation.setDuration(400)
        self.animation.setEasingCurve(QEasingCurve.OutQuad)

    def show_animated_message(self, message, msg_type="success"):
        colors = {
            "success": "#2ecc71",
            "error": "#e74c3c",
            "warning": "#f39c12",
            "info": "#3498db"
        }
        
        color = colors.get(msg_type, "#2ecc71")
        self.setStyleSheet(f"""
            background-color: {color};
            color: white;
            font-weight: bold;
            padding: 8px;
            border-radius: 4px;
            font-size: 14px;
        """)
        self.setText(message)
        
        # Stop any ongoing animation to prevent conflicts
        if self.animation.state() == QPropertyAnimation.Running:
            self.animation.stop()
            try:
                self.animation.finished.disconnect(self._on_hide_finished)
            except TypeError:
                pass
                
        # Animate IN
        self.setVisible(True)
        self.effect.setOpacity(0.0)
        self.animation.setStartValue(0.0)
        self.animation.setEndValue(1.0)
        self.animation.start()
        
        # Schedule animate OUT
        QTimer.singleShot(3000, self.hide_message)

    def hide_message(self):
        if self.animation.state() == QPropertyAnimation.Running:
            self.animation.stop()
            
        self.animation.setStartValue(self.effect.opacity())
        self.animation.setEndValue(0.0)
        self.animation.finished.connect(self._on_hide_finished)
        self.animation.start()

    def _on_hide_finished(self):
        self.setVisible(False)
        try:
            self.animation.finished.disconnect(self._on_hide_finished)
        except TypeError:
            pass
