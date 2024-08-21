import tracemalloc
import random
import time

names = ["John", "Ankit", "Rawat", "Rashmi", "Aru", "Ashish"]
majors = ["Maths", "Engineering", "Computers", "Arts", "Business"]


def people_list(num_people):
    result = []
    for i in range(num_people):
        person = {
            "id": i,
            "name": random.choice(names),
            "major": random.choice(majors)
        }
        result.append(person)
    return result


def people_generatr(num_people):
    for i in range(num_people):
        person = {
            "id": i,
            "name": random.choice(names),
            "major": random.choice(majors)
        }
        yield person


tracemalloc.start()
t1 = time.time()
# people = people_list(1000000)
people = people_generatr(1000000)

# memory
snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics('lineno')
for stat in top_stats[:10]:
    print(stat)
t2 = time.time()

print(f"Took {t2 - t1} Seconds..")
