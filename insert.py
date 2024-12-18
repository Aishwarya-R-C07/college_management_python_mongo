from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client['school']

# Delete previous data from collections
print("Deleting previous data from collections...")

# Delete all documents from each collection
db.Student.delete_many({})
db.Department.delete_many({})
db.Subject.delete_many({})
db.Staff.delete_many({})

# Insert new data into collections
print("Inserting data into collections...")

# Insert Students
students_data = [
    {"name": "Rahul", "age": 22, "grade": "A+"},
    {"name": "Priya", "age": 23, "grade": "B+"}
]
db.Student.insert_many(students_data)

# Insert Departments
departments_data = [
    {"name": "Electrical Engineering", "degree": "B.Tech", "hod_name": "Dr.S.Vishwanath"},
    {"name": "Biotechnology", "degree": "B.Tech", "hod_name": "Dr.N.Kavitha"}
]
db.Department.insert_many(departments_data)

# Insert Subjects
subjects_data = [
    {"name": "Circuit Theory", "code": "EE201", "credits": 4},
    {"name": "Genetic Engineering", "code": "BT201", "credits": 3}
]
db.Subject.insert_many(subjects_data)

# Insert Staff
staff_data = [
    {"name": "Prof.Sharan", "department": "Electrical Engineering", "experience": 12},
    {"name": "Dr.Ananya", "department": "Biotechnology", "experience": 9}
]
db.Staff.insert_many(staff_data)
