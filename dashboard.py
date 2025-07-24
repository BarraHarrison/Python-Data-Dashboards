import sys
import pandas as pd
from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, 
                             QComboBox, QPushButton, QApplication, QTabWidget)
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt

class TitanicDashboard(QWidget):
    def __init__(self, df):
        super().__init__()
        self.df = df
        self.initUI()

    def initUI(self):
        pass

    def init_overview_tab(self):
        pass

    def init_survival_tab(self):
        pass

    def update_survival_chart(self):
        pass