import edge_tts
import asyncio
import os

async def generate_audio(text, output_path):
    # اختيار صوت "شاكر" السعودي لأنه من أفضل الأصوات العربية الطبيعية
    voice = "ar-SA-ShakirNeural" 
    
    # تقليل طول النص إذا كان ضخماً جداً (اختياري)
    short_text = text[:3000] 
    
    communicate = edge_tts.Communicate(short_text, voice)
    await communicate.save(output_path)
    
    if os.path.exists(output_path):
        print(f"✅ تم إنشاء ملف الصوت بنجاح: {output_path}")
        return True
    return False
