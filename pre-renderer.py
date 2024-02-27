#Install essential libraries
#pip install selenium
#pip install opencv-python-headless
 
#importing essential libraries
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import cv2
import webbrowser
 
#Set up headless Chrome
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode
chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration
driver = webdriver.Chrome(options=chrome_options)
 
#URL to prerender 
url = "https://kwitter-two.vercel.app/"   #Replace the URL
 
#Navigate to the URL
driver.get(url)
 
#Wait for the page to fully render (you can adjust the time as needed)
driver.implicitly_wait(10)
 
#Capture the rendered HTML
rendered_html = driver.page_source
 
# Close the browser
driver.quit()
 
#Saving the generated html code to file
file_path= "generated_file"
with open(file_path,"w") as file:
    file.write(rendered_html)
 
#Opening the generated html file
webbrowser.open_new_tab(file_path)