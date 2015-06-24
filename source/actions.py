def get_links(driver):
        # find the class elements
    class_ = driver.find_elements_by_class_name("title")
    links = {}
    for link in class_:
        links[link.text] = link.find_element_by_css_selector("a").get_attribute("href")
    return links

import os.path

def write_lit(kod):
    
    filename = "../lit/kod_lit_spanish_trans.txt"

    if os.path.isfile(filename):
        f = open(filename, "a")
        f.write(kod['title'] + " " + str(kod['id']) + "\n" + kod['lits'])
        f.close() 
    else:
        f = open(filename, "w")
        f.write(kod['title'] + " " + str(kod['id']) + "\n" + kod['lits'])
        f.close()

import re

def get_info(title, link, lit_not_spanish, driver):

    lits = []
    
    driver.get(link)
    class_ = driver.find_elements_by_css_selector(".offer.available")
        
    for element in class_:
        lit = element.find_element_by_css_selector(".title").find_element_by_css_selector("a").text
        if "DVD" in lit:
            continue
        elif lit in lit_not_spanish:
            return 0
        else:
            lits.append(element.find_element_by_css_selector(".title").find_element_by_css_selector("a").text)
    id_ = int(''.join(x for x in link if x.isdigit()))

    return {'title': title, 'id': id_, 'url': link, 'lits': lits}
