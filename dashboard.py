from PyQt6.QtWidgets import *

from dishes import DishWindow
from employees import EmployeeWindow
from orders import OrderWindow



class Dashboard(QWidget):

    def __init__(self):

        super().__init__()

        self.setWindowTitle(
            "Restaurant Dashboard"
        )

        self.resize(500,400)


        layout=QVBoxLayout()


        title=QLabel(
            "MODERN RESTAURANT"
        )

        layout.addWidget(title)



        dish=QPushButton(
            "Manage Dishes"
        )

        emp=QPushButton(
            "Manage Employees"
        )

        order=QPushButton(
            "Create Order"
        )


        layout.addWidget(dish)
        layout.addWidget(emp)
        layout.addWidget(order)



        dish.clicked.connect(
            self.open_dish
        )

        emp.clicked.connect(
            self.open_employee
        )

        order.clicked.connect(
            self.open_order
        )


        self.setLayout(layout)



    def open_dish(self):

        self.w=DishWindow()

        self.w.show()



    def open_employee(self):

        self.w=EmployeeWindow()

        self.w.show()



    def open_order(self):

        self.w=OrderWindow()

        self.w.show()
