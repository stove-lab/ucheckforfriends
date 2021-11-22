# ucheckforfriends
An edited version of the auto-ucheck program made by irahorecka for personal use.

# Disclaimer
ucheck automatically completes the University of Tornto's UCheck COVID-19 self-assessment form as follows:
- YES: "Do any of the following statements apply to you? - I am fully vaccinated against COVID-19."
- NO: "Are you currently experiencing any of these symptoms? - Fever and/or chills (Temperature of 37.8 degrees Celsius/100 degrees Fahrenheit or higher)."
- NO: "Is anyone you live with currently experiencing any new COVID-19 symptoms and/or waiting for test results after experiencing symptoms?"
- NO: "In the last 14 days, have you travelled outside of Canada and been told to quarantine (per the federal quarantine requirements)?"
- NO: "Has a doctor, health care provider, or public health unit told you that you should currently be isolating (staying at home)?"
- NO: "In the last 10 days, have you been identified as a "close contact" of someone who currently has COVID-19?"
- NO: "In the last 14 days, have you received a COVID Alert exposure notification on your cell phone?"
- NO: "In the last 10 days, have you tested positive on a rapid antigen test or home-based self-testing kit?"

If you do not satisfy these questions as listed, DO NOT use this library to complete your UCheck form. 

## Prerequisite Installations
To use this program, you will need to have:
- Python 3.9 https://www.python.org/downloads/release/python-390/ 

- Selenium
  - If you have python installed, you can run: 
  - On Mac terminal:
  ```bash
  pip install selenium
  ```
  - On Windows command prompt:
  ```bash 
  python -m pip install selenium
  ```
  
- ChromeDriver https://chromedriver.chromium.org/downloads
  - You can check your Chrome version in Settings -> About Chrome
  - Create a new folder e.g. (WebDriver) to hold your chromedriver executable file. Remember the path for this driver as it will be used to edit the code later.

- Any Python compiler e.g. Pycharm, Wing IDE. 
  
## Setup
- Download all the files in the ucheckforfriends directory.
- Add environment variables with the names `UTORID_USER` and `UTORID_PASS`. Set their values to your personal utorid and password respectively. 
  - On Windows: https://www.architectryan.com/2018/08/31/how-to-change-environment-variables-on-windows-10/ 
  - On Mac: Open Terminal -> type `touch ~/.bash_profile` -> type `open ~/.bash_profile`
  - At the bottom of your bash file, add: 
  ```bash
  # Environment Variables for UTORID information
  UTORID_USER = "enter your utorid here"
  UTORID_PASS = "enter your password here"
  ```
  (keep the quotes)
  
 - Then save the file and close it.
  
- In your main.py, change the value inside the quotes for `driver_path` to the path to your chromedriver.exe:

```python
with UCheck(Chrome, Service, driver_path="/opt/WebDriver/bin/chromedriver") as ucheck:
```

- In your config.yaml file, change the value of `ucheck-url` to the url of your questionnaire. 

## How to Use
- Run the `main.py` file in your compiler of choice.
