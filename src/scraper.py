import feedparser
from bs4 import BeautifulSoup

def get_latest_post(rss_url):
    # جلب البيانات من رابط RSS المدونة
    feed = feedparser.parse(rss_url)
    
    if not feed.entries:
        return None
    
    # سحب آخر مقال (أحدث واحد)
    entry = feed.entries[0]
    title = entry.title
    link = entry.link
    pub_date = entry.published
    
    # معالجة محتوى المقال (الوصف)
    content_html = entry.summary if 'summary' in entry else entry.description
    soup = BeautifulSoup(content_html, 'lxml')
    
    # استخراج الروابط (عشان روابط تحميل التطبيقات تظهر في الوصف)
    links_text = "\n\nروابط هامة من المقال:\n"
    for a in soup.find_all('a', href=True):
        links_text += f"- {a.text}: {a['href']}\n"
    
    # تحويل الـ HTML لنص نظيف للبودكاست
    clean_text = soup.get_text(separator=' ')
    
    return {
        "title": title,
        "clean_text": clean_text,
        "full_description": clean_text + links_text, # الوصف الذي سيظهر في يوتيوب
        "link": link,
        "pub_date": pub_date
    }
