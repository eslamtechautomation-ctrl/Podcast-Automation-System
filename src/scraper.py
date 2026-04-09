import feedparser
from bs4 import BeautifulSoup

def get_latest_post(rss_url):
    feed = feedparser.parse(rss_url)
    if not feed.entries:
        return None
    
    entry = feed.entries[0]
    title = entry.title
    link = entry.link
    pub_date = entry.published
    
    # معالجة المحتوى لاستخراج روابط التحميل
    content_html = entry.summary if 'summary' in entry else entry.description
    soup = BeautifulSoup(content_html, 'lxml')
    
    # تجميع الروابط الهامة (مثل رابط تحميل التطبيق)
    links_list = []
    for a in soup.find_all('a', href=True):
        if a.text.strip():
            links_list.append(f"{a.text.strip()}: {a['href']}")
    
    links_text = "\n\n🔗 روابط التحميل والمصادر:\n" + "\n".join(links_list) if links_list else ""
    
    # تنظيف النص من الـ HTML لعمل ملف الصوت
    clean_text = soup.get_text(separator=' ').strip()
    
    return {
        "title": title,
        "clean_text": clean_text,
        "full_description": clean_text + links_text, # هذا سيظهر في وصف يوتيوب
        "link": link,
        "pub_date": pub_date,
        "id": entry.id.split('-')[-1] # معرف فريد للمقال
    }
