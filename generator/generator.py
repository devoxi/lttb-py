import csv
import random


def signal_generator():
    seed = 1
    max_y = 250
    min_y = 100
    start_x = 0
    end_x = 7500

    random.seed(seed)
    prev_y = random.random()*(max_y-min_y)+min_y

    with open('source.csv', 'w') as f:
        csvf = csv.writer(f, delimiter=',')
        cur = start_x
        while cur <= end_x:
            if random.random() > 0.01:
                sign = random.choice([-1,1])
                amp = random.random()*5
                gen = random.random()*amp*sign+prev_y
            else:
                gen = random.random()*(max_y-min_y)+min_y
            prev_y = gen
            csvf.writerow([cur, gen])
            cur += 1


if __name__ == '__main__':
    signal_generator()
    exit()