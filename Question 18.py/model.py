import sqlite3


class EmployeeModel:

    def __init__(self, db_name="employees.db"):
        self.db_name = db_name

    def connect(self):
        return sqlite3.connect(self.db_name)

    def get_departments(self):
        conn = self.connect()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT DISTINCT department
            FROM employees
            ORDER BY department
        """)

        departments = [row[0] for row in cursor.fetchall()]

        conn.close()

        return departments

    def get_salary_report(self, department):
        conn = self.connect()
        cursor = conn.cursor()

        # Parameterized SQL query
        cursor.execute("""
            SELECT employee_id,
                   name,
                   designation,
                   salary
            FROM employees
            WHERE department = ?
            ORDER BY salary DESC
        """, (department,))

        employees = cursor.fetchall()

        conn.close()

        return employees

    def get_department_summary(self, department):
        conn = self.connect()
        cursor = conn.cursor()

        # Parameterized aggregate query
        cursor.execute("""
            SELECT COUNT(*),
                   SUM(salary),
                   AVG(salary),
                   MIN(salary),
                   MAX(salary)
            FROM employees
            WHERE department = ?
        """, (department,))

        summary = cursor.fetchone()

        conn.close()

        return summary
