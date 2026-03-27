from PyQt5.QtGui import QColor


COLORS = {
    "outlier": QColor(255, 150, 150),
    "normal": QColor(255, 255, 255),
}


def highlight_rows(
    table,
    mask,
    color_key,
):

    color = COLORS[color_key]

    for row in range(len(mask)):

        for col in range(
            table.columnCount()
        ):

            item = table.item(
                row,
                col
            )

            if not item:
                continue

            if mask.iloc[row]:

                item.setBackground(color)

            else:

                item.setBackground(
                    COLORS["normal"]
                )