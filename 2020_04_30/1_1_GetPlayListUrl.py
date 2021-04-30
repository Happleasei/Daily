from selenium import webdriver
import time
import sys
allUniv = []

class Song_List():
    def __init__(self):
        self.url = 'https://music.163.com/#/search/m/?s=%E6%8A%91%E9%83%81&type=1000'
        self.driver = webdriver.Chrome()

    def paser(self):
        self.driver.get(self.url)
        # 切换到iframe框架

        frame = self.driver.find_element_by_xpath('//*[@id="g_iframe"]')
        self.driver.switch_to.frame(frame)
        time.sleep(2)
        i = 0
        item = []
        while True:
            info_list = self.driver.find_elements_by_css_selector("[class='f-cb']")
            for each in info_list:
                s_url = each.find_element_by_xpath("div[2]/div/span/a").get_attribute("href")
                item = {s_url}
                print(item)
                time.sleep(0.5)
            js = "var q=document.documentElement.scrollTop=100000"
            self.driver.execute_script(js)
            # 点击下一页
            next_page = self.driver.find_element_by_link_text('下一页')
            next_page.click()
            i += 1
            time.sleep(2)
            if(i==17):break


if __name__ == '__main__':


    output = sys.stdout
    outputfile = open("g:\python\s_url.csv", 'w', 25000, encoding='utf-8')
    sys.stdout = outputfile
    song_list = Song_List()
    song_list.paser()
    outputfile.close()
    sys.stdout = output

