import asyncio
import os
import glob
from src.scraper import get_latest_post
from src.tts_engine import generate_audio
from src.rss_generator import update_rss_file

def cleanup_old_episodes(audio_dir, max_files=20):
    """حذف ملفات الصوت القديمة للإبقاء على مساحة المستودع نظيفة"""
    # جلب قائمة بجميع ملفات mp3 في المجلد
    files = glob.glob(os.path.join(audio_dir, "*.mp3"))
    
    # ترتيب الملفات حسب وقت التعديل (الأقدم أولاً)
    files.sort(key=os.path.getmtime)
    
    # إذا زاد العدد عن الحد المسموح، ابدأ الحذف
    if len(files) > max_files:
        files_to_delete = files[:-max_files] # استثناء آخر 20 ملف
        for file_path in files_to_delete:
            try:
                os.remove(file_path)
                print(f"🗑️ تم حذف ملف قديم للمحافظة على المساحة: {file_path}")
            except Exception as e:
                print(f"⚠️ فشل حذف الملف {file_path}: {e}")

async def main():
    # الإعدادات الأساسية
    BLOG_RSS = "https://familytvr.blogspot.com/feeds/posts/default?alt=rss"
    AUDIO_DIR = "audio"
    USERNAME = "eslamtechautomation-ctrl"
    REPO = "Podcast-Automation-System"
    
    if not os.path.exists(AUDIO_DIR):
        os.makedirs(AUDIO_DIR)

    print("🚀 بدء عملية الأتمتة...")
    
    # 1. تنظيف الملفات القديمة (الحد الأقصى 20 ملف)
    cleanup_old_episodes(AUDIO_DIR, max_files=20)

    # 2. جلب أحدث مقال من بلوجر
    post = get_latest_post(BLOG_RSS)
    
    if post:
        file_name = f"episode_{post['id']}.mp3"
        audio_path = os.path.join(AUDIO_DIR, file_name)
        
        # 3. التحقق إذا كان المقال جديداً (غير موجود في المجلد)
        if not os.path.exists(audio_path):
            print(f"🎙️ جاري توليد صوت للحلقة الجديدة: {post['title']}")
            await generate_audio(post['clean_text'], audio_path)
            
            # رابط الملف المباشر على GitHub Pages
            audio_url = f"https://{USERNAME}.github.io/{REPO}/audio/{file_name}"
            
            # 4. تحديث ملف الـ RSS ليقرأه يوتيوب
            print("📝 تحديث ملف podcast.xml...")
            update_rss_file(post, audio_url)
            print("✅ انتهت العملية بنجاح.")
        else:
            print("⏭️ لا توجد مقالات جديدة، آخر مقال تمت معالجته بالفعل.")
    else:
        print("❌ فشل في الوصول لمقالات المدونة.")

if __name__ == "__main__":
    asyncio.run(main())
