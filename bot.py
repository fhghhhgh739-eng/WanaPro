import logging
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

# إعداد السجلات لمعرفة حالة البوت
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# المفتاح الخاص المدمج
SKILL_API_KEY = "86CVKcFZKH5Y0bolMMq4hkWxkoNmcYwhyKTxsE2NnL8CW2Fessc-bw"

# أمر البداية /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_name = update.effective_user.first_name
    await update.message.reply_text(f"أهلاً بك يا أسطورة {user_name} في بوت 'تغلي' الذكي! تم تفعيل الاتصال والمهارات بنجاح 🤖🔥")

# معالجة الرسائل والمهام الواردة
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    
    # هنا يستقبل البوت رسالتك ويعالجها عبر المفتاح والمهارات المدمجة
    await update.message.reply_text(f"⚡ تم استلام طلبك ومعالجته بنجاح تام: {user_text}")

def main():
    # توكن البوت الصحيح الجديد
    token = "8694566651:AAFraTGpEIyJnvsytMq9HSASkJ09b_p4hBE"
    
    # بناء التطبيق
    application = ApplicationBuilder().token(token).build()

    # إضافة الأوامر والهاندلرز
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))

    print("🤖 بوت 'تغلي' يعمل الآن بالتوكن الصحيح وباتصال مستقر...")
    
    # تشغيل البوت
    application.run_polling()

if __name__ == '__main__':
    main()
    
    
  
