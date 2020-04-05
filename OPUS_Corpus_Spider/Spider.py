from bs4 import BeautifulSoup
import requests
import argparse
import os
import subprocess


def get_page_source_code(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    return soup


def check_item(item, args):
    s = item.attrs.get("href", None)

    if s is None:
        return False

    return True if "download" in s and args.key_words in s and s.endswith(args.file_type) else False


def crawl():
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", required=True, help="需要爬取的网页的网址")
    parser.add_argument("--output_dir", default="data", help="语料库下载后的存储地址，绝对地址或相对地址均可，默认是./data")
    parser.add_argument("--key_words", default="", help="下载的语料名称中必须含有的关键字，例如en表示下载和英文相关的语料，默认全部下载")
    parser.add_argument("--download_url", default="download_url.txt", help="把所有的下载链接都写入参数--download_url指定的文件中，方便查看，绝对路径或相对路径均可，默认是./download_url.txt")
    parser.add_argument("--file_type", default="", help="需要下载的文件格式，默认全部都下载")

    args = parser.parse_args()

    print("正在获取{}的网页源码...".format(args.url))
    source_code = get_page_source_code(args.url)
    print("获取网页源码完成\n")

    download_url = [item.attrs["href"] for item in source_code.find_all(name="a") if check_item(item, args)]

    download_url = list(set(download_url))  # 去重

    print("把该页面所有语料库的下载链接写入文件{}...".format(args.download_url))
    current_path = os.getcwd()
    with open(os.path.join(current_path, args.download_url), "w", encoding="utf-8") as f:
        f.write("\n".join(download_url))
    print("写入完成\n")

    output_dir = os.path.join(os.getcwd(), args.output_dir)
    print("开始下载语料，下载的语料的存储路径为: {}".format(output_dir))

    if not os.path.isdir(output_dir):
        os.makedirs(output_dir)

    for item in download_url:
        idx = item.rfind("/") + 1
        file_name = item[idx:]
        s = "http://opus.nlpl.eu/" + item
        print("开始从{}下载{}...".format(s, file_name))
        file_zip = requests.get(s)
        with open(os.path.join(output_dir, file_name), "wb") as f:
            f.write(file_zip.content)
        print("下载完成!\n")

        print("开始解压文件{}...".format(file_name))
        if file_name.endswith(".zip"):
            unzip_command = "unzip -d " + os.path.join(output_dir, file_name[:-4]) + " " + os.path.join(output_dir, file_name)
        else:
            unzip_command = "gunzip " + os.path.join(output_dir, file_name)

        if subprocess.call(unzip_command, shell=True):
            print("解压失败!\n")
        else:
            # 解压成功后删除.zip压缩包，.gz压缩包解压后自己会删除
            if file_name.endswith(".zip"):
                del_command = "rm " + os.path.join(output_dir, file_name)
                subprocess.call(del_command, shell=True)
            print("解压完成!\n")


if __name__ == "__main__":
    crawl()