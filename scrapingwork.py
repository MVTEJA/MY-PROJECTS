import requests
from bs4 import BeautifulSoup


for i in range(1 , 25):
    url_text = requests.get(f'https://internshala.com/internships/web%20development-internship/page-{i}').text

    soup = BeautifulSoup(url_text, 'lxml')

    div_tags = soup.find_all('div', class_='internship_meta')

    for d_tag in div_tags:
        position = d_tag.find('a').text.strip()
        company = d_tag.find('div', class_='heading_6 company_name').text.strip()
        location = d_tag.find('a', class_='location_link view_detail_button').text.strip()
        stipend = d_tag.find('span', class_='stipend').text.strip()

        print(f'Position: {position}\nCompany: {company}\nLocation: {location}\nStipend: {stipend}')
        print("\n")












