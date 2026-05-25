"""
UI: MainWindow
Window utama — mengelola QStackedWidget untuk navigasi antar halaman.
Dibuat oleh: Orang 1 (View Layer)
"""
# from PySide6.QtWidgets import QMainWindow, QStackedWidget, QStatusBar
# from PySide6.QtGui import QAction

# TODO: Import semua halaman setelah dibuat
# from ui.pages.login_page import LoginPage
# from ui.pages.dashboard_customer import DashboardCustomer
# from ui.pages.dashboard_owner import DashboardOwner
# from ui.pages.inventory_page import InventoryPage
# from ui.pages.rental_page import RentalPage
# from ui.pages.history_page import HistoryPage

MEMBER_NAMES = [
    "Nama1 — NIM1",
    "Nama2 — NIM2",
    "Nama3 — NIM3",
]

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("MyGTS — My Gangsar Treasure System")
#         self.setMinimumSize(1100, 700)
#         self._build_menu_bar()
#         self._build_status_bar()
#         self._build_stack()
#
#     def _build_menu_bar(self):
#         menu = self.menuBar()
#         file_menu = menu.addMenu("File")
#         file_menu.addAction(QAction("Exit", self, triggered=self.close))
#         help_menu = menu.addMenu("Help")
#         help_menu.addAction(QAction("Tentang MyGTS", self))
#
#     def _build_status_bar(self):
#         status = QStatusBar()
#         status.showMessage("  |  ".join(MEMBER_NAMES))
#         status.setStyleSheet("font-size: 11px; color: #555;")
#         self.setStatusBar(status)
#
#     def _build_stack(self):
#         self.stack = QStackedWidget()
#         self.setCentralWidget(self.stack)
