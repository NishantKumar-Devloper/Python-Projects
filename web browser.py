import sys
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QApplication, QLineEdit, QPushButton, QGridLayout, QLabel, QWidget, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QFont, QPixmap

class Browser(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle('Searcher')
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet("background-color: #032B44;")
        # Create a layout for the widgets
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        # Create a label and set its font
        label = QLabel('Searcher')
        label.setFont(QFont('Arial', 48))  # Double the font size
        label.setStyleSheet("color: white;")
        label.setAlignment(Qt.AlignCenter)  # Center the label
        layout.addWidget(label)
        
        
        # Create a horizontal layout for the search box and buttons
        h_layout = QHBoxLayout()
        layout.addLayout(h_layout)
        
        # Create a line edit for URL or search query
        self.url_field = QLineEdit(self)
        self.url_field.setFont(QFont('Arial', 12))
        self.url_field.setPlaceholderText('Enter URL or Search Query:')  # Set the placeholder text
        h_layout.addWidget(self.url_field)
        
        # Create a button for navigation
        self.go_button = QPushButton('Go', self)
        self.go_button.clicked.connect(self.navigate_to_url)
        self.go_button.setStyleSheet("background-color: #4CAF50; color: white; border: none; padding: 10px 20px; font-size: 16px; border-radius: 5px;")
        h_layout.addWidget(self.go_button)
        
        # Create a button for Google search
        self.search_button = QPushButton('Search', self)
        self.search_button.clicked.connect(self.google_search)
        self.search_button.setStyleSheet("background-color: #4CAF50; color: white; border: none; padding: 10px 20px; font-size: 16px; border-radius: 5px;")
        h_layout.addWidget(self.search_button)
        
        # Create a web engine view
        self.view = QWebEngineView(self)
        layout.addWidget(self.view)
        
        self.show()
    
    def navigate_to_url(self):
        url = self.url_field.text()
        if not url.startswith('http'):
            url = 'http://' + url
        self.view.setUrl(QUrl(url))
    
    def google_search(self):
        query = self.url_field.text()
        url = 'https://www.google.com/search?q=' + query
        self.view.setUrl(QUrl(url))

app = QApplication(sys.argv)
browser = Browser()
sys.exit(app.exec_())