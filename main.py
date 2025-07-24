import sys
import pandas as pd
from PyQt5.QtWidgets import QApplication
from dashboard import TitanicDashboard

if __name__ == "__main__":
    df = pd.read_csv("data/train.csv")
    app = QApplication(sys.argv)
    window = TitanicDashboard(df)
    window.show()
    sys.exit(app.exec_())