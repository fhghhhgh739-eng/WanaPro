import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

# إعداد السجلات لمعرفة حالة البوت
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# أمر البداية /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_name = update.effective_user.first_name
    await update.message.reply_text(f"أهلاً بك يا أسطورة {user_name} في بوت 'تغلي' الذكي! 🤖🔥")

# معالجة الرسائل النصية
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    await update.message.reply_text(f"تم استلام طلبك يا أسطورة: {user_text} ⚡")

def main():
    # توكن البوت الخاص بك
    token = "8694566651:AAHmdGByWfuG3a-hNiGgZuNUA0g6pEAHx40"
    
    # بناء التطبيق بالطريقة الحديثة الصحيحة
    application = ApplicationBuilder().token(token).build()

    # إضافة الهاندلرز
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))

    print("🤖 بوت 'تغلي' يعمل الآن بنجاح تامن...")
    
    # تشغيل البوت بدون مشاكل التحديثات القديمة
    application.run_polling()

if __name__ == '__main__':
    main()
  
