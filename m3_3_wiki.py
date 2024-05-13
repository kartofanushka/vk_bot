import wikipedia
def get_article(article):
    wikipedia.set_lang("ru")
    try:
        page=wikipedia.page(article)
        return f'{page.url}\n{wikipedia.summary(article)[:900]}'
    except wikipedia.WikipediaException:
        return('cannot find any')
# get_article("10")