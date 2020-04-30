#this is a python program to look for tesco slots
#next: add items to the shopping cart

import time
from selenium import webdriver
#pip3 install selenium, if not already installed

def booking_week(w):
    booking_tab=browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/div[1]/div/div[2]/div/div[2]/div/div[2]/div[2]/div[1]/ul/li['+str(w)+']/a')
    booking_tab.click()

    booking_message= browser.find_element_by_class_name('book-a-slot--info-message').text

    if 'No slots' not in booking_message:
        print ('there is a slot in week'+str(w)+', go book!')
    else:
        print ('week'+str(w)+':'+booking_message)
    
    #to handle the spinner after click
    time.sleep(5)

def main():
    
    #open chrome and go to the url
    global browser
    browser = webdriver.Firefox()

    #open bookings page
    browser.get('https://eshop.tesco.com.my/groceries/en-GB/slots/delivery')
    assert 'Sign in - Tesco' in browser.title
    #check the title of the page
    #if the title of the page has "Sign in - Tesco .." enter login info

    #email_addr
    username = browser.find_element_by_name('email')
    username.send_keys('arun.joshi@gmail.com')

    #passwd=
    passwd = browser.find_element_by_name('password')
    passwd.send_keys('joshi123')

    #click on the sign-in button. no buttong id or name, so use class name or xpath
    signin = browser.find_element_by_class_name('smart-submit-button')
    signin.click()

    #your taken to the bookings page
    #look for the tabs "Apr xx-xx". there are 3 tabs for 3 weeks
    #if not "no slot available" means, there is a slot
   
    #3 tabs for 3 weeks
    week_tabs=[1,2,3]

    for i in week_tabs:
        booking_week(i)
        i += 1

    #quit the browser
    browser.quit()

if __name__ == '__main__':
    main()
