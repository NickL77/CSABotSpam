import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

options = Options()
driver = webdriver.Chrome(chrome_options=options)

driver.get("https://discord.com/channels/752041185115373689/753012712140963851")

a = str(input("Log into discord and select the channel to spam"))

while True:

    try:

        text_area = driver.find_element_by_xpath("//div[@data-slate-object='block']")
        text_area.send_keys("@Jack")
        text_area.send_keys(Keys.RETURN)
       
        time.sleep(0.2)
        text_area = driver.find_element_by_xpath("//div[@data-slate-object='block']")
        text_area.send_keys(Keys.RETURN)

        '''
        time.sleep(2)

        all_msg = driver.find_elements_by_xpath("//div[@class='contents-2mQqc9']")

        for msg in all_msg[::-1]:
            words = msg.text.split('\n')
            if len(words) > 1 and words[1] == "poof":
                poof_msg = msg
                break

        poof_msg.click()

        msg_options = poof_msg.find_element_by_xpath("//div[@aria-label='More']")
        msg_options.click()

        delete_btn = driver.find_element_by_xpath("//div[@id='message-actions-delete']")
        delete_btn.click()

        confirm_delete = driver.find_element_by_xpath("//button[@class='button-38aScr lookFilled-1Gx00P colorRed-1TFJan sizeMedium-1AC_Sl grow-q77ONN']")
        confirm_delete.click()

        print("deleted") 
        '''
    except Exception as e: 
        print("Something went wrong :(")
        print(e)
    
    time.sleep(120)
