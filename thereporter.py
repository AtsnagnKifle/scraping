#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup
import openpyxl

base_url = "https://www.ethiopianreporterjobs.com/job-category/"
job_category = ['it-jobs-in-ethiopia',
                'construction-jobs-in-ethiopia', 'business-development']


def get_job(job_elements, category):

    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.append(('No', 'job_details_link', 'job_title', 'job_company', 'job_type',
                  'job_location', 'job_experience_level', 'job_date_posted', 'job_date_closing'))
    no = 1
    for job_element in job_elements:
        job_details_link = job_element.find(
            "a", class_="job-details-link")['href']
        job_title = job_element.find(
            "h3", class_="loop-item-title").find('a').text
        job_meta = job_element.find("p", class_="content-meta")
        job_company = job_meta.find(
            "span", class_="job-company").find("a").find("span").text
        job_type = job_meta.find(
            "span", class_="job-type").find("a").find("span").text
        job_location = job_meta.find(
            "span", class_="job-location").find("a").find("em").text
        job_experience_level = job_meta.find(
            "span", class_="job-experience_level").text
        job_date = job_meta.find(
            "span", class_="job-date")
        job_date_posted = job_date.find("span", class_="job-date__posted").text
        job_date_closing = job_date.find(
            "span", class_="job-date__closing").text

        sheet.append((no, job_details_link, job_title, job_company, job_type,
                      job_location, job_experience_level, job_date_posted, job_date_closing))
        no += 1

    wb.save('thereporter_{}.xlsx'.format(category))


for category in job_category:
    print("********start*********")
    print("********{}*********".format(category))

    page = requests.get(base_url+category)
    soup = BeautifulSoup(page.content, 'html.parser')
    job_elements = soup.find_all("article")
    get_job(job_elements, category)
    print("********end*********\n")
