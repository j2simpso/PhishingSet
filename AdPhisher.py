#from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
from selenium import webdriver
import time


# Load in Google queries
# For each query:
#    run it on Google
#   for each Ad in the DOM:
#       inspect URL - does it match intended URL?
#       inspect Title - does it claim to represent third party
#       inspect Coontent - is it scammy?
#       is displayURL significantly different from actual URL?
#       if Yes :
#           Capture Screenshot
#           Capture Ad Detils
#           Generate Report
#    Sleep by 30 seconds

browser = webdriver.Safari()
browser.get("https://www.google.com/search?client=safari&rls=en&q=rental+cars&ie=UTF-8&oe=UTF-8")

elements = browser.find_elements_by_class_name("ads-ad")

for element in elements:
    print element.find_element_by_css_selector("[class$=ads-creative]")
#def setLocMobile(lat, lon):


#def runFromMobile():

#def runFromDesktop():
