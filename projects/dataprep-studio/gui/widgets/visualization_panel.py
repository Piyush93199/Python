from PyQt5.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QFormLayout,
    QLabel,
    QPushButton,
    QComboBox,
    QHBoxLayout,
)
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

from visualization.plots import (
    plot_histogram,
    plot_boxplot,
    plot_correlation_heatmap,
)


class VisualizationPanel(QWidget):

    def __init__(self):

        super().__init__()

        layout = QVBoxLayout()

        title = QLabel("Data Visualization")

        layout.addWidget(title)

        form = QFormLayout()

        self.column_box = QComboBox()

        form.addRow(
            "Column:",
            self.column_box,
        )

        self.plot_type_box = QComboBox()

        self.plot_type_box.addItems(
            [
                "Histogram",
                "Boxplot",
                "Correlation Heatmap",
            ]
        )

        form.addRow(
            "Plot Type:",
            self.plot_type_box,
        )

        layout.addLayout(form)

        self.plot_button = QPushButton(
            "Generate Plot"
        )

        layout.addWidget(
            self.plot_button
        )

        history_layout = QHBoxLayout()
        history_layout.addWidget(QLabel("Plot History:"))
        self.history_box = QComboBox()
        history_layout.addWidget(self.history_box)
        layout.addLayout(history_layout)

        self.save_button = QPushButton(
            "Save Selected Plot as PNG"
        )

        layout.addWidget(
            self.save_button
        )

        self.canvas_container = QVBoxLayout()
        self.canvas = None
        layout.addLayout(self.canvas_container)
        
        # Add a stretch to push everything up if the canvas is small
        layout.addStretch()

        self.setLayout(layout)

    def set_columns(self, columns):

        self.column_box.clear()

        self.column_box.addItems(columns)

    def set_canvas(self, fig):
        if self.canvas is not None:
            self.canvas_container.removeWidget(self.canvas)
            self.canvas.deleteLater()

        self.canvas = FigureCanvas(fig)
        self.canvas_container.addWidget(self.canvas)
        self.canvas.draw()