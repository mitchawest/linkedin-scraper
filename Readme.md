# linked-scraper

This is a simple python web scraper to pull my linkedin details from my profile and update an Amazon Web Services (AWS) S3 file with the JSON details. This allows my personal website to stay updated with all of the details from my linkedin page so that I don't have to update both separately.

# Packages

  - Selenium: for emulating user browser behavior using headless chrome
  - BeautifulSoup: for parsing the extracted page source and grabbing specific profile details
  - Boto3: for publishing the extracted details to an AWS S3 instance. A React app will read from S3 to populate personal page details.

# To Use

Required environment variables:
  - LI_USER_URL: page url of linkedin profile
  - LI_USER_EMAIL: linkedin login user email
  - LI_USER_SECRET: linkedin login user password
  - AWS_APP_ID: AWS application access ID
  - AWS_APP_SECRET: AWS application access secret key
  - AWS_S3_BUCKET: AWS S3 bucket name
  - AWS_S3_FILEPATH: AWS S3 file put path
  - LI_RECOMMENDEE_NAME: Was originally unable to parse recommendations given vs received this filters only the recommendations that include the desired user's name in the recommendation body.

Scripts:
  - Prior to running:
    - pip install selenium
    - pip install boto3
    - pip install bs4
  - To run:
    - python scraper.py

### Todos
  - add hooks to deploy to EC2

