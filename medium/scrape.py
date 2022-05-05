import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import json
import time
from selenium.common.exceptions import NoSuchElementException


# fetch blogs based on tags
def get_blogs(tag,page):
    # path = "F:/Downloads/Compressed/chromedriver"
    path = "E:/GC1/chromedriver_win32/chromedriver"
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--window-size=1920,1080')
    driver = webdriver.Chrome(executable_path=path, options=options)
    
    link = "https://medium.com/tag/" + tag
    driver.get(link)
    time.sleep(5)

    if driver.title=="Could not find tag on Medium":
        return None
    
    # Collecting all related tags
    related_tags = driver.find_element_by_class_name("jd")
    related_tags_list = related_tags.find_elements_by_tag_name("a")

    # print("RELATED TAGS --> ", type(related_tags_list),"\n\n")

    tags = []
    for tag in related_tags_list:
        data = {
            'tag': tag.text,
            'tag_link': tag.get_attribute('href')
        }
        #print("URLS --> ", data,"\n\n")
        tags.append(data)
    
    
    # to scroll the page upto bottom of the page
    while(page > 0):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(8)
        page = page - 1
    
    # Collecting list of all blogs
    blogs_ = driver.find_element_by_class_name("ev")
    blogs_list = blogs_.find_elements_by_tag_name("article")
    

    # print("Blog list --> ", blogs_list, "\n", type(blogs_list),"\n\n")

    blogs = []

    # Fetching blog details
    for blog in blogs_list:
        temp = blog.find_elements_by_tag_name("a")

        # will currently deal only in writer and date
        title = blog.find_element_by_tag_name('h2')
        blogs.append({
            'writer': temp[0].text,
            'date': temp[-1].text,
            'link': temp[-1].get_attribute('href'),
            'title': title.text,
        })
        # print("Blogs --> ", blogs,"\n\n")

    driver.close()
    return {'tags' : tags, 'blogs': blogs}


def get_details(link):
    # Collect details of a blog
    # Start to show the crawiling time
    start = time.time()

    path = "E:/GC1/chromedriver_win32/chromedriver"
    

    options = Options()
    options.add_argument('--headless')
    options.add_argument('--window-size=1920,1080')
    driver = webdriver.Chrome(executable_path=path, options=options)
    driver.get(link)
    time.sleep(5)

    time_ = ""
    date_=""

    article_title = driver.find_elements_by_tag_name("article")[0]

    # fetching author
    all_headers = article_title.find_elements_by_tag_name("header")
    authors = article_title.find_element_by_class_name("pw-author")
    author = authors.text
    # print("...................." , author)

    # fetching reading time
    while True:
        try:
            all_headers = article_title.find_elements_by_tag_name("header")
            all_headers = article_title.find_elements_by_class_name("pw-reading-time")
            for dt in all_headers: 
                if "read" in dt.text:
                    time_ += dt.text  
                    # print('>>> Time fetched ')
                    break
            break
        except:
            time.sleep(5)
    # print(time_)

     # fetching published date
    while True:
        try:
            all_headers = article_title.find_elements_by_tag_name("header")
            all_headers = article_title.find_elements_by_class_name("pw-published-date")
            for dt in all_headers: 
                if "Jan" in dt.text or "Feb" in dt.text or "Mar" in dt.text or "Apr" in dt.text or "May" in dt.text or "Jun" in dt.text or "Jul" in dt.text or "Aug" in dt.text or "Sep" in dt.text or "Oct" in dt.text or "Nov" in dt.text or  "Dec" in dt.text :
                    date_ += dt.text 
                    # print('>>> Date fetched ')
                    break
            break
        except:
            time.sleep(5)
    # print(date_)

    #fetching all related tags inside blog
    related_tags_list = []
    all_links = driver.find_elements_by_tag_name("a")

    for link in all_links:
        url = link.get_attribute('href')
        flag = url.find("/tag/")
        # print(flag)
        if flag != -1:
            related_tags_list.append(link.text)
        flag = url.find("/tagged/")
        if flag != -1:
            related_tags_list.append(link.text)
    # print(related_tags_list)

    if len(related_tags_list)==0:
        related_tags_list.append("No Related Tag Found !")
    
    # fetching responses count
    resp = article_title.find_elements_by_class_name("pw-multi-vote-count")
    
    # print("\n\n BUTTONS ><><><><>" , resp)
    # for b in resp:
    #     print("\n Text:  ------ ", b.text )

    resp_cnt = "Not found" 
    # print("\n\n><><><><>" , resp_cnt)


    #fetching claps and response

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)

    num_claps = "NA"
    num_responses = "NA"
    response_button = None
    
    
    driver.close()
    return {
        'time' : time_,
        'date': date_,
        'author': author,
        'num_claps': num_claps,
        'num_responses': resp_cnt,
        'related_tags': related_tags_list,
        'burst_time': int(time.time()-start),
    }


# data = get_details("https://towardsdatascience.com/is-python-really-a-bottleneck-786d063e2921")





