from flask import Flask, render_template, request, redirect, url_for
import mariadb
import os

app = Flask(__name__)

def get_connection():
    return mariadb.connect(
        host="localhost",
        port=3306,
        user="root",
        password=os.getenv("DB_PASSWORD", "YOUR_PASSWORD"),
        database="flask_demo"
    )

@app.route("/")
def home():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, email, course FROM students")
    students = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template("index.html", students=students)

@app.route("/add", methods=["POST"])
def add_student():
    name = request.form["name"]
    email = request.form["email"]
    course = request.form["course"]
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO students (name, email, course) VALUES (?, ?, ?)",
        (name, email, course)
    )
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for("home"))

@app.route("/edit/<int:id>")
def edit_student(id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id, name, email, course FROM students WHERE id=?",
        (id,)
    )
    student = cursor.fetchone()
    cursor.close()
    conn.close()
    return render_template("edit.html", student=student)

@app.route("/update/<int:id>", methods=["POST"])
def update_student(id):
    name = request.form["name"]
    email = request.form["email"]
    course = request.form["course"]
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE students SET name=?, email=?, course=? WHERE id=?",
        (name, email, course, id)
    )
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for("home"))

@app.route("/delete/<int:id>")
def delete_student(id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE id=?", (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
