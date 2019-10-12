from flask import render_template

from app import app


@app.route('/')
def index():
    sources = [
        {
            "id": "abc-news",
            "name": "ABC News",
            "description": "Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at ABCNews.com.",
            "url": "https://abcnews.go.com",
            "category": "general",
            "language": "en",
            "country": "us"
        },
        {
            "id": "abc-news-au",
            "name": "ABC News (AU)",
            "description": "Australia's most trusted source of local, national and world news. Comprehensive, independent, in-depth analysis, the latest business, sport, weather and more.",
            "url": "http://www.abc.net.au/news",
            "category": "general",
            "language": "en",
            "country": "au"
        },
        {
            "id": "aftenposten",
            "name": "Aftenposten",
            "description": "Norges ledende nettavis med alltid oppdaterte nyheter innenfor innenriks, utenriks, sport og kultur.",
            "url": "https://www.aftenposten.no",
            "category": "general",
            "language": "no",
            "country": "no"
        },
        {
            "id": "al-jazeera-english",
            "name": "Al Jazeera English",
            "description": "News, analysis from the Middle East and worldwide, multimedia and interactives, opinions, documentaries, podcasts, long reads and broadcast schedule.",
            "url": "http://www.aljazeera.com",
            "category": "general",
            "language": "en",
            "country": "us"
        },
        {
            "id": "ansa",
            "name": "ANSA.it",
            "description": "Agenzia ANSA: ultime notizie, foto, video e approfondimenti su: cronaca, politica, economia, regioni, mondo, sport, calcio, cultura e tecnologia.",
            "url": "http://www.ansa.it",
            "category": "general",
            "language": "it",
            "country": "it"
        },
        {
            "id": "argaam",
            "name": "Argaam",
            "description": "ارقام موقع متخصص في متابعة سوق الأسهم السعودي تداول - تاسي - مع تغطيه معمقة لشركات واسعار ومنتجات البتروكيماويات , تقارير مالية الاكتتابات الجديده ",
            "url": "http://www.argaam.com",
            "category": "business",
            "language": "ar",
            "country": "sa"
        },
        {
            "id": "ars-technica",
            "name": "Ars Technica",
            "description": "The PC enthusiast's resource. Power users and the tools they love, without computing religion.",
            "url": "http://arstechnica.com",
            "category": "technology",
            "language": "en",
            "country": "us"
        },
        {
            "id": "ary-news",
            "name": "Ary News",
            "description": "ARY News is a Pakistani news channel committed to bring you up-to-the minute Pakistan news and featured stories from around Pakistan and all over the world.",
            "url": "https://arynews.tv/ud/",
            "category": "general",
            "language": "ud",
            "country": "pk"
        },
        {
            "id": "associated-press",
            "name": "Associated Press",
            "description": "The AP delivers in-depth coverage on the international, politics, lifestyle, business, and entertainment news.",
            "url": "https://apnews.com/",
            "category": "general",
            "language": "en",
            "country": "us"
        },
    ]
    return render_template("index.html", sources=sources)


@app.route('/about')
def about():
    return render_template("about.html")
