from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

import pandas as pd 
import matplotlib.pyplot as plt 
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class SimpleDashboard:

    def __init__(self, root):
        self.root = root

        self.root.title("Simple Data Dashboard")
        self.root.geometry("1000x600")

        df = pd.read_csv("titanic.csv")