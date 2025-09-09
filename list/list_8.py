# Dictionary Practice Example

# Initial dictionary
student = {"name": "Simran", "age": 21, "marks": 90}
print("Original Dictionary:", student)

# 1. keys()
print("\nKeys:", student.keys())

# 2. values()
print("Values:", student.values())

# 3. items()
print("Items:", student.items())

# 4. get()
print("Get 'age':", student.get("age"))
print("Get 'grade' (default N/A):", student.get("grade", "N/A"))

# 5. update()
student.update({"age": 22, "grade": "A"})
print("After update:", student)

#imp  6. pop()
removed = student.pop("marks")
print("Popped 'marks':", removed)
print("After pop:", student)

#imp 7. popitem()
last_item = student.popitem()
print("Popped last item:", last_item)
print("After popitem:", student)

# 8. copy()
student_copy = student.copy()
print("Copy of student:", student_copy)

# 9. fromkeys()
keys = ["a", "b", "c"]
new_dict = dict.fromkeys(keys, 0)
print("New dict from keys:", new_dict)

# 10. clear()
student.clear()
print("After clear:", student)
