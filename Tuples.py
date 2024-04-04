studentList = ("minoo","nasrin","aws","asya")

for i in studentList:
    print(i)

    print(studentList)

    tuplechange = list (studentList)

    print(tuplechange)

    tuplechange.pop(0)
    studentList = tuple(tuplechange)

    print(studentList)