from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QComboBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

import pandas as pd 
import matplotlib.pyplot as plt 
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class SimpleDashboard(QWidget):

    def __init__(self, root):
        super().__init__()

        self.setWindowTitle("Simple Data Dashboard")
        self.setGeometry(100, 100, 1000, 600)

        self.df = pd.read_csv("titanic.csv")

        self.initUI()

    def initUI(self):
        main_layout = QVBoxLayout()
        control_layout = QHBoxLayout()

        self.column_dropdown = QComboBox()
        numeric_columns = self.df.select_dtypes(include='number').columns.tolist()
        self.column_dropdown.addItems(numeric_columns)
        control_layout.addWidget(QLabel("Select Column:"))
        control_layout.addWidget(self.column_dropdown)

        plot_button = QPushButton("Plot Histogram")
        plot_button.clicked.connect(self.plot_histogram)
        control_layout.addWidget(self.column_dropdown)

        main_layout.addLayout(control_layout)

    def plot_histogram(self):
        pass