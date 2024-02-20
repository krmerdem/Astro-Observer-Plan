from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QLabel, QWidget, QColorDialog
from PySide6.QtGui import QImage, QPixmap
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import sys

class MatplotlibWidget(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MatplotlibWidget, self).__init__(fig)
        self.setParent(parent)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.central_widget = MatplotlibWidget(self)
        self.setCentralWidget(self.central_widget)

        self.color_button = QPushButton("Choose Color", self)
        self.color_button.clicked.connect(self.choose_color)

        layout = QVBoxLayout()
        layout.addWidget(self.color_button)
        layout.addWidget(self.central_widget)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def choose_color(self):
        color_dialog = QColorDialog(self)
        color = color_dialog.getColor()

        if color.isValid():
            # Use the selected color for plotting or other purposes
            print(f"Selected color: {color.name()}")
            self.central_widget.axes.plot([0, 1, 2, 3, 4], [0, 3, 1, 2, 5], color=color.name())
            self.central_widget.draw()

def run_app():
    app = QApplication(sys.argv)
    main_win = MainWindow()
    app.setStyle('fusion')
    main_win.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    run_app()
