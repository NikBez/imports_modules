from datetime import datetime

import requests
from bs4 import BeautifulSoup

from application.db.people import get_employees
from application.salary import calculate_salary


def main():
    calculate_salary()
    get_employees()
    print(datetime.utcnow())


    response = requests.get('http://www.google.com')
    response.raise_for_status()
    response = response.text

    soup = BeautifulSoup(response, 'html.parser')
    print(soup.find_all('b'))


if __name__ == '__main__':
    main()
