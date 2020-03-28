import xml.etree.ElementTree as ET
import os

source_path = "/data/rrjin/Graduation/data/bible-corpus/bibles/"

output_path = "/data/rrjin/Graduation/data/bible-corpus/bibles_txt/"

for files in os.listdir(source_path):

    if os.path.isfile(source_path + files) and files.endswith(".xml"):

        lang = files[:-4]

        print(lang)
        root = ET.fromstring(open(source_path + files, encoding="utf-8").read())

        # for item in root.iter("seg"):
        #     print(type(item), type(item.text), item.text)

        with open(output_path + lang + ".txt", "w", encoding="utf-8") as out:
            for item in root.iter("seg"):
                if item.text is not None:
                    out.write(item.text.strip() + "\n")