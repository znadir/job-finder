import time
from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import html2text

def searchJobs(search_url, jobOffersSelector, jobTitleSelector, jobLinkSelector, jobSnippetSelector, query, must_keywords):
    driver = webdriver.Firefox()
    driver.get(search_url + query.lower().replace(" ", "+"))

    driver.execute_script("window.scrollTo(0, 10000)")
    time.sleep(2)

    job_offers = driver.find_elements(By.CSS_SELECTOR, jobOffersSelector)

    my_jobs = []

    for job_offer in job_offers:
        try:
            title = html2text.html2text(job_offer.find_element(By.CSS_SELECTOR, jobTitleSelector).get_attribute('innerHTML')).replace("*","").replace("\n","").strip()
            link = job_offer.find_element(By.CSS_SELECTOR, jobLinkSelector).get_property("href")
            snippet = html2text.html2text(job_offer.find_element(By.CSS_SELECTOR, jobSnippetSelector).get_attribute('innerHTML')).replace("*","").replace("\n","").strip()

            for keyword in must_keywords:
                if keyword.lower() not in title.lower() + snippet.lower():
                    raise Exception("Doesn't include must keyword")

            my_jobs.append({
                'title': title,
                'link': link,
                'snippet': snippet
            })
        except:
            # not a job offer
            pass

    driver.close()

    return my_jobs