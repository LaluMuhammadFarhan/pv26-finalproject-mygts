"""
MyGTS - My Gangsar Treasure System
Aplikasi manajemen inventaris sanggar berbasis PySide6 + Supabase
"""

import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Qt

# from ui.main_window import MainWindow  # uncomment setelah MainWindow dibuat


def main():
    app = QApplication(sys.argv)
    app.setApplicationName("MyGTS")
    app.setApplicationDisplayName("My Gangsar Treasure System")
    app.setOrganizationName("Gangsar Sanggar")

    # Load global stylesheet
    # with open("assets/qss/style.qss", "r") as f:
    #     app.setStyleSheet(f.read())

    # window = MainWindow()
    # window.show()

    print("MyGTS started successfully.")
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
