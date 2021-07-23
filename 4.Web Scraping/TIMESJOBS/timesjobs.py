"""

- This script is scrape the TIMESJOBS website, which is job searching website.
- Once  job and experience are given, it will scrape and shows all data.
- It scapes all pages, not single page.
- For more details and step by step, TIMESJOBS.ipynb is  preferable.

"""

# !pip install beautifulsoup4
# !pip install lxml

# import modules
from bs4 import BeautifulSoup
import requests

base_url = 'https://www.timesjobs.com/'
my_job = input('Job: ')
experience = input("Enter only number.\nFor all experience, only press 'enter'.\nExperience: ")

seq = 1   # set page no

# fetch data until the last page
while True:

    # create url to fetch data on one page after another page 
    url = base_url + '/candidate/job-search.html?from=submit&txtKeywords=' + my_job+'&cboWorkExp1='+experience+'&sequence='+str(seq)

    # fetch HTMl text
    html_text = requests.get(url).text

    # parse HTML text using 'lxml'
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

    # loop all jobs and dispaly each job details.
    for job in jobs:

        # find required data in HTML tags
        position = job.find('h2').text.strip()
        print('Position: ', position)
        company_name = job.find('h3', class_='joblist-comp-name').text.strip()
        print('Company: ',company_name)
        skill = job.find('span', class_='srp-skills').text.strip()
        print('Skill: ',skill)
        published_date = job.find('span', class_='sim-posted').span.text.strip()
        print('Posted Date: ',published_date)
        more_info = job.header.h2.a['href']
        print('More info: ', more_info)
        print('-----------------------------------------------------------------------')

    # after one page, move to another page
    # check the page number bar and find current page
    bar = soup.find('div', class_='srp-pagination clearfix')
    # print(bar.find('em', class_='active').text)

    # get all  page numbers on the bar
    sequence_bar = bar.find_all('em')
    # print(sequence_bar[-1].text)

    # check the current page is the last page
    # print(bar.find('em', class_='active').text == sequence_bar[-1].text)

    # if current page is the last page, terminate loop.
    # else, move to another page and fetch data.
    if bar.find('em', class_='active').text == sequence_bar[-1].text:
        break
    seq = seq+1