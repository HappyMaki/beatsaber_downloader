import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import os

chrome_options = Options()
chrome_options.add_argument("--headless")
# chrome_options.headless = True # also works

os.makedirs("beatmap_data")
os.makedirs("beatmap_songs")
os.makedirs("beatmap_temp")

def get_beat_saber_songs(search_query, n=40):
    driver = webdriver.Chrome("Drivers/chromedriver.exe", options=chrome_options)
    driver.get("https://beatsaver.com/")

    search_bar = driver.find_element_by_xpath("/html/body/main/form/div[1]/div[1]/input")
    search_bar.click()
    search_bar.send_keys(search_query)

    sort_by_select = Select(driver.find_element_by_xpath("/html/body/main/form/div[2]/div[4]/select"))
    sort_by_select.select_by_visible_text('Rating')

    search_button = driver.find_element_by_xpath("/html/body/main/form/div[1]/div[2]/button")
    search_button.click()

    time.sleep(5)

    result_num = len(driver.find_elements_by_class_name("beatmap"))
    print(result_num)
    final_urls = []
    if n > result_num:
        n = result_num
    for i in range(1, n):
        download_button = driver.find_element_by_xpath(f"/html/body/main/div[3]/div[{i}]/div[4]/a[4]")
        final_urls.append(download_button.get_attribute('href'))


    # time.sleep(5)
    driver.close()
    return final_urls

interesting_song_searches = ["kpop", "cpop", "jpop", "twice", "blackpink"]

urls = []
for search in interesting_song_searches:
    print(search)
    urls += get_beat_saber_songs(search)

urls = list(set(urls))
f = open(f"beatmap_data/urls.txt", "w")
for url in urls:
    f.write(url + "\n")
f.close()

