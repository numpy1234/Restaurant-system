from PyQt6.QtWidgets import *

from database import connect



class DishWindow(QWidget):


    def __init__(self):

        super().__init__()


        self.setWindowTitle("Dishes")

        self.resize(400,400)


        layout = QVBoxLayout()


        self.name = QLineEdit()
        self.name.setPlaceholderText("Dish Name")


        self.cost = QLineEdit()
        self.cost.setPlaceholderText("Cost")


        self.cook = QComboBox()


        self.load_cooks()



        add = QPushButton("Add Dish")

        show = QPushButton("Show Dishes")


        self.output = QTextEdit()



        layout.addWidget(self.name)

        layout.addWidget(self.cost)

        layout.addWidget(QLabel("Cook"))

        layout.addWidget(self.cook)

        layout.addWidget(add)

        layout.addWidget(show)

        layout.addWidget(self.output)



        add.clicked.connect(
            self.add
        )


        show.clicked.connect(
            self.display
        )



        self.setLayout(layout)




    def load_cooks(self):

        con = connect()

        cur = con.cursor()


        cur.execute(
            "SELECT CookID,Name FROM Cook"
        )


        cooks = cur.fetchall()


        if len(cooks)==0:

            self.cook.addItem(
                "Add employees first"
            )

            return



        for c in cooks:

            self.cook.addItem(
                c[1],
                c[0]
            )




    def add(self):


        if self.cook.currentData() is None:


            QMessageBox.warning(
                self,
                "Error",
                "Please add employees first"
            )

            return



        con = connect()

        cur = con.cursor()



        cur.execute(

        """
        INSERT INTO Dish
        (Name,Cost,CookID)

        VALUES(%s,%s,%s)

        """,

        (
        self.name.text(),
        self.cost.text(),
        self.cook.currentData()
        )

        )


        con.commit()



        QMessageBox.information(

        self,

        "Success",

        "Dish Added"

        )



    def display(self):


        con = connect()

        cur = con.cursor()



        cur.execute(

        """
        SELECT 
        Dish.DishID,
        Dish.Name,
        Dish.Cost,
        Cook.Name

        FROM Dish

        JOIN Cook

        ON Dish.CookID = Cook.CookID

        """

        )



        self.output.clear()



        for x in cur.fetchall():

            self.output.append(

            f"""
ID: {x[0]}
Dish: {x[1]}
Cost: ₹{x[2]}
Cook: {x[3]}

----------------
"""

            )
