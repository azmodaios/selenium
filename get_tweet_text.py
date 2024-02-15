from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta

def login(user, password):
    driver.get("https://twitter.com")
    sleep(2)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[href="/login"]'))).click()
    acc = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="session[username_or_email]"]'))).send_keys(user)
    sleep(2)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="session[password]"]'))).send_keys(password)
    sleep(3)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[data-testid="LoginForm_Login_Button"]'))).click()
    sleep(3)

tweet_list = []
def get_tweets(since, until, account):
    since_date = datetime.strptime(since, '%Y-%m-%d')
    until_date = datetime.strptime(until, '%Y-%m-%d')
    actual_date = since_date
    tweet_list = []
    while actual_date <= until_date:
        started = actual_date.strftime('%Y-%m-%d')
        actual_date += timedelta(days=1)
        print(f"started_at :{started} and finish at :{actual_date.strftime('%Y-%m-%d')}")
        driver.get(
            f"https://twitter.com/search?q=(from%3A{account})%20until%3A{actual_date.strftime('%Y-%m-%d')}%20since%3A{started}%20-filter%3Alinks%20-filter%3Areplies&src=typed_query")
        sleep(8)
        tweet_tag = driver.find_elements(By.CSS_SELECTOR, "article")

        for tweet in tweet_tag:
            sleep(1)
            data = tweet.text
            tweet_list.append(data)
    print(tweet_list)
    driver.quit()
    return tweet_list

# login
user = '*****' # your username
password = '*****' # your password

# search
since = '2023-01-01' # change me
until = '2023-12-31' # change me
account = '*****' # the target username

login(user, password)
result = get_tweets(since, until, account)
print(result)
