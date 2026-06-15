from PyQt6.QtWidgets import *

from login import check_login
from dashboard import Dashboard



app = QApplication([])


login_window = QWidget()

login_window.setWindowTitle("Restaurant Login")

login_window.resize(350,200)



layout = QVBoxLayout()



user = QLineEdit()
user.setPlaceholderText("Username")


password = QLineEdit()
password.setPlaceholderText("Password")

password.setEchoMode(
    QLineEdit.EchoMode.Password
)


button = QPushButton("Login")



layout.addWidget(user)
layout.addWidget(password)
layout.addWidget(button)



login_window.setLayout(layout)



# keep reference here
dashboard_window = None



def login():

    global dashboard_window


    if check_login(
        user.text(),
        password.text()
    ):

        login_window.hide()


        dashboard_window = Dashboard()

        dashboard_window.show()


    else:

        QMessageBox.warning(
            login_window,
            "Error",
            "Wrong Login"
        )



button.clicked.connect(login)



login_window.show()


app.exec()
