import time
import xlrd


def predictor(ticker, info_filename, graph_filename, col_name, time_range):
    info = open(info_filename, "r")

    for line in info:
        row = line.split()


if __name__ == "__main__":
    ticker = input()
    info_filename = input()
    graph_filename = input()
    col_name = input()
    time_range = input()

    counter = 0
    while counter < time_range:
        if counter > 0:
            time.sleep(60)
        predictor(ticker, info_filename, graph_filename, col_name, time_range)

