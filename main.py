from lttb.lttb import largest_triangle_three_buckets
import csv


def main():
    with open('source.csv', 'r') as f:
        c = 0
        data = []
        csvf = csv.reader(f, delimiter=',')
        for row in csvf:
            if c == 0:
                c += 1
                continue
            data.append([int(row[0]), float(row[1])])
            c += 1
        sampled = largest_triangle_three_buckets(data, 500)
        with open('sampled.csv', 'w') as f2:
            csvf2 = csv.writer(f2, delimiter=',')
            for row in sampled:
                csvf2.writerow(row)


if __name__ == '__main__':
    main()
    exit()