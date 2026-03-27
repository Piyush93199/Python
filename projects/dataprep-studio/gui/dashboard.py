from PyQt5.QtWidgets import (
    QMainWindow,
    QPushButton,
    QFileDialog,
    QVBoxLayout,
    QWidget,
    QLabel,
    QMessageBox,
    QSplitter,
    QFileDialog,
    QHBoxLayout,
    QListWidget,
)

from gui.widgets.animated_stack import AnimatedStackedWidget
from gui.widgets.animated_label import AnimatedMessageLabel

from gui.widgets.control_panel import (
    SummaryPanel,
    ImputerPanel,
    EncoderPanel,
    ScalerPanel,
    OutlierPanel,
    SplitterPanel,
)

from core.data_explorer import (
    get_shape,
    get_missing_values,
    get_data_types,
    get_basic_statistics,
)

from core.imputer import (
    mean_impute,
    median_impute,
    mode_impute,
    constant_impute,
)

from core.encoder import (
    label_encode,
    one_hot_encode,
)

from core.scaler import (
    min_max_scale,
    standardize,
)

from core.outlier import (
    detect_outliers_iqr,
    detect_outliers_zscore,
)

from visualization.plots import (
    plot_histogram,
    plot_boxplot,
    plot_correlation_heatmap,
)

from core.exporter import save_dataset
from gui.widgets.control_panel import ImputerPanel
from core.outlier import detect_outliers_iqr
from core.loader import load_csv
from gui.widgets.table_widget import TableWidget
from core.data_explorer import get_shape
from gui.widgets.control_panel import SummaryPanel
import pandas as pd
from gui.status_bar import StatusBar
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QTimer
from utils.table_highlighter import highlight_rows
from core.splitter import train_test_split_custom
from gui.widgets.visualization_panel import VisualizationPanel

class Dashboard(QMainWindow):

    def __init__(self, theme_manager=None):

        super().__init__()

        self.theme_manager = theme_manager

        self.setWindowTitle("DataPrep Studio")

        self.dataframe = None

        self.history = []

        self.current_plot_fig = None

        self.generated_plots = {}

        self.init_ui()

        self.scaled_columns = set()

    def init_ui(self):

        layout = QVBoxLayout()

        # ---- FILE INFO ----

        top_bar = QHBoxLayout()
        top_bar.setContentsMargins(15, 10, 15, 10)
        top_bar.setSpacing(15)

        self.label = QLabel("No file loaded")
        self.label.setStyleSheet("font-weight: 700; color: #8b949e; font-size: 14px;")
        top_bar.addWidget(self.label)

        top_bar.addStretch()

        self.load_button = QPushButton("Load CSV")
        self.load_button.setFixedWidth(150)
        self.load_button.clicked.connect(self.open_file)
        top_bar.addWidget(self.load_button)

        self.undo_button = QPushButton("Undo")
        self.undo_button.setFixedWidth(120)
        self.undo_button.clicked.connect(self.undo_last_action)
        top_bar.addWidget(self.undo_button)



        layout.addLayout(top_bar)

        # ---- MESSAGE BANNER ----
        self.message_label = AnimatedMessageLabel()
        layout.addWidget(self.message_label)

        # ---- TABLE ----

        self.table = TableWidget()

        # ---- MODERN SIDEBAR NAVIGATION ----
        self.bottom_pane = QWidget()
        bottom_layout = QHBoxLayout(self.bottom_pane)
        bottom_layout.setContentsMargins(0, 0, 0, 0)

        self.sidebar = QListWidget()
        self.sidebar.setFixedWidth(220)
        self.sidebar.setObjectName("Sidebar")

        self.stacked_widget = AnimatedStackedWidget()

        bottom_layout.addWidget(self.sidebar)
        bottom_layout.addWidget(self.stacked_widget)

        # ---- RESIZABLE SPLITTER ----
        self.splitter = QSplitter(Qt.Vertical)
        self.splitter.addWidget(self.table)
        self.splitter.addWidget(self.bottom_pane)

        # Initial size ratio
        self.splitter.setSizes([500, 300])
        self.splitter.setHandleWidth(8)

        layout.addWidget(self.splitter)

        # Create panels

        self.summary_panel = SummaryPanel()

        self.imputer_panel = ImputerPanel()

        self.encoder_panel = EncoderPanel()
        self.scaler_panel = ScalerPanel()
        self.outlier_panel = OutlierPanel()
        self.splitter_panel = SplitterPanel()
        self.visualization_panel = VisualizationPanel()

        # Add panels to Stack and Sidebar
        panels = [
            ("Summary Overview", self.summary_panel),
            ("Missing Value Imputer", self.imputer_panel),
            ("Categorical Encoder", self.encoder_panel),
            ("Feature Scaling", self.scaler_panel),
            ("Outlier Detection", self.outlier_panel),
            ("Train-Test Split", self.splitter_panel),
            ("Data Visualization", self.visualization_panel)
        ]

        for name, panel in panels:
            self.sidebar.addItem(name)
            self.stacked_widget.addWidget(panel)

        self.sidebar.currentRowChanged.connect(self.stacked_widget.setCurrentIndex)
        self.sidebar.setCurrentRow(0)

        # ---- SIGNAL CONNECTIONS ----

        self.imputer_panel.apply_button.clicked.connect(
            self.apply_imputation
        )

        self.imputer_panel.column_box.currentTextChanged.connect(
            self.update_strategy_options
        )

        self.encoder_panel.apply_button.clicked.connect(
            self.apply_encoding
        )

        # ---- CONTAINER ----

        container = QWidget()

        container.setLayout(layout)

        self.setCentralWidget(container)

        # ---- STATUS BAR ----

        self.status_bar = StatusBar()

        self.setStatusBar(self.status_bar)

        self.scaler_panel.apply_button.clicked.connect(
            self.apply_scaling
        )

        self.outlier_panel.detect_button.clicked.connect(
            self.detect_outliers
        )

        self.splitter_panel.split_button.clicked.connect(
            self.split_data
        )

        bottom_bar = QHBoxLayout()
        bottom_bar.addStretch()

        self.save_button = QPushButton("Save Clean Dataset")
        self.save_button.setFixedWidth(250)
        bottom_bar.addWidget(self.save_button)
        self.save_button.clicked.connect(self.save_dataset)

        layout.addLayout(bottom_bar)

        self.visualization_panel.plot_button.clicked.connect(
            self.generate_plot
        )

        self.visualization_panel.save_button.clicked.connect(
            self.save_plot
        )

        self.visualization_panel.history_box.currentTextChanged.connect(
            self.on_plot_history_changed
        )

        self.outlier_panel.remove_button.clicked.connect(
            self.remove_outliers
        )

    def open_file(self):

        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Open CSV",
            "",
            "CSV Files (*.csv)",
        )

        if file_path:

            df = load_csv(file_path)

            if df is not None:

                self.dataframe = df

                self.table.load_dataframe(df)

                self.label.setText(file_path)

                rows, cols = get_shape(df)

                missing = get_missing_values(df)

                dtypes = get_data_types(df)

                stats = get_basic_statistics(df)

                self.summary_panel.update_summary(
                    rows,
                    cols,
                    missing,
                    dtypes,
                    stats,
                )

                self.imputer_panel.set_columns(
                    df.columns.tolist()
                )

                self.encoder_panel.set_columns(
                    df.select_dtypes(
                        include="object"
                    ).columns.tolist()
                )

                self.show_message(
                    "CSV file loaded successfully"
                )

                numeric_columns = df.select_dtypes(
                    include="number"
                ).columns.tolist()

                self.scaler_panel.set_columns(
                    numeric_columns
                )

                numeric_columns = df.select_dtypes(
                    include="number"
                ).columns.tolist()

                self.outlier_panel.set_columns(
                    numeric_columns
                )

                self.visualization_panel.set_columns(
                    self.dataframe.columns.tolist()
                )


    def apply_imputation(self):
    
        if self.dataframe is None:
            return
    
        column = self.imputer_panel.column_box.currentText()

        self.save_state(
            f"Imputed {column}"
        )
    
        strategy = self.imputer_panel.strategy_box.currentText()
    
    
        if strategy == "mean":
    
            self.dataframe = mean_impute(
                self.dataframe,
                column,
            )
    
        elif strategy == "median":
    
            self.dataframe = median_impute(
                self.dataframe,
                column,
            )
    
        elif strategy == "mode":
    
            self.dataframe = mode_impute(
                self.dataframe,
                column,
            )
    
        elif strategy == "constant":
    
            value = self.imputer_panel.constant_input.text()
    
            if value == "":
                return
    
            self.dataframe = constant_impute(
                self.dataframe,
                column,
                value,
            )
    
        self.table.load_dataframe(
            self.dataframe
        )
    
        rows, cols = get_shape(
            self.dataframe
        )
    
        missing = get_missing_values(
            self.dataframe
        )
    
        dtypes = get_data_types(
            self.dataframe
        )
    
        stats = get_basic_statistics(
            self.dataframe
        )
    
        self.summary_panel.update_summary(
            rows,
            cols,
            missing,
            dtypes,
            stats,
        )

        self.show_message(
            f"Missing values imputed in '{column}'"
        )

    def update_strategy_options(self):

        column = self.imputer_panel.column_box.currentText()

        if column == "":
            return

        is_numeric = pd.api.types.is_numeric_dtype(
            self.dataframe[column]
        )

        self.imputer_panel.strategy_box.clear()

        if is_numeric:

            self.imputer_panel.strategy_box.addItems(
                [
                    "mean",
                    "median",
                    "mode",
                    "constant",
                ]
            )

        else:

            self.imputer_panel.strategy_box.addItems(
                [
                    "mode",
                    "constant",
                ]
            )
    
    def apply_encoding(self):

        if self.dataframe is None:
            return

        column = (
            self.encoder_panel
            .column_box
            .currentText()
        )

        self.save_state(
            f"Encoded {column}"
        )

        if column == "":
            return

        if self.dataframe[column].isnull().sum() > 0:

            self.show_message(
                "Impute missing values before encoding",
                "warning"
            )

            QMessageBox.warning(
                self,
                "Missing Values",
                "Impute missing values before encoding",
            )

            return

        method = (
            self.encoder_panel
            .encoding_box
            .currentText()
        )

        if method == "label":

            self.dataframe, mapping = label_encode(
                self.dataframe,
                column,
            )

        elif method == "one_hot":

            self.dataframe = one_hot_encode(
                self.dataframe,
                column,
            )

        self.show_message(
            f"{method} encoding applied to '{column}'"
        )

        self.table.load_dataframe(
            self.dataframe
        )

        rows, cols = get_shape(
            self.dataframe
        )

        missing = get_missing_values(
            self.dataframe
        )

        dtypes = get_data_types(
            self.dataframe
        )

        stats = get_basic_statistics(
            self.dataframe
        )

        self.summary_panel.update_summary(
            rows,
            cols,
            missing,
            dtypes,
            stats,
        )

    def show_message(self, message, msg_type="success"):
        self.message_label.show_animated_message(message, msg_type)

    def apply_scaling(self):

        column = (
            self.scaler_panel
            .column_box
            .currentText()
        )

        self.save_state(
            f"Scaled {column}"
        )

        method = (
            self.scaler_panel
            .method_box
            .currentText()
        )

        if column == "":
            return

        if not pd.api.types.is_numeric_dtype(
            self.dataframe[column]
        ):

            self.show_message(
                "Scaling works only on numeric columns",
                "error"
            )

            return

        if column in self.scaled_columns:

            self.show_message(
                f"{column} is already scaled",
                "warning"
            )

            return

        if self.dataframe is None:
            return

        if method == "min_max":

            self.dataframe = min_max_scale(
                self.dataframe,
                column,
            )

            self.show_message(
                f"Min-Max scaling applied to '{column}'",
                "success"
            )

        elif method == "standardize":

            self.dataframe = standardize(
                self.dataframe,
                column,
            )

            self.show_message(
                f"Standardization applied to '{column}'",
                "success"
            )

        self.scaled_columns.add(column)
        self.table.load_dataframe(
            self.dataframe
        )

        rows, cols = get_shape(
            self.dataframe
        )

        missing = get_missing_values(
            self.dataframe
        )

        dtypes = get_data_types(
            self.dataframe
        )

        stats = get_basic_statistics(
            self.dataframe
        )

        self.summary_panel.update_summary(
            rows,
            cols,
            missing,
            dtypes,
            stats,
        )

        before_mean = self.dataframe[column].mean()
        before_std = self.dataframe[column].std()

        after_mean = self.dataframe[column].mean()
        after_std = self.dataframe[column].std()

        self.show_message(
            f"{column}: mean {before_mean:.2f} → {after_mean:.2f}",
            "info"
        )

    def detect_outliers(self):

        if self.dataframe is None:
            return

        column = (
            self.outlier_panel
            .column_box
            .currentText()
        )

        method = (
            self.outlier_panel
            .method_box
            .currentText()
        )

        threshold = float(
            self.outlier_panel
            .threshold_input
            .text()
        )

        if column == "":
            return

        # ---- choose method ----

        if method == "IQR":

            mask = detect_outliers_iqr(
                self.dataframe,
                column,
            )

        elif method == "Z-Score":

            mask = detect_outliers_zscore(
                self.dataframe,
                column,
                threshold,
            )

        count = mask.sum()

        highlight_rows(
            self.table,
            mask,
            "outlier",
        )

        self.show_message(
            f"{count} outliers detected using {method}",
            "info",
        )

    def split_data(self):

        if self.dataframe is None:
            return

        test_size = float(
            self.splitter_panel
            .test_size_input
            .text()
        )

        shuffle = (
            self.splitter_panel
            .shuffle_checkbox
            .isChecked()
        )

        seed = int(
            self.splitter_panel
            .seed_input
            .text()
        )

        train, test = train_test_split_custom(
            self.dataframe,
            test_size=test_size,
            shuffle=shuffle,
            random_state=seed,
        )

        self.train_df = train

        self.test_df = test

        self.show_message(
            f"Train: {len(train)} rows | Test: {len(test)} rows",
            "info",
        )

    def save_dataset(self):

        if self.dataframe is None:

            self.show_message(
                "No dataset to save",
                "warning",
            )

            return

        file_path, selected_filter = QFileDialog.getSaveFileName(
            self,
            "Save Dataset",
            "dataset.csv",
            "CSV Files (*.csv);;Excel Files (*.xlsx)",
        )

        if not file_path:
            return

        if not file_path.lower().endswith((".csv", ".xlsx")):

            if "CSV" in selected_filter:

                file_path += ".csv"

            elif "Excel" in selected_filter:

                file_path += ".xlsx"

        try:

            save_dataset(
                self.dataframe,
                file_path,
            )

            self.show_message(
                "Dataset saved successfully",
                "success",
            )

        except Exception as e:

            self.show_message(
                str(e),
                "error",
            )

    def generate_plot(self):

        if self.dataframe is None:

            self.show_message(
                "Load dataset first",
                "error",
            )

            return

        column = (
            self.visualization_panel
            .column_box
            .currentText()
        )

        if not column:

            self.show_message(
                "Select a column first",
                "warning",
            )

            return

        if column not in self.dataframe.columns:

            self.show_message(
                "Invalid column selected",
                "error",
            )

            return

        plot_type = (
            self.visualization_panel
            .plot_type_box
            .currentText()
        )

        fig = None
        title = ""

        if plot_type == "Histogram":

            fig = plot_histogram(
                self.dataframe,
                column,
            )
            title = f"Histogram: {column}"

        elif plot_type == "Boxplot":

            fig = plot_boxplot(
                self.dataframe,
                column,
            )
            title = f"Boxplot: {column}"

        elif plot_type == "Correlation Heatmap":

            fig = plot_correlation_heatmap(
                self.dataframe
            )
            title = "Correlation Heatmap"

        if fig:
            base_title = title
            counter = 1
            while title in self.generated_plots:
                title = f"{base_title} ({counter})"
                counter += 1
                
            self.generated_plots[title] = fig
            
            # This triggers currentTextChanged, which safely sets the canvas
            self.visualization_panel.history_box.addItem(title)
            self.visualization_panel.history_box.setCurrentText(title)

    def on_plot_history_changed(self, title):
        if title in self.generated_plots:
            fig = self.generated_plots[title]
            self.current_plot_fig = fig
            self.visualization_panel.set_canvas(fig)

    def save_plot(self):

        if self.current_plot_fig is None:

            self.show_message(
                "No plot generated to save",
                "warning",
            )

            return

        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "Save Plot as PNG",
            "plot.png",
            "PNG Files (*.png)",
        )

        if file_path:

            if not file_path.lower().endswith(".png"):

                file_path += ".png"

            try:

                self.current_plot_fig.savefig(
                    file_path,
                    bbox_inches="tight",
                )

                self.show_message(
                    "Plot saved successfully",
                    "success",
                )

            except Exception as e:

                self.show_message(
                    f"Failed to save plot: {str(e)}",
                    "error",
                )

    def remove_outliers(self):

        if self.dataframe is None:
            return

        column = (
            self.outlier_panel
            .column_box
            .currentText()
        )

        self.save_state(
            f"Removed {removed_count} outliers"
        )

        method = (
            self.outlier_panel
            .method_box
            .currentText()
        )

        threshold = float(
            self.outlier_panel
            .threshold_input
            .text()
        )

        if method == "IQR":

            mask = detect_outliers_iqr(
                self.dataframe,
                column,
            )

        elif method == "Z-Score":

            mask = detect_outliers_zscore(
                self.dataframe,
                column,
                threshold,
            )

        removed_count = mask.sum()

        from core.outlier import remove_outliers

        self.dataframe = remove_outliers(
            self.dataframe,
            mask,
        )

        self.table.load_dataframe(
            self.dataframe
        )

        self.show_message(
            f"{removed_count} rows removed",
            "info",
        )

    def save_state(
        self,
        action_name,
    ):

        if self.dataframe is None:
            return

        snapshot = self.dataframe.copy()

        self.history.append(
            (
                action_name,
                snapshot,
            )
        )

    def undo_last_action(self):

        if not self.history:

            self.show_message(
                "Nothing to undo",
                "warning",
            )

            return

        action_name, previous_df = self.history.pop()

        self.dataframe = previous_df

        self.table.load_dataframe(
        self.dataframe
        )

        self.show_message(
        f"Undid: {action_name}",
        "info",
        )

    def save_state(
        self,
        action_name,
    ):

        if self.dataframe is None:
            return

        snapshot = self.dataframe.copy()

        self.history.append(
            (
                action_name,
                snapshot,
            )
        )