import sys
from PySide6.QtCore import QUrl
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QMainWindow, QApplication, QToolBar, QLineEdit, QStyle
from PySide6.QtWebEngineWidgets import QWebEngineView


class MainWindow(QMainWindow):
    def __init__(self):
        # initialization
        super().__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://ezpython.ir'))

        self.setCentralWidget(self.browser)
        self.showMaximized()

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.go_url)
        self.browser.urlChanged.connect(self.update_url)

        pixmap_back_icon = QStyle.StandardPixmap.SP_ArrowBack
        back_icon = self.style().standardIcon(pixmap_back_icon)
        back_button = QAction(back_icon, 'Back', self)
        back_button.triggered.connect(self.browser.back)

        pixmap_forward_icon = QStyle.StandardPixmap.SP_ArrowForward
        forward_icon = self.style().standardIcon(pixmap_forward_icon)
        forward_button = QAction(forward_icon, 'Forward', self)
        forward_button.triggered.connect(self.browser.forward)

        pixmap_reload_icon = QStyle.StandardPixmap.SP_BrowserReload
        reload_icon = self.style().standardIcon(pixmap_reload_icon)
        reload_button = QAction(reload_icon, 'Reload', self)
        reload_button.triggered.connect(self.browser.reload)

        pixmap_home_icon = QStyle.StandardPixmap.SP_ArrowUp
        home_icon = self.style().standardIcon(pixmap_home_icon)
        home_button = QAction(home_icon, 'Home', self)
        home_button.triggered.connect(self.go_home)

        toolbar = QToolBar()
        toolbar.addActions([back_button, forward_button, reload_button])
        toolbar.addWidget(self.url_bar)
        toolbar.addAction(home_button)
        self.addToolBar(toolbar)

    def go_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self):
        url = self.browser.url()
        self.url_bar.setText(url.toString())

    def go_home(self):
        self.browser.setUrl(QUrl('https://ezpython.ir'))


app = QApplication(sys.argv)
QApplication.setApplicationName('MyBrowser')
window = MainWindow()
app.exec()
