import sys
import psycopg2
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QHBoxLayout,
    QLineEdit, QPushButton, QTableWidget, QTableWidgetItem, QMessageBox,
    QHeaderView
)
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QIcon, QFont

from util.database import base_datos, user, password, host, port

conn = psycopg2.connect(
    dbname=base_datos,
    user=user,
    password=password,
    host=host,
    port=port
)

def delete_by_id(collaborator_id, table):
    reply = QMessageBox.question(
        None, "Confirm Deletion",
        f"Do you want to delete the collaborator with ID {collaborator_id}?",
        QMessageBox.Yes | QMessageBox.No
    )
    
    if reply == QMessageBox.Yes:
        cursor = conn.cursor()
        cursor.execute(
            "DELETE FROM collaborators WHERE id=%s",
            (collaborator_id,)
        )
        conn.commit()
        cursor.close()
        
        for input_field in table.parent().findChildren(QLineEdit):
            input_field.clear()
        
        table.clearSelection()
        table.setCurrentCell(-1, -1)
        
        load_collaborators(table)


def select_collaborator(table, name_input, role_input, salary_input):
    row = table.currentRow()
    if row == -1:
        return
    
    name_input.setText(table.item(row, 1).text())
    role_input.setText(table.item(row, 2).text())
    salary_input.setText(table.item(row, 3).text())


def save_collaborator(name_input, role_input, salary_input, table):
    name = name_input.text()
    role = role_input.text()
    salary = salary_input.text()
    
    row = table.currentRow()
    cursor = conn.cursor()

    if row != -1:
        id_item = table.item(row, 0)
        if id_item:
            collaborator_id = id_item.text()
            cursor.execute(
                """UPDATE collaborators SET name=%s, role=%s, salary=%s
                   WHERE id=%s
                """,
                (name, role, salary, collaborator_id)
            )
    else:
        cursor.execute(
            "INSERT INTO collaborators(name, role, salary) VALUES(%s, %s, %s)",
            (name, role, salary)
        )

    conn.commit()
    cursor.close()

    name_input.clear()
    role_input.clear()
    salary_input.clear()

    table.clearSelection()
    table.setCurrentCell(-1, -1)
    load_collaborators(table)


def load_collaborators(table):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM collaborators ORDER BY id")
    collaborators = cursor.fetchall()
    cursor.close()

    table.setRowCount(len(collaborators))
    table.setColumnCount(5)
    table.setHorizontalHeaderLabels(["ID", "Name", "Role", "Salary", "Action"])

    for i, collaborator in enumerate(collaborators):
        for j, value in enumerate(collaborator):
            item = QTableWidgetItem(str(value))
            item.setTextAlignment(Qt.AlignCenter)
            table.setItem(i, j, item)

        delete_button = QPushButton()
        delete_button.setIcon(QIcon("delete.png"))
        delete_button.setIconSize(QSize(24, 24))
        delete_button.setFlat(True)
        delete_button.clicked.connect(
            lambda _, id=collaborator[0]: delete_by_id(id, table)
        )

        table.setCellWidget(i, 4, delete_button)


def create_window():
    window = QWidget()
    window.setWindowTitle("Collaborator Management")
    window.setGeometry(100, 100, 900, 400)

    layout = QVBoxLayout()
    input_layout = QHBoxLayout()

    # Name input
    name_layout = QVBoxLayout()
    name_input = QLineEdit()
    name_input.setMinimumSize(200, 35)
    name_input.setFont(QFont("Arial", 12))
    name_label = QLabel("Name")
    name_label.setFont(QFont("Arial", 11))
    name_layout.addWidget(name_label)
    name_layout.addWidget(name_input)
    input_layout.addLayout(name_layout)

    # Role input
    role_layout = QVBoxLayout()
    role_input = QLineEdit()
    role_input.setMinimumSize(200, 35)
    role_input.setFont(QFont("Arial", 12))
    role_label = QLabel("Role")
    role_label.setFont(QFont("Arial", 11))
    role_layout.addWidget(role_label)
    role_layout.addWidget(role_input)
    input_layout.addLayout(role_layout)

    # Salary input
    salary_layout = QVBoxLayout()
    salary_input = QLineEdit()
    salary_input.setMinimumSize(200, 35)
    salary_input.setFont(QFont("Arial", 12))
    salary_label = QLabel("Salary")
    salary_label.setFont(QFont("Arial", 11))
    salary_layout.addWidget(salary_label)
    salary_layout.addWidget(salary_input)
    input_layout.addLayout(salary_layout)

    # Save button
    save_button = QPushButton()
    save_button.setIcon(QIcon("save.png"))
    save_button.setIconSize(QSize(36, 36))
    save_button.setFlat(True)
    save_button.setToolTip("Save Changes")
    input_layout.addWidget(save_button)

    input_layout.setStretch(0, 3)
    input_layout.setStretch(1, 1)
    input_layout.setStretch(2, 1)
    input_layout.setStretch(3, 0)

    layout.addLayout(input_layout)

    # Table
    table = QTableWidget()
    table.setColumnCount(4)
    table.setHorizontalHeaderLabels(['ID', "Name", "Role", "Salary"])
    table.horizontalHeader().setStretchLastSection(True)
    table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    layout.addWidget(table)

    save_button.clicked.connect(
        lambda: save_collaborator(name_input, role_input, salary_input, table)
    )

    table.cellClicked.connect(
        lambda row, col: select_collaborator(
            table, name_input, role_input, salary_input
        )
    )

    window.setLayout(layout)
    load_collaborators(table)
    window.show()
    return window


def main():
    app = QApplication(sys.argv)
    window = create_window()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
