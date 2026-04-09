from src.utils import format_date_to_rfc822, clean_description_text

def update_rss_file(post_data, audio_url, output_file="podcast.xml"):
    email = "eslammosde@gmail.com"
    # هذا هو الرابط المباشر (Raw) للصورة التي أرسلتها
    cover_image = "https://raw.githubusercontent.com/eslamtechautomation-ctrl/Podcast-Automation-System/main/assets/cover.jpg"
    
    # تنظيف وتنسيق البيانات قبل وضعها في الـ RSS
    clean_desc = clean_description_text(post_data['full_description'])
    formatted_date = format_date_to_rfc822(post_data['pub_date'])

    rss_template = f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" 
    xmlns:itunes="http://www.itunes.com/dtds/podcast-1.0.dtd" 
    xmlns:content="http://purl.org/rss/1.0/modules/content/"
    xmlns:atom="http://www.w3.org/2005/Atom">
  <channel>
    <atom:link href="https://eslamtechautomation-ctrl.github.io/Podcast-Automation-System/podcast.xml" rel="self" type="application/rss+xml" />
    <title>Family TVR Podcast</title>
    <link>https://familytvr.blogspot.com/</link>
    <language>en-us</language>
    <itunes:author>Family TVR</itunes:author>
    <itunes:owner>
        <itunes:name>Eslam Tech</itunes:name>
        <itunes:email>{email}</itunes:email>
    </itunes:owner>
    <itunes:image href="{cover_image}" />
    <description>تحويل آلي لمقالات مدونة Family TVR إلى بودكاست صوتي</description>
    <itunes:category text="Technology" />
    
    <item>
      <title>{post_data['title']}</title>
      <itunes:title>{post_data['title']}</itunes:title>
      <description><![CDATA[{clean_desc}]]></description>
      <pubDate>{formatted_date}</pubDate>
      <enclosure url="{audio_url}" type="audio/mpeg" length="1024" />
      <guid isPermaLink="false">{post_data['id']}</guid>
      <itunes:author>Family TVR</itunes:author>
      <itunes:image href="{cover_image}" />
    </item>
  </channel>
</rss>"""

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(rss_template)
