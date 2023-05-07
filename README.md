# paper_summary

## 論文翻訳・要約ツールです。

## 実行方法：
【通常】

python main.py

【Docker】

docker build -t paper_summary .

【Linux, Mac】
docker run --rm -v $(pwd):/app -it paper_summary

【Windows】
docker run --rm -v "%cd%":/app -it paper_summary

## config.iniについて

imgフォルダ内のconfig.pngを参照ください。

翻訳、要約の出力結果の調整ができます。

## DeepLについて

翻訳でDeepLのAPIを使用することができます。

使用するためにはDeepLのAPIキーが必要となりますので、ご自身で取得の上、設定ください。

main.pyの「your API key」の部分を変更すれば使用できます。

## OpenAIによる要約について

OpenAIによる要約を実行することができます。

使用するためにはOpenAIのAPIキーが必要となりますので、ご自身で取得の上、設定ください。

gpt3_summary.pyの「your API key」の部分を変更すれば使用できます。

## 元記事
https://yonesuke0716.hatenablog.com/entry/2023/05/07/212750