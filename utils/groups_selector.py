import random

people = ["A.B.J", "A.L.", "A.Š.", "A. Pe.", "A. Pu.", "A. M.", "D. G.", "D. R.", "E. S", "E. A.", "G. M.",
          "J. J.", "K. B.", "L. V.", "L. B.", "l. L.", "M. S.", "M. K.", "M. A.", "O. K.", "T. P.", "V. K.",
          "V. V.", "V. L."]

groups = []

while people:
    random.shuffle(people)
    groups.append(people[:5])
    people = people[5:]

print(groups)
