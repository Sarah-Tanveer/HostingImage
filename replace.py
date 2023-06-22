import re
import os

folders = []
path_ = os.getcwd()
dir_list = os.listdir(path_)
for i in dir_list:
    path = f"{path_}/{i}"
    if not os.path.isfile(path) and "reduced.html" in os.listdir(f"{path}/info"):
      folders.append(i)

for folder in folders:
  with open(f"{folder}/info/reduced.html", "r") as f:
    html_content = f.read()

  img_src_regex = r"<img(.*?)src=\"(.*?)\""
  img_srcs = re.findall(img_src_regex, html_content)
  for img_src in img_srcs:
    img_src = img_src[-1]
    if "localhost" in img_src:
        name = img_src.split("/")[-1]
        url = f"http://github.com/Sarah-Tanveer/HostingImage/raw/main/{folder}/{name}"
        html_content = html_content.replace(img_src, url)
  with open(f"{folder}/info/reduced_new.html", "w+") as f:
    f.write(html_content)
