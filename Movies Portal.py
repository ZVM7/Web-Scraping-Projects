from selenium import webdriver
import pandas as df

url = "https://doramalive.ru/dorama/?mode=all"
driver = webdriver.Chrome(executable_path=r'C:\Users\zura_\Desktop\chromedriver.exe')
driver.get(url)



def Check_movies():
    title = []
    ratings = []

    for i in range(5):


        Button = driver.find_element_by_xpath('//ul[@class="pagination"]')
        Next_page = Button.find_element_by_class_name('modern-page-next')
        Next_page.click()

        All_info = driver.find_element_by_xpath('//div[@class="row row-flex media-list"]')
        all_the_cubes = All_info.find_elements_by_xpath('.//div[@class="col-md-6"]')


        for info in all_the_cubes:
            title.append(info.find_element_by_class_name("media-heading").text.replace("#",""))
            ratings.append(info.find_element_by_class_name("media-rating").text.strip())

        Dorama = df.DataFrame({"Title": title, "Ratings": ratings})





s = Check_movies()
