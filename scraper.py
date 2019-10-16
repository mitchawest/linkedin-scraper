from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import json
import os

from parse_certifications import certifications_parser
from parse_education import education_parser
from parse_experience import experience_parser
from parse_recommendations import recommendations_parser
from parse_skills import skills_parser
from uploader import upload_to_aws_s3

try:
    # set options and driver for selenium webdriver
    path = os.path.realpath('./chromedriver')
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(path, options=chrome_options)
    driver.implicitly_wait(30)

    # populate login page and submit credentials
    login_url = 'https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin'
    driver.get(login_url)
    username = driver.find_element_by_name('session_key')
    password = driver.find_element_by_name('session_password')
    username.send_keys(os.environ['LI_USER_EMAIL'])
    password.send_keys(os.environ['LI_USER_SECRET'])
    driver.find_element_by_css_selector(
        'div.login__form_action_container >button').click()

    # navigate to proflie page scroll to bottom to load all elements and click show more on skills
    page_url = os.environ['LI_USER_URL']
    driver.get(page_url)
    time.sleep(5)
    driver.execute_script(
        "window.scrollTo(0, document.body.scrollHeight * .5);")
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

    # scroll show more skills button into view and click
    show_more_button = driver.find_element_by_css_selector(
        'button.pv-profile-section__card-action-bar.pv-skills-section__additional-skills')
    webdriver.ActionChains(driver).move_to_element(
        show_more_button).click(show_more_button).perform()

    # scroll recommendations into view and click show more button on each
    see_more_buttons = driver.find_elements_by_css_selector(
        'blockquote.pv-recommendation-entity__text>div>span>span>a.lt-line-clamp__more')
    for link in see_more_buttons:
        webdriver.ActionChains(driver).move_to_element(
            link).click(link).perform()

    # send page source to beautiful soup parsers and close driver
    source = driver.page_source
    driver.close()
    certifications = certifications_parser(source)
    education = education_parser(source)
    experience = experience_parser(source)
    recommendations = recommendations_parser(source)
    skills = skills_parser(source)

    # build user object and write to Mongo
    linkedin_data = {
        'experience': experience,
        'education': education,
        'recommendations': recommendations,
        'skills': skills,
        'certifications': certifications
    }

    upload_to_aws_s3(json.dumps(linkedin_data),
                     os.environ['AWS_S3_BUCKET'], os.environ['AWS_S3_FILEPATH'])

    print('Done')
except Exception as e:
    print('Exception: ' + e)
