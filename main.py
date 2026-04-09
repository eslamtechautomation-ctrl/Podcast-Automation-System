import asyncio
import os
from src.scraper import get_latest_post
from src.tts_engine import generate_audio
from src.rss_generator import update_rss_file

async def main():
    # الإعدادات
    BLOG_RSS = "https://familytvr.blogspot.com/feeds/posts/default?alt=rss"
    AUDIO_DIR = "audio"
    USERNAME = "eslamtechautomation-ctrl"
    REPO = "Podcast-Automation-System"
    
    if not os.path.exists(AUDIO_DIR):
        os.makedirs(AUDIO_DIR)

    print("🚀 بدء عملية الأتمتة...")
    post = get_latest_post(BLOG_RSS)
    
    if post:
        # جعل اسم الملف فريد باستخدام الـ ID الخاص بالمقال
        file_name = f"episode_{post['id']}.mp3"
        audio_path = os.path.join(AUDIO_DIR, file_name)
        
        # إذا كان الملف موجود مسبقاً لا داعي لإعادة التوليد
        if not os.path.exists(audio_path):
            print(f"🎙️ جاري توليد الصوت: {post['title']}")
            await generate_audio(post['clean_text'], audio_path)
            
            # رابط الملف المباشر بعد الرفع على GitHub Pages
            audio_url = f"https://{USERNAME}.github.io/{REPO}/audio/{file_name}"
            
            print("📝 تحديث ملف الـ RSS...")
            update_rss_file(post, audio_url)
            print("✅ انتهت العملية بنجاح.")
        else:
            print("⏭️ المقال موجود مسبقاً في البودكاست.")
    else:
        print("❌ لم يتم العثور على مقالات.")

if __name__ == "__main__":
    asyncio.run(main())
