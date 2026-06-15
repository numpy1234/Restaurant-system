from PyQt6.QtWidgets import *

from database import connect



class EmployeeWindow(QWidget):


    def __init__(self):

        super().__init__()

        self.setWindowTitle(
        "Employees"
        )


        layout=QVBoxLayout()



        self.name=QLineEdit()

        self.name.setPlaceholderText(
        "Name"
        )



        self.salary=QLineEdit()

        self.salary.setPlaceholderText(
        "Salary"
        )



        add=QPushButton(
        "Add Employee"
        )


        show=QPushButton(
        "Show Employees"
        )


        self.out=QTextEdit()



        layout.addWidget(self.name)

        layout.addWidget(self.salary)

        layout.addWidget(add)

        layout.addWidget(show)

        layout.addWidget(self.out)


        add.clicked.connect(
        self.add
        )


        show.clicked.connect(
        self.show
        )


        self.setLayout(layout)



    def add(self):


        con=connect()

        cur=con.cursor()



        cur.execute(

        """
        INSERT INTO Cook
        (Name,Salary)

        VALUES(%s,%s)

        """,

        (
        self.name.text(),
        self.salary.text()
        )

        )


        con.commit()



    def show(self):

        con=connect()

        cur=con.cursor()


        cur.execute(
        "SELECT * FROM Cook"
        )


        self.out.clear()


        for x in cur.fetchall():

            self.out.append(
            str(x)
            )
