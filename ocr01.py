#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ocr01.py
# 2021/11/27 Nakagomi
import pyocr
from PIL import Image
import pyocr.builders

#img : PIL image
def get_digit_ocr_info(img):
	result = None
	width, height=img.size
	tools = pyocr.get_available_tools()
	tool = tools[0]
	langs = tool.get_available_languages()
	lang = 'eng'	#言語設定で、英語を選択（日本語は'jpn'）

	digit_txt = tool.image_to_string(
		img,
		lang=lang,
		builder=pyocr.builders.DigitBuilder(tesseract_layout=6)
	)
	#print(digit_txt)
	return digit_txt

def main():
	img = Image.open('/home/pi/ocr/img001.jpg')	#読み込み画像の場所
	ret = get_digit_ocr_info(img)
	print(ret)					#OCR変換した結果を表示

if __name__ == '__main__':
	main()
