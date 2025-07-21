from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QComboBox
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
        pass

    def plot_histogram(self):
        pass