from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import pandas as pd
import urllib.request
from PIL import Image
import numpy as np
import imageio
import matplotlib.pyplot as plt
import requests
from selenium import webdriver
import time
from stats import yeet
thumbnails = []
results = []




def scrape_channel():
    driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')

    def yeet(href):
        try:
            driver.get(href)
            time.sleep(2)
            driver.execute_script("window.scrollBy(0,100)")
            try:
                driver.find_element_by_xpath('//*[@id="text"]').click()
            except:
                pass
            show_more = driver.find_element_by_xpath(
                '/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/div[8]/div[3]/ytd-video-secondary-info-renderer/div/ytd-expander/paper-button[2]/yt-formatted-string')
            show_more.click()
            time.sleep(1)
            title = driver.find_elements_by_xpath(
                '/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/div[7]/div[2]/ytd-video-primary-info-renderer/div/h1/yt-formatted-string')[
                0].text

            views = driver.find_element_by_xpath(
                '/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/div[7]/div[2]/ytd-video-primary-info-renderer/div/div/div[1]/div[1]/yt-view-count-renderer/span[1]').text
            desc = driver.find_element_by_xpath(
                '/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/div[8]/div[3]/ytd-video-secondary-info-renderer/div/ytd-expander/div/div/yt-formatted-string')
            likes = driver.find_element_by_xpath(
                '/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/div[7]/div['
                '2]/ytd-video-primary-info-renderer/div/div/div['
                '3]/div/ytd-menu-renderer/div/ytd-toggle-button-renderer[1]/a')
            dislikes = driver.find_element_by_xpath(
                '/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/div[7]/div[2]/ytd-video-primary-info-renderer/div/div/div[3]/div/ytd-menu-renderer/div/ytd-toggle-button-renderer[2]/a')
            print(dislikes.text)
            results.append({
                'title': title,
                'url': href,
                'views': views,
                'description': desc.text,
                'likes': likes.text,
                'dislikes': dislikes.text
            })
        except Exception as e:
            print(e)

    driver.get('https://www.youtube.com/AphmauGaming/videos')
    screen_height = driver.execute_script("return window.screen.height")
    i = 1
    while True:
        i += 1
        tmp = len(thumbnails)
        for video in driver.find_elements_by_id("thumbnail"):
            try:
                if video.get_attribute('href') not in thumbnails:
                    thumbnails.append(video.get_attribute('href'))
            except:
                pass
        print(len(thumbnails))
        driver.execute_script(f"window.scrollBy(0,{screen_height} * {i})")

        time.sleep(2)
        if tmp == len(thumbnails):
            break
    count = 0
    for href in thumbnails:
        yeet(href)
        print(str(count) + " / " + str(len(thumbnails)))
        count += 1
    df = pd.DataFrame(results)
    df.to_csv("results.csv")

