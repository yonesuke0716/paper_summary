from langchain.chat_models import ChatOpenAI
from langchain.text_splitter import CharacterTextSplitter
from langchain.docstore.document import Document
from langchain.chains.summarize import load_summarize_chain


def summary_output(translator, load_txt_file, is_deepl=False):
    print(f"GPT-3要約中・・・{load_txt_file}")
    with open(f"summary/{load_txt_file}") as f:
        long_text = f.read()
    llm = ChatOpenAI(model_name="gpt-3.5-turbo", openai_api_key="your API Key")
    text_splitter = CharacterTextSplitter()
    texts = text_splitter.split_text(long_text)

    docs = [Document(page_content=t) for t in texts[:3]]

    chain = load_summarize_chain(llm, chain_type="stuff")
    with open(f"summary/{load_txt_file}", mode="w", encoding="utf-8") as f:
        result = chain.run(docs)
        print(result, file=f)
        if translator is not None:
            if is_deepl:
                translated = translator.translate_text(result, source_lang="EN", target_lang="JA")
                print(translated, file=f)
            else:
                translated = translator.translate(result, dest="ja")
                print(translated.text, file=f)
