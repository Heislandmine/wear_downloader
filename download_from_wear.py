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


# コーディネートページからページのurlを抽出
def get_page_urls(base_url: str, target_url: str) -> list:
    page_urls = []
    page_urls.append(target_url)
    response = requests.get(target_url).content
    html = bs4.BeautifulSoup(response, "html.parser")
    elements = [x for x in html.find("div", id="pager").find_all("a")]
    for element in elements:
        page_urls.append(base_url + element.get("href"))

    return list(set(page_urls))  # 重複削除のために一度setに変換


if __name__ == "__main__":
    print(get_page_urls("https://wear.jp", "https://wear.jp/amnono/"))
