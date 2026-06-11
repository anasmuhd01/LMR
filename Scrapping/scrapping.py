from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

driver.get("https://technopark.in/company-list")

# Wait until companies load
wait.until(
    EC.presence_of_element_located((By.XPATH, "//a[contains(@href,'company-details')]"))
)

companies = driver.find_elements(By.XPATH, "//a[contains(@href,'company-details')]")

print("Companies found (initial):", len(companies))

for c in companies:
    try:
        name = c.find_element(By.TAG_NAME, "h4").text
        link = c.get_attribute("href")

        driver.get(link)

        # 🔽 Click "Contact Company"
        try:
            contact = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//p[contains(text(),'Contact Company')]"))
            )
            contact.click()
        except:
            pass

        # 🔍 Get ALL email elements
        emails = driver.find_elements(By.XPATH, "//a[contains(@href,'mailto:')]")

        # ✅ Pick ONLY visible email
        real_email = None
        for e in emails:
            if e.is_displayed():
                real_email = e.text
                break

        if real_email:
            print(name, "→", real_email)
        else:
            print(name, "→ No email found")

        driver.back()

    except:
        continue

driver.quit()