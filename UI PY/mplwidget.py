from PySide6.QtWidgets import*

from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

from matplotlib.figure import Figure
import matplotlib.ticker as ticker
import matplotlib.dates as mdates
import matplotlib.style as style

class MplWidget(QWidget):
    
    def __init__(self, parent = None):

        QWidget.__init__(self, parent)
        self.canvas = FigureCanvas(Figure(tight_layout=True))
        self.toolbar = NavigationToolbar(self.canvas, self)
        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.toolbar)
        vertical_layout.addWidget(self.canvas)
        
        self.canvas.axes = self.canvas.figure.add_subplot(111)
        self.setLayout(vertical_layout)
        
        # self.canvas.axes.grid(True, color='gray')
        # self.canvas.axes.grid()
        # self.canvas.axes.invert_yaxis()
        self.canvas.axes.set_xlim(0, 2.05)
        self.canvas.axes.set_ylim(0, 90)
        self.canvas.axes.set_xlabel('Universal Time Coordinated (UTC)')
        self.canvas.axes.set_ylabel('Altitude ($^\circ$)')
        # self.canvas.figure.set_facecolor("#FAFAFA")
        # self.canvas.axes.set_facecolor("#FAFAFA")
        self.canvas._draw_border = True
        
        

        