from pyvirtualdisplay import Display
from selenium import webdriver
from actions import *

display = Display(visible = 0, size = (800, 600))
display.start()

driver = webdriver.Firefox()
file_ = open("../lit_not_spanish.txt")

lit_not_spanish = file_.read()
file_.close()

#print(lit_not_spanish)

for i in range(1, 51):
    driver.get("https://www.thetrumpet.com/key_of_david/program_archive?page=%d" %i)
    print("Searching https://www.thetrumpet.com/key_of_david/program_archive?page=%d" %i)
    links = get_links(driver)
    for link in links:
#        print(link)
        kod = get_info(link, links[link], lit_not_spanish, driver)
        if kod == 0 or kod == 1:
            continue
        else:
            write_lit(kod)

driver.quit()
