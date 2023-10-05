from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from cryptography.fernet import Fernet
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time, os, datetime, requests



__version__ = '1.5'

if os.path.isfile("version.txt") == True:
    with open("version.txt","w") as f:
        f.write(__version__)

else:
    with open("version.txt","a+") as f:
        f.write(__version__)




response = requests.get('https://raw.githubusercontent.com/JerryIT1/CID-Creation/main/version.txt')
data = response.text


if float(data) > float(__version__):
    print('Update Available')
    print('App needs to update from '+__version__+ ' to '+data)
    update = input("Would you like to update now? (Y/N)")
    update = update.upper()
    if update in ('Y', 'YES'):

        options = Options() 
        path = os.getcwd()
        
        prefs = {"download.default_directory" : path}
        options.add_experimental_option("prefs", prefs)

        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        driver.get('https://github.com/JerryIT1/CID-Creation/releases/download/v'+data+'/workday.exe')
        #if os.path.isfile("workday.exe") == True:
        #    os.rename('workday.exe', 'OLD workday.exe')
        time.sleep(500)
        
        exit()
    else:
        os.system('cls')
        print('When you want to update just run the program again :)')


# In order to run you will need to have chromedriver in the same folder, or set the file path so it can access it

x = datetime.datetime.now()
currentYear = x.year
strYear = str(currentYear)
prevYear = x.year -1
strPrevYear = str(prevYear)


if x.month in (1,2,3):
    newDate = "1001"+strPrevYear
elif x.month in (4,5,6):
    newDate = "0101"+strYear
elif x.month in (7,8,9):
    newDate = "0401"+strYear
elif x.month in (10,11,12):
    newDate = "0701"+strYear

# Prompts user to input their username and password. 
# Can store to a text file so it wont prompt every time
# or could completely remove this portion to have it
# wait for manual input so it never sees the username/password.

print(__version__)

if os.path.isfile("login.txt") == True:
    os.system( "attrib -h login.txt" )
    os.system( "attrib -h filekey.key" )
    with open('filekey.key', 'rb') as filekey:
        key = filekey.read()
    fernet = Fernet(key)
    with open('login.txt', 'rb') as enc_file:
        encrypted = enc_file.read()
    decrypted = fernet.decrypt(encrypted)
    with open('login.txt', 'wb') as dec_file:
        dec_file.write(decrypted)


    with open("login.txt", "r") as f:
        loginCreds = f.readline()
    loginCreds = loginCreds.split("---")
    username = loginCreds[0]
    password = loginCreds[1]

    key = Fernet.generate_key()
    with open('filekey.key', 'wb') as filekey:
        filekey.write(key)
    with open('filekey.key', 'rb') as filekey:
        key = filekey.read()
    fernet = Fernet(key)
    with open('login.txt', 'rb') as file:
        original = file.read()
    encrypted = fernet.encrypt(original)
    with open('login.txt', 'wb') as encrypted_file:
        encrypted_file.write(encrypted)
    
    os.system( "attrib +h login.txt" )
    os.system( "attrib +h filekey.key" )

else:
    username = input("Enter username to login\n")
    password = input("Enter Password to login\n")
    with open("login.txt","a+") as f:
        f.write(username+'---')
        f.write(password)

    key = Fernet.generate_key()
    with open('filekey.key', 'wb') as filekey:
        filekey.write(key)
    with open('filekey.key', 'rb') as filekey:
        key = filekey.read()
    fernet = Fernet(key)
    with open('login.txt', 'rb') as file:
        original = file.read()
    encrypted = fernet.encrypt(original)
    with open('login.txt', 'wb') as encrypted_file:
        encrypted_file.write(encrypted)

    os.system( "attrib +h login.txt" )
    os.system( "attrib +h filekey.key" )



answer = "NO"
os.system('cls')

print(__version__)


while answer not in ('Y', 'YES'):

    if answer == "N" or answer =="NO":
        facility = input("Enter facility in simple words (ex. If facility is HealthCare Resort of Plano. Enter \"Plano\")\n")
        position = input("\n\nEnter abreivated position name (ex. CNA/LVN/RN)\n")
        position = position.upper()
        name = input("\n\nEnter first and last name of agency (ex. Berman Nowlin)\n")
        phone = input("\n\nEnter the phone number associated with the facility\nIf you do not know the phone number you can find it here: https://ensign.zendesk.com/hc/en-us/articles/5221745419667\n")
    

    os.system('cls')
    print("\n\n"+name+" is an "+position+" at "+facility+"\n")
    answer = input("Correct? (Y/N)\n")
    answer = answer.upper()
    if answer == "Y" or answer == "YES":
        print("Creating CID...")
    elif answer == "N" or answer == "NO":
        os.system('cls')
    else: 
        print("\nI didnt quite catch that.\n Answer with Yes or No")




if name.find("`") == -1:
    name = name.split(" ")
    fname = name[0]
    try:
        lname = name[1]
    except IndexError:
        errorGot = input("\n\nMake sure you put a space between the first and last name\nPress Enter to close then run it again...")
        exit()
else: 
    name = name.split("`")
    fname = name[0]
    try:
        lname = name[1]
    except IndexError:
        errorGot = input("\n\nMake sure you put a space between the first and last name\nPress Enter to close then run it again...")
        exit()









# Defines which browser to use
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()


# Tells driver where to load when first initiated
driver.get('https://www.myworkday.com/ensign/d/inst/13102!CK5mGhIKBggDEMenAhIICgYI1A0QjgI~*FjkLA8iZuyM~/cacheable-task/23748$16.htmld#backheader=true&TABINDEX=0')

def login():

    # Waits until it can find the "username" input. Works like windows file explorer ex. C:\Users\Berman\Desktop. Goes into html, then into body, then into the first div etc.
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div/div[1]/div/div[1]/div[3]/div[1]/div/input"))).send_keys(username)


    # Waits until it can find the "password" input
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div/div[1]/div/div[1]/div[3]/div[2]/div/input"))).send_keys(password)

    # Clicks the "submit" button to submit username and password
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div/div[1]/div/div[1]/div[3]/button"))).click()



    #print(WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div/div[1]/div/div[1]/div[3]/button"))))
    time.sleep(0.5)
    try:
        if driver.find_element(By.XPATH, "//div[contains(text(),'Invalid user name')]"):
            driver.close()
            os.remove("login.txt")
            os.remove("filekey.key")
            os.system("cls")
            end = input("Hey! Your password was either changed recently, or was entered incorrectly. Go ahead and press and close this page and when you re-open it will prompt for username and password\n")
            time.sleep(0.5)
            exit()
    except:
        print("")

    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div/div[2]/div/div/div[2]/a"))).click()


    print('logged in\n')
    


def create_position():
    print("Started Creating Position")
    # Opens Create Position Menu (Takes longer to load depending on internet speed, so it will load nonstop until it works or is closed)
    while True:
        try:
            WebDriverWait(driver, 180).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div[2]/div[1]/section/div/div/div/div[1]/div/div[2]/div/div[2]/div/div/div[2]/div/div[4]/div/div/div/div[2]/div/div[1]/ul/li[1]/div"))).click()
        except:
             continue
        else:
         break




    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div[2]/div[1]/section/div/div/div/div[1]/div/div[2]/div/div[2]/div/div/div[2]/div/div[4]/div/div/div/div[2]/div/div[1]/ul/li[1]/div"))).click()
    
    # Finds search bar and inputs facility that was inputted by end-user


    while True:
        try:
            elem = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[11]/div/div[2]/div/div[2]/div/div/ul/li/div[2]/div/div/div/div/div/div/input")))
            time.sleep(0.5)
            elem.send_keys('nursing '+facility)
            time.sleep(0.5)
            elem.send_keys(Keys.ENTER)
        except:
             continue
        else:
         break

    

    # Not going to have the bot click "submit" just in case facility has multiple options


    # Selects PBJ based worker
    while True:
        try:
            elem = WebDriverWait(driver, 180).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div/div[2]/div[1]/section/div[1]/div/div/div[1]/div/div/ul/li[2]/div[2]/div/div/div/div/div/div/input")))
            elem.send_keys("PBJ")
            elem.send_keys(Keys.ENTER)
        except:
             continue
        else:
         break

    
    # Enters position and start date (Right now its hard coded but will be later adjusted with time)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div/div[2]/div[1]/section/div[1]/div/div/div[1]/div/div/ul/li[3]/div[2]/div[1]/div/input"))).send_keys("Agency."+position)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div/div[2]/div[1]/section/div[1]/div/div/div[2]/div/div[2]/div/div[2]/div[1]/div/div/div/ul/li[1]/div[2]/div/div/div/div[2]/div[1]/div[1]/input"))).send_keys(newDate)
    
    # This is for the second start date 
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div/div[2]/div[1]/section/div[1]/div/div/div[2]/div/div[2]/div/div[2]/div[1]/div/div/div/ul/li[2]/div[2]/div/div/div/div[2]/div[1]/div[1]/input"))).send_keys(newDate)
    time.sleep(1)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div/div[2]/div[1]/section/div[1]/div/div/div[2]/div/div[2]/div/div[2]/div[1]/div/div/div/ul/li[2]/div[2]/div/div/div/div[2]/div[1]/div[1]/input"))).send_keys(newDate)
 
    # Enters job profile (Cant find Contingent LPN, so I set it to LVN)
    elem = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div/div[2]/div[1]/section/div[1]/div/div/div[2]/div/div[2]/div/div[2]/div[1]/div/div/div/ul/li[6]/div[2]/div/div/div/div/div/div/input")))
    if position == "LPN":
        elem.send_keys("contingent LVN")
    else:
        if position == "LVN":
            elem.send_keys("contingent (9)")
        else:
            elem.send_keys("contingent "+position)
    elem.send_keys(Keys.ENTER)
    time.sleep(2)

    # Enters worker type
    elem = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div/div[2]/div[1]/section/div[1]/div/div/div[2]/div/div[2]/div/div[2]/div[1]/div/div/div/ul/li[11]/div[2]/div/div/div/div/div/div/input")))
    elem.send_keys("contingent")
    elem.send_keys(Keys.ENTER)

    # Enters Facility, Made it so end user selects the actualy facility incase there are multiple

    while True:
        try:
            elem = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div/div[2]/div[1]/section/div[1]/div/div/div[2]/div/div[2]/div/div[2]/div[1]/div/div/div/ul/li[9]/div[2]/div/div/div/div/div/div/input")))
            elem.send_keys(facility)
            time.sleep(0.5)
            elem.send_keys(Keys.ENTER)
        except:
             continue
        else:
         break
    
    print("Finished creating position")




    # I wont make bot submit the page and will let end-user look over what has been entered before being prompted to continue


def create_worker():
    print("Started creating worker")
    while True:
        try:
            WebDriverWait(driver, 180).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div[2]/div[1]/section/div/div/div/div[1]/div/div[2]/div/div[2]/div/div/div[2]/div/div[4]/div/div/div/div[2]/div/div[1]/ul/li[2]/div"))).click()
        except:
            continue
        else:
            break


    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[11]/div/div[2]/div/div[2]/div/div/ul/li[2]/div[2]/div/div/div/div[2]/div/div/span/input"))).click()

    while True:
        try:
            elem = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[11]/div/div[2]/div/div[2]/div/div/ul/li[1]/div[2]/div/div/div/div/div/div/input")))
            time.sleep(0.5)
            elem.send_keys('nursing '+facility)
            time.sleep(0.5)
            elem.send_keys(Keys.ENTER)
        except:
             continue
        else:
         break

    



    
    while True:
        try:
            WebDriverWait(driver, 180).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div/div[2]/div[1]/section/div[1]/div/div/div[1]/div/div/ul/li[5]/div[2]/div/div/div"))).click()
            
        except:
            continue
        else:
            break

    while True:
        try:
            WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div/div[2]/div[1]/section/div[1]/div/div/div[2]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div/ul/li[2]/div[2]/div/div/input"))).send_keys(fname)
        except:
            continue
        else:
            break
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div/div[2]/div[1]/section/div[1]/div/div/div[2]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div/ul/li[4]/div[2]/div/div/input"))).send_keys(lname)

    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div/div[2]/div[1]/section/div[1]/div/div/div[2]/div/div[2]/div/div[1]/ul/li[2]"))).click()
    
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div/div[2]/div[1]/section/div[1]/div/div/div[2]/div/div[2]/div/div[2]/div[2]/div/div/div/div[1]/div/button"))).click()

    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div/div[2]/div[1]/section/div[1]/div/div/div[2]/div/div[2]/div/div[2]/div[2]/div/div/div/div[1]/div/ul/li/div/div/div[2]/div/div/div/ul/li[2]/div[2]/div/div/input"))).send_keys(phone)
   

    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div/div[2]/div[1]/section/div[1]/div/div/div[2]/div/div[2]/div/div[2]/div[2]/div/div/div/div[1]/div/ul/li/div/div/div[2]/div/div/div/ul/li[5]/div[2]/div[1]/div/div/div/div/div/input"))).send_keys("work")

    
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div/div[2]/div[1]/section/div[1]/div/div/div[2]/div/div[2]/div/div[2]/div[2]/div/div/div/div[1]/div/ul/li/div/div/div[2]/div/div/div/ul/li[4]/div[2]/div[1]/div"))).click()
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div/div[2]/div[1]/section/div[1]/div/div/div[2]/div/div[2]/div/div[2]/div[2]/div/div/div/div[1]/div/ul/li/div/div/div[2]/div/div/div/ul/li[4]/div[2]/div[1]/div"))).click()
    time.sleep(0.5)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[11]/div[1]/ul/li[3]"))).click()
    


    while True:
        try:
            WebDriverWait(driver, 180).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div/div[2]/div[1]/section/div[1]/div/div/div[1]/div/div/ul/li[1]/div[2]/div/div/div/div[2]/div[1]/div[1]/input"))).send_keys(newDate)
        except:
            continue
        else:
            break
    elem = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div/div[2]/div[1]/section/div[1]/div/div/div[1]/div/div/ul/li[2]/div[2]/div[1]/div/div/div/div/div/input")))
    elem.send_keys("new position")
    time.sleep(0.5)
    elem.send_keys(Keys.ENTER)
    while True:
        try:
            WebDriverWait(driver, 180).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[11]/div[1]/div/div[2]/div/div[1]/div/div/div[1]"))).click()
        except:
            continue
        else:
            break

    elem = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div/div[2]/div[1]/section/div[1]/div/div/div[1]/div/div/div[1]/div/div[2]/div/ul/li[1]/div[2]/div/div/div/div/div/div/input")))
    elem.send_keys("Agency."+position)
    elem.send_keys(Keys.ENTER)
    time.sleep(1)




    elem = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div/div[2]/div[1]/section/div[1]/div/div/div[1]/div/div/div[1]/div/div[2]/div/ul/li[4]/div[2]/div/div/div/div/div[1]/div/input")))
    elem.send_keys("Part Time")
    elem.send_keys(Keys.ENTER)

    elem = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div/div[2]/div[1]/section/div[1]/div/div/div[1]/div/div/div[1]/div/div[2]/div/ul/li[2]/div[2]/div/div/div/div/div[1]/div/input")))
    elem.send_keys("Agency/Registry")
    time.sleep(1)
    elem.send_keys(Keys.ENTER)

    # Stop the code so you can add cost center 
    os.system('cls')
    print("CID has been created. Use this time to add cost center and copy CID from workday")
    time.sleep(50000)
    driver.close()


login()
create_position()
create_worker()
                             