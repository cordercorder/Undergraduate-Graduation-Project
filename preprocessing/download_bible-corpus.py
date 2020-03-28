import requests

source = "/data/rrjin/Graduation/data/bible-corpus/all_languages.txt"
output = "/data/rrjin/Graduation/data/bible-corpus/parallel_text/"

with open(source) as f:

    s = f.read()
    all_languages = s.split()

    for languages in all_languages:

        if languages == "en":
            continue

        prefix_path = "http://opus.nlpl.eu/download.php?f=bible-uedin/v1/moses/"
        # suf_path = languages + "-en.txt.zip"

        suf_path = "en-" + languages + ".txt.zip"

        print("Start Downloading ", languages)
        parallel_text_zip = requests.get(prefix_path + suf_path)
        with open(output + suf_path, "wb") as tmp:
            tmp.write(parallel_text_zip.content)
        print("End")