import os
from datetime import datetime

def update_rss_file(post_data, audio_url, output_file="podcast.xml"):
    email = "eslammosde@gmail.com"
    cover_image = "https://raw.githubusercontent.com/YOUR_USERNAME/YOUR_REPO/main/assets/cover.jpg" # ستحتاج لتغيير المسار لاحقاً
    
    rss_template = f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" 
    xmlns:itunes="http://www.itunes.com/dtds/podcast-1.0.dtd" 
    xmlns:content="http://purl.org/rss/1.0/modules/content/">
  <channel>
    <title>Family TVR Podcast</title>
    <link>https://familytvr.blogspot.com/</link>
    <language>ar</language>
    <itunes:author>Family TVR</itunes:author>
    <itunes:owner>
        <itunes:name>Family TVR</itunes:name>
        <itunes:email>{email}</itunes:email>
    </itunes:owner>
    <itunes:image href="{cover_image}" />
    <description>بودكاست تقني آلي لمدونة Family TVR</description>
    
    <item>
      <title>{post_data['title']}</title>
      <description>{post_data['full_description']}</description>
      <pubDate>{post_data['pub_date']}</pubDate>
      <enclosure url="{audio_url}" type="audio/mpeg" length="1024" />
      <guid isPermaLink="false">{post_data['link']}</guid>
      <itunes:duration>00:10:00</itunes:duration>
    </item>
  </channel>
</rss>"""

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(rss_template)
    print("✅ تم تحديث ملف podcast.xml")
