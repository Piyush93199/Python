from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QHeaderView


class TableWidget(QTableWidget):

    def load_dataframe(self, df):

        self.setRowCount(df.shape[0])
        self.setColumnCount(df.shape[1])

        self.setHorizontalHeaderLabels(df.columns)

        for row in range(df.shape[0]):

            for col in range(df.shape[1]):

                value = str(df.iat[row, col])

                item = QTableWidgetItem(value)

                self.setItem(row, col, item)

                self.horizontalHeader().setSectionResizeMode(
                    QHeaderView.Stretch
                )