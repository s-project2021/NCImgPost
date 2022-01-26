# NCimgPost
ネットワークカメラから画像を取得し、bsae64にエンコードしたものをjson形式でサーバにPostします。


# Requirement
* Python 3.9.6
* HTTPで画像取得できるネットワークカメラ(検証:TS-WRLC)


# Installation
```sh
pip install opencv-python
pip install urllib3
pip install requests
```

# Run
```sh
python res.py
```

# Usage
* `toPath`に送信先サーバのアドレスを指定
* `fromPath`に取得元カメラのアドレスを指定
* 必要に応じて Digest認証のIDとPWを指定


# License　
- [GPL 3.0](https://www.gnu.org/licenses/gpl-3.0.txt)



