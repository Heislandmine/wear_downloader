import requests
import bs4
from PIL import Image
from io import BytesIO
import os.path
import sys

url = sys.argv[1]


def get_image_url(url: str) -> str:
    response = requests.get(url).content
    html = bs4.BeautifulSoup(response, "html.parser")
    image_url = html.find("meta", property="og:image").get("content")
    return image_url


def save_image(url: str) -> None:
    file_name = os.path.basename(url)
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img.save(file_name)


if __name__ == "__main__":
    image_url = get_image_url(url)
    save_image(image_url)
