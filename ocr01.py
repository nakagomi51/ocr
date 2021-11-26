#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# test06.py
# 2021/11/27 Nakagomi
#
#オプション指定
#DigitBuilder:
# TextBuilder		= 文字列を認識	
# WordBoxBuilder	= 単語単位で文字認識 + BoundingBox	
# LineBoxBuilder	= 行単位で文字認識 + BoundingBox	
# DigitBuilder		= 数字 / 記号を認識		←今回はこれを使用
# DigitLineBoxBuilder	= 数字 / 記号を認識 + BoundingBox
#
#tesseract_layout:
# 0 = Orientation and script detection (OSD) only.
# 1 = Automatic page segmentation with OSD.
# 2 = Automatic page segmentation, but no OSD, or OCR
# 3 = Fully automatic page segmentation, but no OSD. (Default)
# 4 = Assume a single column of text of variable sizes.
# 5 = Assume a single uniform block of vertically aligned text.
# 6 = Assume a single uniform block of text.		←今回は単一ブロックとして認識
# 7 = Treat the image as a single text line.
# 8 = Treat the image as a single word.
# 9 = Treat the image as a single word in a circle.
# 10 = Treat the image as a single character.

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
	lang = 'eng'	#言語設定で、「英語」を選択

	digit_txt = tool.image_to_string(
		img,
		lang=lang,
		builder=pyocr.builders.DigitBuilder(tesseract_layout=6)
	)
	print(digit_txt)
	return digit_txt

def main():
	im = Image.open('/home/pi/img007.jpg')	#読み込み画像の場所
	get_digit_ocr_info(im)

if __name__ == '__main__':
	main()
