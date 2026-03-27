from PyQt5.QtWidgets import QStackedWidget, QGraphicsOpacityEffect
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve

class AnimatedStackedWidget(QStackedWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

    def setCurrentIndex(self, index):
        if self.currentIndex() == index:
            return

        # Prepare the incoming widget for a fade-in animation
        incoming_widget = self.widget(index)
        
        # Add opacity effect securely
        self.effect = QGraphicsOpacityEffect(incoming_widget)
        incoming_widget.setGraphicsEffect(self.effect)

        # Configure the fluid animation loop
        self.animation = QPropertyAnimation(self.effect, b"opacity")
        self.animation.setDuration(400)  # 400ms is perfectly smooth for page flips
        self.animation.setStartValue(0.0)
        self.animation.setEndValue(1.0)
        self.animation.setEasingCurve(QEasingCurve.InOutQuad)
        
        # Swap the widget index rapidly and run the animation
        super().setCurrentIndex(index)
        self.animation.start()
