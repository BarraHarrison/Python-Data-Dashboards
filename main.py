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

        self.df = pd.read_csv("titanic/gender_submission.csv")

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

        survival_button = QPushButton("Show Survival Count")
        survival_button.clicked.connect(self.update_chart)
        control_layout.addWidget(survival_button)

        main_layout.addLayout(control_layout)

        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.figure)
        main_layout.addWidget(self.canvas)

        self.setLayout(main_layout)

    def plot_histogram(self):
        column = self.column_dropdown.currentText()
        self.ax.clear()
        self.df[column].dropna().hist(ax=self.ax, bins=20)
        self.ax.set_title(f"Histogram of {column}")
        self.canvas.draw()


    def update_chart(self):
        self.ax.clear()
        survival_counts = self.df['Survived'].value_counts().sort_index()
        self.ax.bar(['Did Not Survive', 'Survived'], survival_counts)
        self.ax.set_title("Titanic Survival Counts")
        self.ax.set_ylabel("Number of Passengers")
        self.canvas.draw()


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = SimpleDashboard()
    window.show()
    sys.exit(app.exec_())