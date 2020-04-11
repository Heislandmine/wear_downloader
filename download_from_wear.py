import requests
import bs4
from PIL import Image
from io import BytesIO
import os.path


# urlのページから画像のurlを抽出
def get_image_url(url: str) -> str:
    response = requests.get(url).content
    html = bs4.BeautifulSoup(response, "html.parser")
    image_url = html.find("meta", property="og:image").get("content")
    return image_url


# 画像をダウンロードして保存
def save_image(url: str) -> None:
    file_name = os.path.basename(url)
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img.save(file_name)


# コーディネートページから個別ページのurlを取得
def get_url_from_coordinate(base_url: str, url: str) -> list:
    response = requests.get(url).content
    html = bs4.BeautifulSoup(response, "html.parser")
    div_image = html.find_all("div", class_="image")
    content_url = [
        element.find("a", class_="over").get("href")
        for element in div_image
        if element.find("a", class_="over") is not None
    ]
    content_url = [base_url + element for element in content_url]

    return content_url


if __name__ == "__main__":

    base_url = "https://wear.jp"
    ret = get_url_from_coordinate(base_url, "https://wear.jp/mmngo/")
    for url in ret:
        image_url = get_image_url(url)
        save_image(image_url)
