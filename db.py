import sqlite3


class Database:
    def __init__(self, db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        sql = """
        CREATE TABLE IF NOT EXISTS employees(
            id Integer Primary Key,
            name text,
            age text,
            doj text,
            email text,
            gender text,
            contact text,
            address text
        )
        """
        self.cur.execute(sql)
        self.con.commit()

    # insert function
    def insert(self, name, age, doj, email, gender, contact, address):
        self.cur.execute("INSERT INTO employees (name, age, doj, email, gender, contact, address) VALUES (?, ?, ?, ?, ?, ?, ?)",
                         (name, age, doj, email, gender, contact, address))
        self.con.commit()

    # fetch all data from DB
    def fetch(self):
        self.cur.execute("SELECT * FROM employees")
        rows = self.cur.fetchall()
        return rows

    # delete a record in db
    def remove(self, id):
        self.cur.execute("DELETE FROM employees WHERE id = ?", (id,))
        self.con.commit()

    # update in db
    def update(self, id, name, age, doj, email, gender, contact, address):
        self.cur.execute("UPDATE employees SET name = ?, age = ?, doj = ?, email = ?, gender = ?, contact = ?, address = ? WHERE id = ?",
                         (name, age, doj, email, gender, contact, address, id))
        self.con.commit()
