import threading
import random
import time

def randomUserNumbers(a, b):
    values = []
    for i in range(10):
        values.append(random.randint(a, b))
    return values
start_time = time.time()
def value_max(zoznam):
    max_num = max(zoznam)
    print(f"najvacsie cislo je {max_num}")

def value_min(zoznam):
    min_num= min(zoznam)
    print(f"najmensie cislo je {min_num}")


zoznam = randomUserNumbers(1,999)

thread1 = threading.Thread(target=value_max, args=(zoznam,))
thread2 = threading.Thread(target=value_min, args=(zoznam,))

thread1.start()
thread2.start()

thread1.join()
thread2.join()
trvanie = time.time() - start_time


print(zoznam)
print(trvanie)
#print(value_min(zoznam))
#print(value_max(zoznam))



