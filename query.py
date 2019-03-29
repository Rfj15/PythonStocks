import time

if __name__ == "__main__":
     info_filename = input()
     ticker = input()
     time = input()


    info = open(info_filename, "r")

    header = ['Time',
              'Ticker',
              'latestPrice',
              'latestVolume',
              'Close',
              'Open',
              'low',
              'high']

    for line in info:
        row = line.split()
        if len(row) > 0:
            if row[0] == time and row[1] == ticker:
                data = list(zip(header, row))
                for x in data:
                    print(x[0], ": ", x[1])