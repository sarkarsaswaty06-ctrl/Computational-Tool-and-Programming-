import sqlite3


class StudentModel:
    def __init__(self, db_name="students.db"):
        self.db_name = db_name
        self.create_table()

    def connect(self):
        return sqlite3.connect(self.db_name)

    def create_table(self):
        conn = self.connect()
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS students (
                roll_no INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                department TEXT NOT NULL,
                cgpa REAL NOT NULL
            )
        """)

        conn.commit()
        conn.close()

    def add_student(self, roll_no, name, department, cgpa):
        try:
            conn = self.connect()
            cursor = conn.cursor()

            cursor.execute("""
                INSERT INTO students (roll_no, name, department, cgpa)
                VALUES (?, ?, ?, ?)
            """, (roll_no, name, department, cgpa))

            conn.commit()
            conn.close()
            return True

        except sqlite3.IntegrityError:
            return False

    def get_all_students(self):
        conn = self.connect()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM students")
        students = cursor.fetchall()

        conn.close()
        return students

    def get_student(self, roll_no):
        conn = self.connect()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM students WHERE roll_no = ?",
            (roll_no,)
        )

        student = cursor.fetchone()
        conn.close()

        return student

    def update_student(self, roll_no, name, department, cgpa):
        conn = self.connect()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE students
            SET name = ?, department = ?, cgpa = ?
            WHERE roll_no = ?
        """, (name, department, cgpa, roll_no))

        conn.commit()
        updated = cursor.rowcount > 0
        conn.close()

        return updated

    def delete_student(self, roll_no):
        conn = self.connect()
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM students WHERE roll_no = ?",
            (roll_no,)
        )

        conn.commit()
        deleted = cursor.rowcount > 0
        conn.close()

        return deleted
