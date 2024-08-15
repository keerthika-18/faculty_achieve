import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import mysql.connector
import csv

# Database connection and management functions...

def fetch_students():
    db = mysql.connector.connect(host="localhost", user="keerthi", password="Keerthi@1807", database="Student_management1")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    db.close()
    return rows

def add_student_to_db(first_name, last_name, email, age):
    db = mysql.connector.connect(host="localhost", user="keerthi", password="Keerthi@1807", database="Student_management1")
    cursor = db.cursor()
    cursor.execute("INSERT INTO students (first_name, last_name, email, age) VALUES (%s, %s, %s, %s)", (first_name, last_name, email, age))
    db.commit()
    db.close()

def update_student_in_db(student_id, first_name, last_name, email, age):
    db = mysql.connector.connect(host="localhost", user="keerthi", password="Keerthi@1807", database="student_management1")
    cursor = db.cursor()
    cursor.execute("UPDATE students SET first_name=%s, last_name=%s, email=%s, age=%s WHERE student_id=%s", (first_name, last_name, email, age, student_id))
    db.commit()
    db.close()

def delete_student_from_db(student_id):
    db = mysql.connector.connect(host="localhost", user="keerthi", password="Keerthi@1807", database="Student_management1")
    cursor = db.cursor()
    cursor.execute("DELETE FROM students WHERE student_id=%s", (student_id,))
    db.commit()
    db.close()

def export_students_to_csv(filename):
    rows = fetch_students()
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "First Name", "Last Name", "Email", "Age"])
        writer.writerows(rows)

def search_students(search_term):
    db = mysql.connector.connect(host="localhost", user="keerthi", password="Keerthi@1807", database="Student_management1")
    cursor = db.cursor()
    query = "SELECT * FROM students WHERE first_name LIKE %s OR last_name LIKE %s OR email LIKE %s"
    cursor.execute(query, (f'%{search_term}%', f'%{search_term}%', f'%{search_term}%'))
    rows = cursor.fetchall()
    db.close()
    return rows

def fetch_teachers():
    db = mysql.connector.connect(host="localhost", user="keerthi", password="Keerthi@1807", database="Student_management1")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM teachers")
    rows = cursor.fetchall()
    db.close()
    return rows

def add_teacher_to_db(first_name, last_name, email, subject):
    db = mysql.connector.connect(host="localhost", user="keerthi", password="Keerthi@1807", database="Student_management1")
    cursor = db.cursor()
    cursor.execute("INSERT INTO teachers (first_name, last_name, email, subject) VALUES (%s, %s, %s, %s)", (first_name, last_name, email, subject))
    db.commit()
    db.close()

def update_teacher_in_db(teacher_id, first_name, last_name, email, subject):
    db = mysql.connector.connect(host="localhost", user="keerthi", password="Keerthi@1807", database="Student_management1")
    cursor = db.cursor()
    cursor.execute("UPDATE teachers SET first_name=%s, last_name=%s, email=%s, subject=%s WHERE teacher_id=%s", (first_name, last_name, email, subject, teacher_id))
    db.commit()
    db.close()

def delete_teacher_from_db(teacher_id):
    db = mysql.connector.connect(host="localhost", user="keerthi", password="Keerthi@1807", database="Student_management1")
    cursor = db.cursor()
    cursor.execute("DELETE FROM teachers WHERE teacher_id=%s", (teacher_id,))
    db.commit()
    db.close()

def export_teachers_to_csv(filename):
    rows = fetch_teachers()
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "First Name", "Last Name", "Email", "Subject"])
        writer.writerows(rows)

def search_teachers(search_term):
    db = mysql.connector.connect(host="localhost", user="keerthi", password="Keerthi@1807", database="Student_management1")
    cursor = db.cursor()
    query = "SELECT * FROM teachers WHERE first_name LIKE %s OR last_name LIKE %s OR email LIKE %s OR subject LIKE %s"
    cursor.execute(query, (f'%{search_term}%', f'%{search_term}%', f'%{search_term}%', f'%{search_term}%'))
    rows = cursor.fetchall()
    db.close()
    return rows

class ManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Management System")
        
        self.style = ttk.Style()
        self.style.configure("TFrame", background="#F0F0F0")
        self.style.configure("TLabel", background="#F0F0F0")
        self.style.configure("Student.TFrame", background="#E0F7FA")
        self.style.configure("Teacher.TFrame", background="#FFEBEE")
        
        self.create_widgets()

    def create_widgets(self):
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(pady=10, expand=True)

        self.student_frame = ttk.Frame(self.notebook, width=400, height=280, style="Student.TFrame")
        self.teacher_frame = ttk.Frame(self.notebook, width=400, height=280, style="Teacher.TFrame")

        self.student_frame.pack(fill='both', expand=True)
        self.teacher_frame.pack(fill='both', expand=True)

        self.notebook.add(self.student_frame, text='Students')
        self.notebook.add(self.teacher_frame, text='Teachers')

        # Student Widgets
        self.student_id = tk.StringVar()
        self.student_first_name = tk.StringVar()
        self.student_last_name = tk.StringVar()
        self.student_email = tk.StringVar()
        self.student_age = tk.StringVar()
        self.student_search_term = tk.StringVar()

        self.create_student_widgets()
        self.load_students()

        # Teacher Widgets
        self.teacher_id = tk.StringVar()
        self.teacher_first_name = tk.StringVar()
        self.teacher_last_name = tk.StringVar()
        self.teacher_email = tk.StringVar()
        self.teacher_subject = tk.StringVar()
        self.teacher_search_term = tk.StringVar()

        self.create_teacher_widgets()
        self.load_teachers()

    def create_student_widgets(self):
        ttk.Label(self.student_frame, text="First Name").grid(row=0, column=0, padx=10, pady=5)
        ttk.Entry(self.student_frame, textvariable=self.student_first_name).grid(row=0, column=1, padx=10, pady=5)
        
        ttk.Label(self.student_frame, text="Last Name").grid(row=1, column=0, padx=10, pady=5)
        ttk.Entry(self.student_frame, textvariable=self.student_last_name).grid(row=1, column=1, padx=10, pady=5)
        
        ttk.Label(self.student_frame, text="Email").grid(row=2, column=0, padx=10, pady=5)
        ttk.Entry(self.student_frame, textvariable=self.student_email).grid(row=2, column=1, padx=10, pady=5)
        
        ttk.Label(self.student_frame, text="Age").grid(row=3, column=0, padx=10, pady=5)
        ttk.Entry(self.student_frame, textvariable=self.student_age).grid(row=3, column=1, padx=10, pady=5)

        self.student_tree = ttk.Treeview(self.student_frame, columns=("ID", "First Name", "Last Name", "Email", "Age"), show='headings')
        self.student_tree.grid(row=6, column=0, columnspan=3, pady=20)

        for col in self.student_tree['columns']:
            self.student_tree.heading(col, text=col)

        button_style = {"bg": "#4CAF50", "fg": "white", "bd": 0, "relief": "flat"}

        add_button = tk.Button(self.student_frame, text="Add", command=self.add_student, **button_style)
        add_button.grid(row=4, column=0, padx=10, pady=5)

        edit_button = tk.Button(self.student_frame, text="Edit", command=self.edit_student, **button_style)
        edit_button.grid(row=4, column=1, padx=10, pady=5)

        delete_button = tk.Button(self.student_frame, text="Delete", command=self.delete_student, **button_style)
        delete_button.grid(row=4, column=2, padx=10, pady=5)

        export_button = tk.Button(self.student_frame, text="Export to CSV", command=self.export_students_to_csv, **button_style)
        export_button.grid(row=7, column=0, columnspan=3, pady=10)

        ttk.Label(self.student_frame, text="Search").grid(row=5, column=0, padx=10, pady=5)
        ttk.Entry(self.student_frame, textvariable=self.student_search_term).grid(row=5, column=1, padx=10, pady=5)
        search_button = tk.Button(self.student_frame, text="Search", command=self.search_students, **button_style)
        search_button.grid(row=5, column=2, padx=10, pady=5)

    def create_teacher_widgets(self):
        ttk.Label(self.teacher_frame, text="First Name").grid(row=0, column=0, padx=10, pady=5)
        ttk.Entry(self.teacher_frame, textvariable=self.teacher_first_name).grid(row=0, column=1, padx=10, pady=5)
        
        ttk.Label(self.teacher_frame, text="Last Name").grid(row=1, column=0, padx=10, pady=5)
        ttk.Entry(self.teacher_frame, textvariable=self.teacher_last_name).grid(row=1, column=1, padx=10, pady=5)
        
        ttk.Label(self.teacher_frame, text="Email").grid(row=2, column=0, padx=10, pady=5)
        ttk.Entry(self.teacher_frame, textvariable=self.teacher_email).grid(row=2, column=1, padx=10, pady=5)
        
        ttk.Label(self.teacher_frame, text="Subject").grid(row=3, column=0, padx=10, pady=5)
        ttk.Entry(self.teacher_frame, textvariable=self.teacher_subject).grid(row=3, column=1, padx=10, pady=5)

        self.teacher_tree = ttk.Treeview(self.teacher_frame, columns=("ID", "First Name", "Last Name", "Email", "Subject"), show='headings')
        self.teacher_tree.grid(row=6, column=0, columnspan=3, pady=20)

        for col in self.teacher_tree['columns']:
            self.teacher_tree.heading(col, text=col)

        button_style = {"bg": "#FF7043", "fg": "white", "bd": 0, "relief": "flat"}

        add_button = tk.Button(self.teacher_frame, text="Add", command=self.add_teacher, **button_style)
        add_button.grid(row=4, column=0, padx=10, pady=5)

        edit_button = tk.Button(self.teacher_frame, text="Edit", command=self.edit_teacher, **button_style)
        edit_button.grid(row=4, column=1, padx=10, pady=5)

        delete_button = tk.Button(self.teacher_frame, text="Delete", command=self.delete_teacher, **button_style)
        delete_button.grid(row=4, column=2, padx=10, pady=5)

        export_button = tk.Button(self.teacher_frame, text="Export to CSV", command=self.export_teachers_to_csv, **button_style)
        export_button.grid(row=7, column=0, columnspan=3, pady=10)

        ttk.Label(self.teacher_frame, text="Search").grid(row=5, column=0, padx=10, pady=5)
        ttk.Entry(self.teacher_frame, textvariable=self.teacher_search_term).grid(row=5, column=1, padx=10, pady=5)
        search_button = tk.Button(self.teacher_frame, text="Search", command=self.search_teachers, **button_style)
        search_button.grid(row=5, column=2, padx=10, pady=5)

    def add_student(self):
        first_name = self.student_first_name.get()
        last_name = self.student_last_name.get()
        email = self.student_email.get()
        age = self.student_age.get()
        if first_name and last_name:
            add_student_to_db(first_name, last_name, email, age)
            self.load_students()
        else:
            messagebox.showwarning("Input Error", "First Name and Last Name are required fields.")

    def edit_student(self):
        selected_item = self.student_tree.selection()
        if selected_item:
            item = self.student_tree.item(selected_item)
            student_id = item['values'][0]
            first_name = self.student_first_name.get()
            last_name = self.student_last_name.get()
            email = self.student_email.get()
            age = self.student_age.get()
            update_student_in_db(student_id, first_name, last_name, email, age)
            self.load_students()
        else:
            messagebox.showwarning("Selection Error", "Please select a student to edit.")

    def delete_student(self):
        selected_item = self.student_tree.selection()
        if selected_item:
            item = self.student_tree.item(selected_item)
            student_id = item['values'][0]
            delete_student_from_db(student_id)
            self.load_students()
        else:
            messagebox.showwarning("Selection Error", "Please select a student to delete.")

    def load_students(self):
        for row in self.student_tree.get_children():
            self.student_tree.delete(row)
        rows = fetch_students()
        for row in rows:
            self.student_tree.insert("", "end", values=row)

    def export_students_to_csv(self):
        filename = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
        if filename:
            export_students_to_csv(filename)

    def search_students(self):
        search_term = self.student_search_term.get()
        for row in self.student_tree.get_children():
            self.student_tree.delete(row)
        rows = search_students(search_term)
        for row in rows:
            self.student_tree.insert("", "end", values=row)

    def add_teacher(self):
        first_name = self.teacher_first_name.get()
        last_name = self.teacher_last_name.get()
        email = self.teacher_email.get()
        subject = self.teacher_subject.get()
        if first_name and last_name:
            add_teacher_to_db(first_name, last_name, email, subject)
            self.load_teachers()
        else:
            messagebox.showwarning("Input Error", "First Name and Last Name are required fields.")

    def edit_teacher(self):
        selected_item = self.teacher_tree.selection()
        if selected_item:
            item = self.teacher_tree.item(selected_item)
            teacher_id = item['values'][0]
            first_name = self.teacher_first_name.get()
            last_name = self.teacher_last_name.get()
            email = self.teacher_email.get()
            subject = self.teacher_subject.get()
            update_teacher_in_db(teacher_id, first_name, last_name, email, subject)
            self.load_teachers()
        else:
            messagebox.showwarning("Selection Error", "Please select a teacher to edit.")

    def delete_teacher(self):
        selected_item = self.teacher_tree.selection()
        if selected_item:
            item = self.teacher_tree.item(selected_item)
            teacher_id = item['values'][0]
            delete_teacher_from_db(teacher_id)
            self.load_teachers()
        else:
            messagebox.showwarning("Selection Error", "Please select a teacher to delete.")

    def load_teachers(self):
        for row in self.teacher_tree.get_children():
            self.teacher_tree.delete(row)
        rows = fetch_teachers()
        for row in rows:
            self.teacher_tree.insert("", "end", values=row)

    def export_teachers_to_csv(self):
        filename = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
        if filename:
            export_teachers_to_csv(filename)

    def search_teachers(self):
        search_term = self.teacher_search_term.get()
        for row in self.teacher_tree.get_children():
            self.teacher_tree.delete(row)
        rows = search_teachers(search_term)
        for row in rows:
            self.teacher_tree.insert("", "end", values=row)

if __name__ == "__main__":
    root = tk.Tk()
    app = ManagementSystem(root)
    root.mainloop()
