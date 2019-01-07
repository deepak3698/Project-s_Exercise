def readnews():
    from newsapi import NewsApiClient
    key=input("Write your api_key:")
    newsapi = NewsApiClient(api_key=key)
    top_headlines = newsapi.get_top_headlines(
                                          sources='google-news-in',
                                          language='en')
    article = top_headlines["articles"]
    list1 = []
    a=input("If you want to listen title of the news then write title\nFor description of the news write description \n")
    for i in article:
            list1.append(i[f"{a}"])
    result = f"next {a} is ".join(map(str, list1))
    return result

def speak(str):
    from win32com.client import Dispatch
    speak=Dispatch("SAPI.SpVoice")
    speak.Speak(str)

if __name__ == '__main__':
    print("!!!!!Today's top_headlines of the news!!!!!")
    try:
        news=readnews()
        speak(news)
    except:
        print("Something Went Wrong!!!")