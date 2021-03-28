import csv
import sys

try:
    filename = sys.argv[1]
    csv_file = open(filename, 'r')

    csv_reader = csv.reader(csv_file)

    index_list = []
    watch_list = []
    next(csv_reader)

    for line in csv_reader:
        # print("Number "+ str(i) +str(line))
        # print(line[1])
        if "watch" in line[1]:
            watch_list.append([line[0], line[2]])
    i = 0
    cargo_list = []
    for watch in watch_list:
        index_list.append(watch)
        # print(str(index_list[i]) + " "+str(i))
        if i != 0 and index_list[i - 1][0] == index_list[i][0]:
            # print(i)
            cargo_list.append(index_list[i][0])
            print(str(index_list[i]) + " is duplicate")
            # del index_list[i]
            # index_list.pop(i)
        i += 1
    watch_set = set(cargo_list)
    cargo_list = list(watch_set)

    print(cargo_list)
    print(len(cargo_list))

    csv_file.close()
except:
    if len(sys.argv) is not 2:
        print("Usage: python3 main.py <csv-file name>")
    else:
        print("There is no file " + str(sys.argv[1]))


