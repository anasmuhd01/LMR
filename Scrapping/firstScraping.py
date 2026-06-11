from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://www.indeed.com/jobs?q=python+fresher")
time.sleep(5)

jobs = driver.find_elements(By.XPATH, "//h2[contains(@class,'jobTitle')]")
for _ in range(5):  # increase if needed
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

print("Jobs found:", len(jobs))

for job in jobs:
    try:
        title = job.text.strip()
        link_element = job.find_element(By.TAG_NAME, "a")
        link = link_element.get_attribute("href")

        if "python" in title.lower():
            print(title)
            print(link)
            print("-" * 40)

    except:
        continue

driver.quit()