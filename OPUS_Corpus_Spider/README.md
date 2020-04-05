# 从OPUS自动下载语料库

### 运行环境
首先需要安装`beautifulsoup4`, `requests`, `lxml`模块

因为代码调用了`Linux`命令，所有代码只能在`Linux`环境下运行（类`Linux`例如`Mac`应该也行，但没试过）

## 参数简介

```
--url 需要爬取的网页的网址
--output_dir 语料库下载后的存储地址，绝对地址或相对地址均可，默认是./data
--key_words 下载的语料名称中必须含有的关键字，例如en表示下载和英文相关的语料，默认全部下载
--download_url 把所有的下载链接都写入参数--download_url指定的文件中，绝对路径或相对路径均可，默认是./download_url.txt
--file_type 需要下载的文件格式，默认全部都下载。在OPUS上的文件格式应该只有2中，.gz格式的文件和.zip格式的文件
```

## 用法

在`run_Spider.sh`中写入相应的参数后运行如下命令即可：
```
sh run_Spider.sh
```

例如`run_Spider.sh`中的内容可以为
```
python -u Spider.py \
    --url http://opus.nlpl.eu/CAPES.php \
    --output_dir /data/opus_corpus/
    --key_words en
    --download_url /data/download_url.txt
    --file_type .txt.zip
```