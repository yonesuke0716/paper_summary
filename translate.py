from tqdm import tqdm


def output_text(translator, text_file_list, format_list, is_deepl=False, is_summary=False):
    f_num = 0
    # str_thresh文字以上超えた出力
    if len(text_file_list) > 0:
        for text_file in text_file_list:
            f_num += 1
            print(f"修正したテキストを生成中・・・output_{f_num}.txt")
            with open(f"output/output_{f_num}.txt", mode="w", encoding="utf-8") as f:
                for t_num in tqdm(range(len(text_file))):
                    # 整形したフォーマットの出力
                    print(text_file[t_num], file=f)
                    if translator is not None:
                        # 英語→日本語
                        if is_deepl:
                            translated = translator.translate_text(text_file[t_num], source_lang="EN", target_lang="JA")
                            print(translated, file=f)
                        else:
                            translated = translator.translate(text_file[t_num], dest="ja")
                            print(translated.text, file=f)
            if is_summary:
                with open(f"summary/result_{f_num}.txt", mode="w", encoding="utf-8") as f:
                    for t_num in range(len(text_file)):
                        # 整形したフォーマットの出力
                        print(text_file[t_num], file=f)
    # str_thresh文字以内の出力
    f_num += 1
    print(f"修正したテキストを生成中・・・output_{f_num}.txt")
    with open(f"output/output_{f_num}.txt", mode="w", encoding="utf-8") as f:
        for n_text in tqdm(range(len(format_list))):
            # 整形したフォーマットの出力
            print(format_list[n_text], file=f)
            if translator is not None:
                # 英語→日本語の出力
                if is_deepl:
                    translated = translator.translate_text(format_list[n_text], source_lang="EN", target_lang="JA")
                    print(translated, file=f)
                else:
                    translated = translator.translate(format_list[n_text], dest="ja")
                    print(translated.text, file=f)
    if is_summary:
        with open(f"summary/result_{f_num}.txt", mode="w", encoding="utf-8") as f:
            for n_text in range(len(format_list)):
                # 整形したフォーマットの出力
                print(format_list[n_text], file=f)
