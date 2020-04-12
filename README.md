# wear_downloader
[Wear](https://wear.jp/)から画像をダウンロードするスクリプトです。

# 必要なもの
- beautifulsoup4

- requests

- Pillow

# 動作環境
以下の環境で動作を確認してます。
- python3 == 3.8.2

- beautifulsoup4 == 4.9.0

- requests == 2.23.0

- Pillow == 7.1.1

# 使い方
```
python3 wear_downloader.py <url>
```

コーディネートページから一括してダウンロード

```
python3 wear_downloader.py <url> -c
```
画像はカレントディレクトリに保存されます。

# 今後追加するかもしれないこと

- 保存先フォルダの指定

- エラーハンドリング


# 更新履歴

4/11 コーディネートページから一括して画像をダウンロード
