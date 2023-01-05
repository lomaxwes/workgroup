
persons= [
    ('Allison Hill', 334053, 'M', '1635644202'),
    ('Megan Mcclain', 191161, 'F', '2101101595'),
    ('Brandon Hall', 731262, 'M', '6054749119'),
    ('Michelle Miles', 539898, 'M', '1355368461'),
    ('Donald Booth', 895667, 'M', '7736670978'),
    ('Gina Moore', 900581, 'F', '7018476624'),
    ('James Howard', 460663, 'F', '5461900982'),
    ('Monica Herrera', 496922, 'M', '2955495768'),
    ('Sandra Montgomery', 479201, 'M', '5111859731'),
    ('Amber Perez', 403445, 'M', '0602870126')
]

class Worker:
    def __init__(self, name='', salary=0, gender='', passport=''):
        self.name = name
        self.salary = salary
        self.gender = gender
        self.passport = passport

    def get_info(self):
        return f"Worker {self.name}; passport-{self.passport}"

bob = Worker('Bob Moore', 330000, 'M', '1635777202')


worker_objects = []

for people in persons:
    worker_objects.append(Worker(people[0], people[1], people[2], people[3]))

for work in worker_objects:
    print(work.get_info())

# Allison = Worker()
# Megan = Worker()
# Brandon = Worker()
# Michelle = Worker()
# Donald = Worker()
# Gina = Worker()
# James = Worker()
# Monica = Worker()
# Sandra = Worker()
# Amber = Worker()
# worker_objects.append(Allison)
# worker_objects.append(Megan)
# worker_objects.append(Brandon)
# worker_objects.append(Michelle)
# worker_objects.append(Donald)
# worker_objects.append(Gina)
# worker_objects.append(James)
# worker_objects.append(Monica)
# worker_objects.append(Sandra)
# worker_objects.append(Amber)
#
#
# for people in worker_objects:
#     print(people.get_info())