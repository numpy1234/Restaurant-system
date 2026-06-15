from PyQt6.QtWidgets import *

from database import connect



class OrderWindow(QWidget):


    def __init__(self):

        super().__init__()


        self.setWindowTitle(
        "Create Order"
        )


        layout=QVBoxLayout()


        self.customer=QLineEdit()

        self.customer.setPlaceholderText(
        "Customer Name"
        )


        self.dish=QLineEdit()

        self.dish.setPlaceholderText(
        "Dish ID"
        )


        create=QPushButton(
        "Create Order"
        )


        layout.addWidget(
        self.customer
        )

        layout.addWidget(
        self.dish
        )

        layout.addWidget(
        create
        )


        create.clicked.connect(
        self.create
        )


        self.setLayout(layout)



    def create(self):


        con=connect()

        cur=con.cursor()



        cur.execute(

        """
        SELECT Cost
        FROM Dish
        WHERE DishID=%s

        """,

        (self.dish.text(),)

        )


        price=cur.fetchone()[0]



        cur.execute(

        """
        INSERT INTO Orders
        (Customer,Date,Total)

        VALUES(%s,CURDATE(),%s)

        """,

        (
        self.customer.text(),
        price
        )

        )


        con.commit()



        QMessageBox.information(
        self,
        "Bill",
        "Total = ₹"+str(price)
        )
