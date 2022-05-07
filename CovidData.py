'''
This code fetches Covid data for last 3 days of a particular country
'''
from itertools import islice
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen


class CovidDataCollector:
    def __init__(self, country):
        self.country = country

    def web_scraper(self):
        req = Request('https://www.worldometers.info/coronavirus/#countries', headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()
        html = webpage.decode("utf-8")
        soup = BeautifulSoup(html, "html.parser")
        data_obtained = soup.get_text()
        return data_obtained

    def store_data(self, data_obtained):
        with open(outputFile, "w", encoding="utf-8") as f:
            f.write(data_obtained)

    def covid_count(self):
        case_list = []
        with open(outputFile, "r") as f:
            for line in f:
                if self.country in line:
                    val = ''.join(islice(f, 2))
                    if "+" in val:
                        cases = val
                        final_count = cases.partition('\n')[-1]
                        case_list.append(final_count)
        converted_list = []
        for element in case_list:
            converted_list.append(element.strip())
        return converted_list

    def int_to_str(self, plus_list):
        string_list = []
        for value in plus_list:
            cases_in_string = ''.join(ch for ch in value if ch.isalnum())
            string_list.append(cases_in_string)
        return string_list

    def cases_count_per_country(self, cases):
        updated_list = cases
        size = len(cases)
        if size == 1:
            updated_list.insert(0, 0)
            updated_list.insert(1, 0)
            print("Only data from last two days are available")
        elif size == 2:
            updated_list.insert(0, 0)
            print("Today's data hasn't been received yet")
        elif size == 3:
            print("All data are available")
        return updated_list

    def print_covid_data(self, finaldata):
        dates = ["Today", "Yesterday", "2 days ago"]
        print(f'Below are the covid details of {self.country} for the past 3 days')
        for data, date in zip(finaldata, dates):
            print(f'Covid cases as of {date} is {data}')


outputFile = 'data.txt'
country_name = input("Please provide the country name: ")
covid = CovidDataCollector(country_name)
mydata = covid.web_scraper()
covid.store_data(mydata)
active_cases = covid.covid_count()
string_list = covid.int_to_str(active_cases)
final_list = covid.cases_count_per_country(string_list)
covid.print_covid_data(final_list)
