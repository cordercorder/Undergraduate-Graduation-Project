from bs4 import BeautifulSoup
import requests
import os


def get_page_source_code(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    return soup


parent_url = "http://data.statmt.org/opus-100-corpus/v1.0"
output_dir = "/data/rrjin/Graduation/data/opus100"
res = ["supervised", "zero-shot"]

for d in res:
    link = os.path.join(parent_url, d)
    dir_name = os.path.join(output_dir, d)

    if not os.path.isdir(dir_name):
        os.makedirs(dir_name)

    source_code = get_page_source_code(link).find_all("a")
    a_token = source_code[5:]
    download_url = [os.path.join(link, item.attrs["href"]) for item in a_token]

    for item in a_token:
        sub_dir_name = os.path.join(dir_name, item.attrs["href"][:-1])

        if not os.path.isdir(sub_dir_name):
            os.makedirs(sub_dir_name)

        d_url = os.path.join(link, item.attrs["href"])
        file_url_list = get_page_source_code(d_url).find_all("a")[5:]

        for sub_url in file_url_list:
            file_url = os.path.join(d_url, sub_url.attrs["href"])
            # print(file_url)
            # print(sub_url.attrs["href"])
            print("正在下载{}...".format(file_url))
            file = requests.get(file_url)

            with open(os.path.join(sub_dir_name, sub_url.attrs["href"]), "wb") as f:
                f.write(file.content)

            print("下载完成!\n")