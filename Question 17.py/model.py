import sqlite3


class EmployeeModel:

    def __init__(self, db_name="employees.db"):
        self.db_name = db_name
        self.create_table()

    def connect(self):
        return sqlite3.connect(self.db_name)

    def create_table(self):
        conn = self.connect()
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS employees (
                employee_id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                designation TEXT NOT NULL,
                department TEXT NOT NULL,
                salary REAL NOT NULL
            )
        """)

        conn.commit()
        conn.close()

    # CREATE
    def add_employee(self, employee_id, name, designation,
                     department, salary):
        try:
            conn = self.connect()
            cursor = conn.cursor()

            cursor.execute("""
                INSERT INTO employees
                (employee_id, name, designation, department, salary)
                VALUES (?, ?, ?, ?, ?)
            """, (employee_id, name, designation, department, salary))

            conn.commit()
            conn.close()

            return True

        except sqlite3.IntegrityError:
            return False

    # READ
    def get_all_employees(self):
        conn = self.connect()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM employees")

        employees = cursor.fetchall()

        conn.close()

        return employees

    def get_employee(self, employee_id):
        conn = self.connect()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM employees WHERE employee_id = ?",
            (employee_id,)
        )

        employee = cursor.fetchone()

        conn.close()

        return employee

    # UPDATE
    def update_employee(self, employee_id, name, designation,
                        department, salary):
        conn = self.connect()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE employees
            SET name = ?,
                designation = ?,
                department = ?,
                salary = ?
            WHERE employee_id = ?
        """, (name, designation, department, salary, employee_id))

        conn.commit()

        updated = cursor.rowcount > 0

        conn.close()

        return updated

    # DELETE
    def delete_employee(self, employee_id):
        conn = self.connect()
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM employees WHERE employee_id = ?",
            (employee_id,)
        )

        conn.commit()

        deleted = cursor.rowcount > 0

        conn.close()

        return deleted
