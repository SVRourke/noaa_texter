from requests import get
from lxml import etree
from bs4 import BeautifulSoup as bs

def get_noaa_image_url(page_url):
    
    page = get(page_url)
    soup = bs(page.content, "html.parser")
    dom = etree.HTML(str(soup))
    img_src = dom.xpath("/html/body/div[5]/div/center/img")[0].get('src')

    return "https://www.nhc.noaa.gov" + img_src
