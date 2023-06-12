def study_schedule(permanence_period, target_time):
    if type(permanence_period) != list or type(target_time) != int:
        return None

    quantity_students = 0

    for student in permanence_period:
        if type(student[0]) != int or type(student[1]) != int:
            return None
        if student[0] <= target_time <= student[1]:
            quantity_students += 1

    return quantity_students
