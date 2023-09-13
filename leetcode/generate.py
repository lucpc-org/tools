from problem import Problem

easy = Problem().easy()
medium = Problem().medium()
hard = Problem().hard()

print(f"1. {easy.get_problem_link()}")
print(f"2. {medium.get_problem_link()}")
print(f"3. {hard.get_problem_link()}")