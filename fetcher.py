from iex import Stock
import time
import datetime
import csv


def update_tickers(ticker_filename, graph_filename, info_filename):
    info = open(info_filename, "a")

    with open(graph_filename, 'at', newline='') as file:
        writer = csv.writer(file, delimiter=',')
        file = open(ticker_filename, "r")

        for line in file:
            symbol = line.replace("\n", "")
            stock = Stock(symbol).quote()
            currentDT = datetime.datetime.now()
            currTime = currentDT.strftime("%H:%M")
            column = [currTime,
                      stock['symbol'],
                      stock['latestPrice'],
                      stock['latestVolume'],
                      stock['close'],
                      stock['open'],
                      stock['low'],
                      stock['high']]
            writer.writerow(i for i in column)

            info_counter = 0
            for data in column:
                info.write(str(data))
                if info_counter == 2 or info_counter == 3:
                    info.write("\t")
                info.write("\t")
                info_counter = info_counter + 1
            info.write("\n")
        info.write("\n")


if __name__ == "__main__":
    # input seconds
    time_lim = int(input())
    minutes = time_lim / 60

    # filename where tickers are stored
    ticker_filename = input()

    # filename to write data to excel
     graph_filename = input()

    # filename to write query data
    info_filename = "info.txt"

    header = ['Time',
              'Ticker',
              'latestPrice',
              'latestVolume',
              'Close',
              'Open',
              'low',
              'high']

    with open(graph_filename, 'wt', newline='') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow(i for i in header)
        file.close()

    info = open(info_filename, "w")

    for label in header:
        info.write(label)
        info.write("\t")
    info.write("\n")

    counter = 0
    while counter < minutes:
        if counter > 0:
            #time.sleep(60)
            time.sleep(5)
        update_tickers(ticker_filename, graph_filename, info_filename)
        counter = counter + 1




