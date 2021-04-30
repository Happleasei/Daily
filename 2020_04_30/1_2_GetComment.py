from selenium import webdriver
import time
import sys
import csv

class Song_List():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def paser(self):
        with open("g:\python\s_url.csv", "r") as f:
            test_csv = f.read().splitlines()
        for url in test_csv:
            self.url = str(url)
            self.driver.get(self.url)
             # 切换到iframe框架
            frame = self.driver.find_element_by_xpath('//*[@id="g_iframe"]')
            self.driver.switch_to.frame(frame)
            time.sleep(2)
            i = 0
            data = []


            while True:
                info_list = self.driver.find_elements_by_xpath('//div[@class="itm"]')
                for each in info_list:
                    id = each.find_element_by_class_name('s-fc7').text
                    content = each.find_element_by_xpath('div[2]/div/div').text
                    # 存储为字典
                    item = {
                           'id':id,'content':content
                        }
                    # data.append(item)
                    #writer.writerow({'用户名':id, '评论':content})
                    print(item)
                    time.sleep(0.3)
                    # 点击下一页
                    # 将滚动条移动到页面的底部
                js = "var q=document.documentElement.scrollTop=100000"
                self.driver.execute_script(js)
                #h获取页
                try:
                    links = self.driver.find_element_by_xpath('//*[@class="m-cmmt"]/div[3]/div').find_elements_by_tag_name("a")
                    for link in links:
                        if link.get_attribute("text") != "":
                            data.append(link.get_attribute("text"))
                    page_number = int(data[-2])
                    next_page = self.driver.find_element_by_link_text('下一页')
                    next_page.click()
                    i += 1
                    if (i == page_number): break
                except: break
                time.sleep(2)

if __name__ == '__main__':

    output = sys.stdout
    outputfile = open("g:\python\comment_1.csv", 'w', 25000, encoding='utf-8')
    sys.stdout = outputfile
    song_list = Song_List()
    song_list.paser()
    outputfile.close()
    sys.stdout = output

