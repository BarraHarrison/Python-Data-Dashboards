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
        self.setWindowTitle("Titanic Advanced Dashboard")
        self.setGeometry(100, 100, 900, 600)

        layout = QVBoxLayout()
        self.tabs = QTabWidget()

        self.overview_tab = QWidget()
        self.survival_tab = QWidget()

        self.tabs.addTab(self.overview_tab, "Overview")
        self.tabs.addTab(self.survival_tab, "Survival Stats")

        self.init_overview_tab()
        self.init_survival_tab()

        layout.addWidget(self.tabs)
        self.setLayout(layout)

    def init_overview_tab(self):
        layout = QVBoxLayout()

        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.figure)
        layout.addWidget(self.canvas)

        self.ax.hist(self.df["Age"].dropna(), bins=30, color='skyblue')
        self.ax.set_title("Age Distribution")
        self.ax.set_xlabel("Age")
        self.ax.set_ylabel("Count")
        self.canvas.draw()

        self.overview_tab.setLayout(layout)

    def init_survival_tab(self):
        layout = QVBoxLayout()

        self.column_dropdown = QComboBox()
        self.column_dropdown.addItems(["Pclass", "Sex", "Embarked"])
        layout.addWidget(QLabel("Select Column:"))
        layout.addWidget(self.column_dropdown)

        plot_button = QPushButton("Show Survival Breakdown")
        plot_button.clicked.connect(self.update_survival_chart)
        layout.addWidget(plot_button)

        self.figure2, self.ax2 = plt.subplots()
        self.canvas2 = FigureCanvas(self.figure2)
        layout.addWidget(self.canvas2)

        self.survival_tab.setLayout(layout)

    def update_survival_chart(self):
        pass