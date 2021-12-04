from selenium import webdriver     
  
# For using sleep function because selenium 
# works only when the all the elements of the 
# page is loaded.
import time 
   
from selenium.webdriver.common.keys import Keys 

# Creating an instance webdriver
browser = webdriver.Edge()
browser.maximize_window()
browser.get('https://www.youtube.com/')

try:
  
    # Let's the user see and also load the element 
    time.sleep(1)
    
    input = browser.find_elements_by_xpath('//*[@id="search"]')
    input[1].send_keys("NF - The Search")

    while True:
        try: 
            print("searching for nf search videos")
            searchButton = browser.find_element_by_xpath('//*[@id="search-icon-legacy"]')
            searchButton.click()
            break
        except:
            time.sleep(0.4)

    while True:
        try: 
            print("selecting for nf search videos")
            videos = browser.find_elements_by_xpath('//*[@id="contents"]/ytd-video-renderer')
            videos[0].click()
            break
        except:
            time.sleep(0.4)

    
    for i in range(4):
        while True:
            try: 
                print("searching for new video")
                newVideos = browser.find_elements_by_xpath('//*[@id="items"]/ytd-compact-video-renderer')
                newVideos[3].click()
                time.sleep(2)
                break
            except:
                time.sleep(0.4)

except KeyboardInterrupt as e:
    print(str(e))

# closing the browser
browser.close()
exit(0)