#exception handling in dictioanry

subject = {
        "name": "Python",
        "type": "Training",
        "hasExam": True,
        "hasProject": True,
        "gradeSystem": ["A+", "A", "B", "C", "F"],
        ("Attendance", ): "Must for everyone"
    }
try:
    (subject["noajay"])
except KeyError as et:
    print(et)
except NameError as et:
    print(et)
except ValueError as et:
    print(et)
except TypeError as et:
    print(et)
else:
    print("No errors")
finally:
    print("Executing Finally")

