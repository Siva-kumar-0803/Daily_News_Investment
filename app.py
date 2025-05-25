import pywhatkit
import datetime
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

driver = webdriver.Chrome()
now = datetime.datetime.now()
URL = "https://www.goodreturns.in/gold-rates/chennai.html"
phone_number = "+919361958447"
hour = now.hour
minute = now.minute + 2  # Schedule the message to be sent 2 minutes later                                                                                                                                    
message = ""

def scrap_gold_prices():
    global message

    driver.get(URL)

    time.sleep(2)  # Wait for the page to load

    gold_prices = driver.find_elements(By.CLASS_NAME, "gold-common-head")

    for price in gold_prices:
        print(price.text)
        message += price.text +"\n"
      


def send_whatsapp_message(phone_number, message, hour, minute):
        
        try:
            pywhatkit.sendwhatmsg(phone_number, message, hour, minute)
            print(f"Message scheduled to be sent to {phone_number} at {hour}:{minute}.")

        except Exception as e:
            print(f"An error occurred: {e}")





def main():
    if now.strftime("%p") == "AM":
        scrap_gold_prices()
        driver.quit()  

        print("Gold prices scraped successfully.")

        send_whatsapp_message(phone_number, message, hour, minute)     

    else :
        print("It's not AM, so the message will not be sent.")
        # You can add any other logic here if needed   

        if __name__ == "__main__":
             main()