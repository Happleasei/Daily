import requests, time
from selenium import webdriver
from lxml import etree
from requests.utils import unquote
from selenium.webdriver.common.keys import Keys


class WangyiMusic:
    def __init__(self):
        self.start_url = "https://music.163.com/discover/playlist/"
        self.url_temp = "https://music.163.com"
        self.headers = {
            "Referer": "https://music.163.com/",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3608.4 Safari/537.36"
        }
        self.session = requests.Session()
        self.driver = webdriver.Chrome()

    def parse_get_url(self):
        resp = self.session.get(self.start_url, headers=self.headers)
        return resp.content.decode()

    def get_category_list(self, html_str):
        el = etree.HTML(html_str)
        dl_list = el.xpath("//div[@class='bd']/dl")
        category_list = []
        for dl in dl_list:
            a_list = dl.xpath(".//a[@class='s-fc1 ']")
            for a in a_list:
                items = {}
                items["cate_name"] = a.xpath("./text()")[0]
                items["cate_url"] = self.url_temp + a.xpath("./@href")[0]
                print(items)
                category_list.append(items)

        cate_url_list = [category["cate_url"] for category in category_list]
        print(cate_url_list)
        return category_list, cate_url_list

    def save_category_list(self, category_list):
        pass

    def get_playlist_list(self):
        li_list = self.driver.find_elements_by_xpath("//ul[@id='m-pl-container']/li")
        playlist_list = []
        for li in li_list:
            items = {}
            items["playlist_name"] = li.find_element_by_xpath(".//a[@class='tit f-thide s-fc0']").text
          #  items["playlist_url"] = li.find_element_by_xpath(".//a[@class='tit f-thide s-fc0']").get_attribute("href")
          #  items["playlist_author"] = li.find_element_by_xpath(".//a[@class='nm nm-icn f-thide s-fc3']").text
          #  items["playlist_num"] = li.find_element_by_xpath(".//span[@class='nb']").text
            print(items)
            playlist_list.append(items)

        next_url = self.driver.find_elements_by_xpath(".//a[@class='zbtn znxt']")
        # next_url = self.driver.find_elements_by_link_text("?????????")
        next_url = next_url[0] if len(next_url) > 0 else None
        print(next_url)
        return playlist_list, next_url

    def save_playlist_list(self, playlist_list):
        for playlist in playlist_list:
            with open("G:\python\_02_all_list.txt", 'a', encoding="utf-8") as f:
                f.write(playlist["playlist_name"])
                f.write("\n\n")

    def run(self):
        # ????????????????????????????????? url
        # ????????????
        html_str = self.parse_get_url()
        # ?????????????????? url ??????
        category_list, cate_url_list = self.get_category_list(html_str)
        # ?????????????????? url ??????
        self.save_category_list(category_list)

        # ???????????????????????? url???????????????????????????????????? url
        for cate_url in cate_url_list:
            # ?????????????????? url
            self.driver.get(cate_url)
            # ????????? iframe ?????????
            self.driver.switch_to.frame(self.driver.find_elements_by_tag_name("iframe")[0])
            # ??????????????????
            time.sleep(5)
            # ????????????
            print("*" * 100)
            print(unquote(self.driver.current_url))  # ???????????? url

            playlist_list, next_url = self.get_playlist_list()  # ??????????????????????????????
            # ????????????
            self.save_playlist_list(playlist_list)
            # ???????????????
            while next_url is not None:
                next_url.send_keys(Keys.ENTER)  # ??????????????????????????????  ???Enter??????click
                time.sleep(5)
                # ????????????
                playlist_list, next_url = self.get_playlist_list()
                # ????????????
                self.save_playlist_list(playlist_list)

            print("*" * 100)

        self.driver.quit()


if __name__ == '__main__':
    wangyimusic = WangyiMusic()
    wangyimusic.run()
