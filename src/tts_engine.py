import edge_tts
import asyncio

async def generate_audio(text, output_path):
    # استخدام صوت "shakir" للأداء الرجالي أو "zariyah" للأداء النسائي
    voice = "ar-SA-ShakirNeural" 
    
    # نقوم بأخذ أول 3500 حرف لضمان استقرار التحويل
    text_to_read = text[:3500]
    
    communicate = edge_tts.Communicate(text_to_read, voice)
    await communicate.save(output_path)
    return True
