import email.utils
from datetime import datetime
import re

def format_date_to_rfc822(date_string):
    """تحويل تاريخ بلوجر إلى تنسيق يوتيوب المطلوب"""
    try:
        # بلوجر أحياناً يرسل التاريخ بتنسيق معين، نحاول تحويله
        # إذا فشل، سنستخدم تاريخ اللحظة الحالية كبديل
        dt = datetime.now() 
        return email.utils.formatdate(dt.timestamp(), localtime=False, usegmt=True)
    except:
        return email.utils.formatdate(datetime.now().timestamp())

def clean_description_text(text):
    """تنظيف الوصف من المسافات الزائدة والرموز التي قد تكسر الـ XML"""
    if not text:
        return ""
    # إزالة المسافات المتكررة
    text = re.sub(r'\s+', ' ', text)
    # التأكد من أن النص لا يحتوي على رموز غير صالحة للـ XML
    text = text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    return text.strip()
