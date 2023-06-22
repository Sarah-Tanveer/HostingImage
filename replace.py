import re

with open("opera_weebly.com/info/reduced.html", "r") as f:
  html_content = f.read()

img_src_regex = r"<img(.*?)src=\"(.*?)\""
img_srcs = re.findall(img_src_regex, html_content)
for img_src in img_srcs:
  img_src = img_src[-1]
  if "localhost" in img_src:
      name = img_src.split("/")[-1]
      url = f"http://github.com/Sarah-Tanveer/HostingImage/raw/main/opera_weebly.com/{name}"
      print(url)
      html_content = html_content.replace(img_src, url)
with open("reduced_new.html", "w+") as f:
  f.write(html_content)

  

