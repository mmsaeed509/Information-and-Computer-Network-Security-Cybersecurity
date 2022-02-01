# system libraries
import os
import random
import time
# selenium libraries
from email.mime import audio
from idlelib.multicall import r

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# recaptcha libraries
import speech_recognition as sr
import urllib
import pydub

'''

Go to the Recaptcha website

'''


def delay():
    time.sleep(random.randint(2, 3))


try:
    # create chrome driver
    driver = webdriver.Chrome(os.getcwd() + "chromedriver")
    delay()
    # go to website
    driver.get("https://www.google.com/recaptcha/api2/demo")

except:
    print("[-] Please update the chromedriver")

'''

Find the Recaptcha frame and click on the audio challenge

'''
# switch to recaptcha frame
frames = driver.find_elements_by_tag_name("iframe")
driver.switch_to.frame(frames[0]);
delay()
# click on checkbox to activate recaptcha
driver.find_element_by_class_name("recaptcha-checkbox-border").click()
# switch to recaptcha audio control frame
driver.switch_to.default_content()
frames = driver.find_element_by_xpath("/html/body/div[2]/div[4]").find_elements_by_tag_name("iframe")
driver.switch_to.frame(frames[0])
delay()
# click on audio challenge
driver.find_element_by_id("recaptcha-audio-button").click()
# switch to recaptcha audio challenge frame
driver.switch_to.default_content()
frames = driver.find_elements_by_tag_name("iframe")
driver.switch_to.frame(frames[-1])
delay()
# click on the play button
driver.find_element_by_xpath("/html/body/div/div/div[3]/div/button").click()

'''

Download audio challenge MP3 file

'''

# get the mp3 audio file
src = driver.find_element_by_id("audio-source").get_attribute("src")
print("[INFO] Audio src: %s" % src)
# download the mp3 audio file from the source
urllib.request.urlretrieve(src, os.getcwd() + "/sample.mp3")

'''

Convert from MP3 to WAV format

'''

sound = pydub.AudioSegment.from_mp3(os.getcwd() + "/sample.mp3")
sound.export(os.getcwd() + "/sample.wav", format="wav")
sample_audio = sr.AudioFile(os.getcwd() + "/sample.wav")

'''

Use Google speech to text API to decipher audio challenge

'''

# translate audio to text with google voice recognition
key = r.recognize_google(audio)
print("[INFO] Recaptcha Passcode: %s" % key)

'''

Fill in the Recaptcha passcode and press verify

'''

# key in results and submit
driver.find_element_by_id("audio-response").send_keys(key.lower())
driver.find_element_by_id("audio-response").send_keys(Keys.ENTER)
driver.switch_to.default_content()
delay()
driver.find_element_by_id("recaptcha-demo-submit").click()
delay()
