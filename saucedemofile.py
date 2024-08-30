from selenium import webdriver
driver = webdriver.Chrome()
#extract the title of the web page
driver.get("https://www.saucedemo.com/")
title_page=driver.title
print("Title of the webpage::",title_page)
url=driver.current_url
print("Current URL::",url)
page_content = driver.page_source

# Save the content to a text file
with open('Webpage_task_11.txt', 'w', encoding='utf-8') as file:
    file.write(page_content)

print('Web page content has been saved to web_page_test.txt')