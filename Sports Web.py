from selenium import webdriver
import pandas as dt

url = "https://www.adamchoi.co.uk/overs/detailed"
driver = webdriver.Chrome(executable_path=r'C:\Users\zura_\Desktop\chromedriver.exe')
driver.get(url)

all_matches_button = driver.find_element_by_xpath('//label[@analytics-event="All matches"]')
all_matches_button.click()

matches = driver.find_elements_by_tag_name("tr")

date = []
home_team = []
score = []
away_team = []

for match in matches:
    date.append(match.find_element_by_xpath('./td[1]').text)
    home_team.append(match.find_element_by_xpath('./td[2]').text)
    score.append(match.find_element_by_xpath('./td[3]').text)
    away_team.append(match.find_element_by_xpath('./td[4]').text)
driver.quit()

Frame = dt.DataFrame({"Date": date,"Home Team": home_team,"Score": score,"Away Team": away_team})
Frame.to_csv("Football_Date.csv",index=False)
print(Frame)
