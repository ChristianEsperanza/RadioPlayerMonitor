# Imports, we are going to use Firefox but you
# can use any browser
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import time
import smtplib, ssl

playerUrl = 'https://www.jrcountry.ca/player/?playerID=825'

driver = webdriver.Chrome()
driver.get(playerUrl)

now_playing = driver.find_element(By.ID, 'hero')
artist= now_playing.find_element(By.CLASS_NAME, 'artist')
song = now_playing.find_element(By.CLASS_NAME, 'song')

print(artist.text)

finished = False

# Click on element ID = playerOVerlay


while not finished:
    if len(driver.find_elements(By.ID, 'playerOverlay')) !=0:
        driver.find_element(By.ID, 'playerOverlay').click()
    time.sleep(2)
    
    now_playing = driver.find_element(By.ID, 'hero')
    artist= now_playing.find_element(By.CLASS_NAME, 'artist')
    song = now_playing.find_element(By.CLASS_NAME, 'song')
    print(artist.text, " - ", song.text)
    
    if "Taylor Swift" in artist.text:
        print("Found taylor")
        finished = True
        break
    
    time.sleep(7)
    driver.refresh()
    

# Send email
port = 465  # For SSL
password = "{find this in google apps}"

# Create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login("my_email@gmail.com", password)
    sender_email = "my_email@gmail.com"
    receiver_emails = ["my_email@gmail.com", "email2@gmail.com"]
    
    message = f"""\
    Subject: Taylor Swift playing on the radio 

    {artist.text} - {song.text} is currently playing, text the word TAYLOR, your name, and city to 604-280-9370"""
    
    server.sendmail(sender_email, receiver_emails, message)
    
    
print("finished")
