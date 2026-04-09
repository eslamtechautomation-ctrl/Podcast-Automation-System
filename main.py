import asyncio
import os
from src.scraper import get_latest_post
from src.tts_engine import generate_audio
from src.rss_generator import update_rss_file

async def main():
    BLOG_RSS = "https://familytvr.blogspot.com/feeds/posts/default?alt=rss"
    AUDIO_DIR = "audio"
    
    if not os.path.exists(AUDIO_DIR):
        os.makedirs(AUDIO_DIR)

    # 1. سحب المقال
    print("🔍 جاري فحص المقالات...")
    post = get_latest_post(BLOG_RSS)
    
    if post:
        file_name = f"episode.mp3"
        audio_path = os.path.join(AUDIO_DIR, file_name)
        
        # 2. توليد الصوت
        print(f"🎙️ جاري تحويل المقال إلى صوت: {post['title']}")
        await generate_audio(post['clean_text'], audio_path)
        
        # 3. تحديث الـ RSS
        # ملاحظة: استبدل الروابط برابط GitHub Pages الخاص بك لاحقاً
        audio_url = f"https://YOUR_USERNAME.github.io/YOUR_REPO/audio/{file_name}"
        update_rss_file(post, audio_url)

if __name__ == "__main__":
    asyncio.run(main())
