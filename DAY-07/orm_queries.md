```python
Student.objects.create(
name="Harshita",
email="harshita@example.com",
age=21,
course="AI"
)

Student.objects.create(
name="Rahul",
email="rahul@example.com",
age=19,
course="Python"
)

Student.objects.create(
name="Priya",
email="priya@example.com",
age=22,
course="Django"
)

Student.objects.all()

Student.objects.values('name','course')

Student.objects.filter(age__gt=20)

Student.objects.get(name="Harshita")

student = Student.objects.get(name="Rahul")
student.course = "Machine Learning"
student.save()

student = Student.objects.get(name="Priya")
student.age += 1
student.save()

student = Student.objects.get(name="Rahul")
student.delete()
```