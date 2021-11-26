# ocr
IoT専門家人材育成講座 OCR Pythonプログラム

■OCR機能の実装：
参考サイト：https://motojapan.hateblo.jp/entry/2018/03/12/094636

１．ラズパイのLxTerminalを起動します。

２．OSアップデート（今回は実行しないでください。）
$ sudo apt-get update
$ sudo apt-get upgrade


３．Tesseract OCRのインストール
$ sudo apt-get install tesseract-ocr tesseract-ocr-jpn


４．インストールできたか確認
$ tesseract -v
　※「tesseract 4.0.0」←このような表示が出ればOK


５．tesseract-ocrをpythonから操作する為のWrapperであるpyocrのインストール
$ sudo pip3 install pyocr


６．pythonプログラムの導入
$ git clone https://github.com/nakagomi51/ocr01.git
