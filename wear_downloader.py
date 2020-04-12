import download_from_wear
import argparse

# 引数のパース設定
parser = argparse.ArgumentParser("download images from Wear")
parser.add_argument("target_url", help="target page url")
parser.add_argument(
    "-c", "--coordinate", action="store_true", help="download from coordinate page"
)
args = parser.parse_args()

target_url = args.target_url

if args.coordinate is not None:
    base_url = "https://wear.jp"
    page_urls = download_from_wear.get_page_urls(base_url, target_url)
    for page_url in page_urls:
        urls = download_from_wear.get_url_from_coordinate(base_url, page_url)
        for url in urls:
            image_url = download_from_wear.get_image_url(url)
            download_from_wear.save_image(image_url)
    else:
        image_url = download_from_wear.get_image_url(target_url)
        download_from_wear.save_image(image_url)
