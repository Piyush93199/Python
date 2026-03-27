from PyQt5.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QComboBox,
    QLineEdit,
    QTableWidget,
    QTableWidgetItem,
    QFormLayout,
    QCheckBox,
)

class SplitterPanel(QWidget):

    def __init__(self):

        super().__init__()

        layout = QVBoxLayout()

        layout.addWidget(
            QLabel("Train-Test Split")
        )

        form = QFormLayout()

        self.test_size_input = QLineEdit()

        self.test_size_input.setText("0.2")

        form.addRow(
            "Test Size:",
            self.test_size_input,
        )

        self.shuffle_checkbox = QCheckBox()

        self.shuffle_checkbox.setChecked(True)

        form.addRow(
            "Shuffle:",
            self.shuffle_checkbox,
        )

        self.seed_input = QLineEdit()

        self.seed_input.setText("42")

        form.addRow(
            "Random Seed:",
            self.seed_input,
        )

        layout.addLayout(form)

        self.split_button = QPushButton(
            "Split Data"
        )

        layout.addWidget(
            self.split_button
        )

        layout.addStretch()

        self.setLayout(layout)

class OutlierPanel(QWidget):

    def __init__(self):

        super().__init__()

        layout = QVBoxLayout()

        layout.addWidget(
            QLabel("Outlier Detection")
        )

        form = QFormLayout()

        self.column_box = QComboBox()

        form.addRow(
            "Column:",
            self.column_box,
        )

        self.method_box = QComboBox()

        self.method_box.addItems(
            [
                "IQR",
                "Z-Score",
            ]
        )

        form.addRow(
            "Method:",
            self.method_box,
        )

        self.threshold_input = QLineEdit()

        self.threshold_input.setText(
            "3.0"
        )

        form.addRow(
            "Threshold:",
            self.threshold_input,
        )

        layout.addLayout(form)

        self.detect_button = QPushButton(
            "Detect Outliers"
        )

        layout.addWidget(
            self.detect_button
        )

        layout.addStretch()

        self.setLayout(layout)

        self.remove_button = QPushButton(
            "Remove Outliers"
        )

        layout.addWidget(
            self.remove_button
        )

    def set_columns(self, columns):

        self.column_box.clear()

        self.column_box.addItems(columns)

class ScalerPanel(QWidget):

    def __init__(self):

        super().__init__()

        layout = QVBoxLayout()

        layout.addWidget(
            QLabel("Feature Scaling")
        )

        form = QFormLayout()

        self.column_box = QComboBox()

        form.addRow(
            "Column:",
            self.column_box,
        )

        self.method_box = QComboBox()

        self.method_box.addItems(
            [
                "min_max",
                "standardize",
            ]
        )

        form.addRow(
            "Method:",
            self.method_box,
        )

        layout.addLayout(form)

        self.apply_button = QPushButton(
            "Apply Scaling"
        )

        layout.addWidget(
            self.apply_button
        )

        layout.addStretch()

        self.setLayout(layout)

    def set_columns(self, columns):

        self.column_box.clear()

        self.column_box.addItems(columns)


class SummaryPanel(QWidget):

    def __init__(self):

        super().__init__()

        layout = QVBoxLayout()

        # ---- Dataset Info ----

        layout.addWidget(QLabel("Dataset Info"))

        self.info_table = QTableWidget()

        layout.addWidget(self.info_table)

        # ---- Missing Values ----

        layout.addWidget(QLabel("Missing Values"))

        self.missing_table = QTableWidget()

        layout.addWidget(self.missing_table)

        # ---- Data Types ----

        layout.addWidget(QLabel("Data Types"))

        self.dtype_table = QTableWidget()

        layout.addWidget(self.dtype_table)

        # ---- Statistics ----

        layout.addWidget(QLabel("Statistics"))

        self.stats_table = QTableWidget()

        self.stats_table.setMinimumHeight(200)
        self.stats_table.setMaximumHeight(300)

        layout.addWidget(self.stats_table)

        layout.addStretch()

        self.setLayout(layout)

    # -------------------------

    def update_summary(
        self,
        rows,
        cols,
        missing,
        dtypes,
        stats,
    ):

        # ---- Dataset Info ----

        self.info_table.setRowCount(2)
        self.info_table.setColumnCount(2)

        self.info_table.setHorizontalHeaderLabels(
            ["Metric", "Value"]
        )

        self.info_table.setItem(
            0,
            0,
            QTableWidgetItem("Rows"),
        )

        self.info_table.setItem(
            0,
            1,
            QTableWidgetItem(str(rows)),
        )

        self.info_table.setItem(
            1,
            0,
            QTableWidgetItem("Columns"),
        )

        self.info_table.setItem(
            1,
            1,
            QTableWidgetItem(str(cols)),
        )

        # ---- Missing Values ----

        self._load_series_table(
            self.missing_table,
            missing,
        )

        # ---- Data Types ----

        self._load_series_table(
            self.dtype_table,
            dtypes,
        )

        # ---- Statistics ----

        self._load_dataframe_table(
            self.stats_table,
            stats,
        )

    # -------------------------

    def _load_series_table(
        self,
        table,
        series,
    ):

        table.setRowCount(len(series))
        table.setColumnCount(2)

        table.setHorizontalHeaderLabels(
            ["Column", "Value"]
        )

        for row, (col, val) in enumerate(
            series.items()
        ):

            table.setItem(
                row,
                0,
                QTableWidgetItem(str(col)),
            )

            table.setItem(
                row,
                1,
                QTableWidgetItem(str(val)),
            )

        table.resizeColumnsToContents()

    # -------------------------

    def _load_dataframe_table(
        self,
        table,
        df,
    ):

        table.setRowCount(len(df.index))
        table.setColumnCount(len(df.columns))

        # Column headers
        table.setHorizontalHeaderLabels(
            df.columns.astype(str)
        )

        # ADD THIS — row labels
        table.setVerticalHeaderLabels(
            df.index.astype(str)
        )

        for i in range(len(df.index)):

            for j in range(len(df.columns)):

                value = df.iloc[i, j]

                table.setItem(
                    i,
                    j,
                    QTableWidgetItem(str(value)),
                )

        table.resizeColumnsToContents()


class ImputerPanel(QWidget):

    def __init__(self):

        super().__init__()

        layout = QVBoxLayout()

        layout.addWidget(QLabel("Missing Value Imputer"))

        self.column_box = QComboBox()

        layout.addWidget(self.column_box)

        self.strategy_box = QComboBox()

        self.strategy_box.addItems(
            [
                "mean",
                "median",
                "mode",
                "constant",
            ]
        )

        layout.addWidget(self.strategy_box)

        self.constant_input = QLineEdit()

        self.constant_input.setPlaceholderText(
            "Constant value (if selected)"
        )

        layout.addWidget(self.constant_input)

        self.apply_button = QPushButton("Apply")

        layout.addWidget(self.apply_button)

        layout.addStretch()

        self.setLayout(layout)

    def set_columns(self, columns):

        self.column_box.clear()

        self.column_box.addItems(columns)

class EncoderPanel(QWidget):

    def __init__(self):

        super().__init__()

        layout = QVBoxLayout()

        layout.addWidget(
            QLabel("Categorical Encoder")
        )

        self.column_box = QComboBox()

        layout.addWidget(
            self.column_box
        )

        self.encoding_box = QComboBox()

        self.encoding_box.addItems(
            [
                "label",
                "one_hot",
            ]
        )

        layout.addWidget(
            self.encoding_box
        )

        self.apply_button = QPushButton(
            "Apply Encoding"
        )

        layout.addWidget(
            self.apply_button
        )

        layout.addStretch()

        self.setLayout(layout)

    def set_columns(self, columns):

        self.column_box.clear()

        self.column_box.addItems(columns)