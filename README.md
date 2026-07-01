# Flask MariaDB CRUD

## Install

```bash
python -m pip install -r requirements.txt
```

## Database

```sql
CREATE DATABASE flask_demo;

USE flask_demo;

CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    course VARCHAR(100)
);
```

Update YOUR_PASSWORD in app.py or set DB_PASSWORD environment variable.

Run:

```bash
python app.py
```
