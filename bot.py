import botogram
import requests
from bs4 import BeautifulSoup
import openpyxl

bot = botogram.create("API")
base_url = "https://www.ethiopianreporterjobs.com/job-category/"


def get_job(category):
    page = requests.get(base_url+category)
    soup = BeautifulSoup(page.content, 'html.parser')
    job_elements = soup.find_all("article")

    no = 1
    jobs = []
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

        jobs.append((no, job_details_link, job_title, job_company, job_type,
                     job_location, job_experience_level, job_date_posted, job_date_closing))
        no += 1

    return jobs


@bot.command("jobs")
def survey_command(chat, message, args):
    btns = botogram.Buttons()
    btns[0].callback("reporter", "reporter")
    chat.send("Please Choose", attach=btns)


@bot.callback("reporter")
def callreporter_command(query, chat, message):
    btns = botogram.Buttons()
    btns[0].callback("it-jobs-in-ethiopia", "itreporter")
    btns[1].callback("construction-jobs-in-ethiopia", "conreporter")
    btns[2].callback("business-development", "busreporter")
    btns[3].callback("ngo-jobs-in-ethiopia", "ngoreporter")
    btns[4].callback("engineering-jobs-in-ethiopia", "engreporter")
    btns[5].callback("accounting-jobs-in-ethiopia", "accreporter")
    btns[6].callback("banking-jobs-in-ethiopia", "banreporter")
    btns[7].callback("fresh-graduate-jobs", "frereporter")
    chat.send("Please Choose", attach=btns)


@bot.command("reporter")
def reporter_command(chat, message, args):
    btns = botogram.Buttons()
    btns[0].callback("it-jobs-in-ethiopia", "itreporter")
    btns[1].callback("construction-jobs-in-ethiopia", "conreporter")
    btns[2].callback("business-development", "busreporter")
    btns[3].callback("ngo-jobs-in-ethiopia", "ngoreporter")
    btns[4].callback("engineering-jobs-in-ethiopia", "engreporter")
    btns[5].callback("accounting-jobs-in-ethiopia", "accreporter")
    btns[6].callback("banking-jobs-in-ethiopia", "banreporter")
    btns[7].callback("fresh-graduate-jobs", "frereporter")

    chat.send("Please Choose", attach=btns)


@bot.callback("ngoreporter")
def ngoreporter_callback(query, chat, message):
    msg = get_msg("ngo-jobs-in-ethiopia")
    query.notify("Recent Reporter Job")
    chat.send(msg)


@bot.callback("engreporter")
def engreporter_callback(query, chat, message):
    msg = get_msg("engineering-jobs-in-ethiopia")
    query.notify("Recent Reporter Job")
    chat.send(msg)


@bot.callback("accreporter")
def accreporter_callback(query, chat, message):
    msg = get_msg("accounting-jobs-in-ethiopia")
    query.notify("Recent Reporter Job")
    chat.send(msg)


@bot.callback("banreporter")
def banreporter_callback(query, chat, message):
    msg = get_msg("banking-jobs-in-ethiopia")
    query.notify("Recent Reporter Job")
    chat.send(msg)


@bot.callback("frereporter")
def frereporter_callback(query, chat, message):
    msg = get_msg("fresh-graduate-jobs")
    query.notify("Recent Reporter Job")
    chat.send(msg)


@bot.callback("itreporter")
def itreporter_callback(query, chat, message):
    msg = get_msg("it-jobs-in-ethiopia")
    query.notify("Recent Reporter Job")
    chat.send(msg)


@bot.callback("conreporter")
def conreporter_callback(query, chat, message):
    msg = get_msg("construction-jobs-in-ethiopia")
    query.notify("Recent Reporter Job")
    chat.send(msg)


@bot.callback("busreporter")
def busreporter_callback(query, chat, message):
    msg = get_msg("business-development")
    query.notify("Recent Reporter Job")
    chat.send(msg)


def get_msg(category):
    msg = "Recent Ethiopian Reporter Jobs\n\n {}\n\n".format(category)
    jobs = get_job(category)
    for job in jobs:
        msg += "no #{}\n job_details_link: {}\n job_title: {}\n job_company: {}\n job_type: {}\n job_location: {}\n job_experience_level: {}\n job_date_posted: {}\n job_date_closing: {}\n\n\n".format(
            job[0], job[1], job[2], job[3], job[4], job[5], job[6], job[7], job[8])

    return msg

# @bot.callback("reporter")
# def reporter_callback(query, chat, message):
#     msg = "Recent Ethiopian Reporter Jobs\n\n"
#     jobs = get_job("it-jobs-in-ethiopia")
#     for job in jobs:
#         msg += "no #{}\n job_details_link: {}\n job_title: {}\n job_company: {}\n job_type: {}\n job_location: {}\n job_experience_level: {}\n job_date_posted: {}\n job_date_closing: {}\n\n\n".format(
#             job[0], job[1], job[2], job[3], job[4], job[5], job[6], job[7], job[8])
#     # message.delete()
#     query.notify("Recent Reporter Job")
#     chat.send(msg)


if __name__ == "__main__":
    bot.run()
