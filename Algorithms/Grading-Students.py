def gradingStudents(grades):

    for i in range(len(grades)):

        current = grades[i]

        if (current < 38) or (current % 5) < 3:

            pass

        else:

            grades[i] = (current + 5) - (current % 5)

    return grades

    # OR

    # return [max(n, (n + 2) // 5 * 5) if n >= 38 else n for n in grades]