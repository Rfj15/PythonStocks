from lxml import html
import requests


def save_tickers(num_tickers, filename):
    page = requests.get('https://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQrender=download')
    tree = html.fromstring(page.content)

    companies = tree.xpath('//*[@id="CompanylistResults"]/tr/td[2]/h3/a/text()')
    companies = [x.strip() for x in companies]

    file = open(filename, "w")

    for company in companies[:num_tickers]:
            file.write(company)
            file.write("\n")
    file.close()


if __name__ == "__main__":
    num_tickers = int(input())
    filename = input()
    save_tickers(num_tickers, filename)