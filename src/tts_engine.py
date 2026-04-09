import edge_tts
import asyncio

async def generate_audio(text, output_path):
    # استخدام صوت إنجليزي (امريكي) احترافي يتناسب مع محتوى مقالاتك
    voice = "en-US-GuyNeural" 
    
    # تنظيف النص
    text = text.replace('\n', ' ').strip()
    
    try:
        # أخذ جزء كافٍ من النص للمقالة
        communicate = edge_tts.Communicate(text[:4000], voice)
        await communicate.save(output_path)
        print(f"✅ تم توليد الصوت بنجاح باستخدام الصوت الإنجليزي")
        return True
    except Exception as e:
        print(f"⚠️ خطأ في تحويل الصوت: {e}")
        return False
