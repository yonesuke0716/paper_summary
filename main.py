import configparser
import os

import googletrans
import deepl

import txt_format
import translate
import read_pdf

import gpt3_summary
import shutil


config_ini = configparser.ConfigParser()
config_ini.read("config.ini", encoding="utf-8-sig")

file_path = config_ini["data"]["file_path"]

# global
str_thresh = int(config_ini["data"]["str_thresh"])
is_summary = bool(int(config_ini["mode"]["summary"]))
is_trans = bool(int(config_ini["mode"]["trans"]))
is_deepl = bool(int(config_ini["mode"]["deepl"]))

os.makedirs("output", exist_ok=True)
if os.path.exists("output"):
    shutil.rmtree("output")
    os.makedirs("output", exist_ok=True)

if is_summary:
    os.makedirs("summary", exist_ok=True)
    if os.path.exists("summary"):
        shutil.rmtree("summary")
        os.makedirs("summary", exist_ok=True)

if is_trans:
    if is_deepl:
        API_KEY = "your API key"
        translator = deepl.Translator(API_KEY)
    else:
        translator = googletrans.Translator()
else:
    translator = None


def main():
    # pdfファイル指定時
    if file_path.endswith("pdf"):
        out_txt = read_pdf.pdf_to_txt(file_path)

    # txtファイル指定時
    elif file_path.endswith("txt"):
        with open(file_path, encoding="utf-8") as f:
            l_strip = [s.strip() for s in f.readlines()]
        out_txt = " ".join(l_strip)

    # テキストファイルの整形
    text_file_list, format_list = txt_format.period_format(out_txt, str_thresh)

    # テキストファイルの出力
    translate.output_text(translator, text_file_list, format_list, is_deepl=is_deepl, is_summary=is_summary)


if __name__ == "__main__":
    # 文字列の整形、出力（翻訳）
    main()
    # GPT-3による要約
    if is_summary:
        file_names = os.listdir("summary")
        for file in file_names:
            gpt3_summary.summary_output(translator, file, is_deepl=is_deepl)
        # 要約結果の結合
        txt_format.concat_textfiles(file_names)
    print("出力が完了しました。")
