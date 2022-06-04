import os


class Config:
    API_ID = int(os.environ.get("API_ID"))
    API_HASH = os.environ.get("API_HASH")
    Token = os.environ.get("BOT_TOKEN")
    Session = os.environ.get("Session_String")
    if Session is None or Session == "":
        Session = ":memory:"
    App_Name = os.environ.get("APP_NAME")
    Port = int(os.environ.get("PORT"))
    Archive_Channel_ID = int(os.environ.get("ARCHIVE_CHANNEL_ID"))
    Start_Message = os.environ.get("Start_Message")
    Bot_Channel = os.environ.get("Bot_Channel_UserName")
    if Bot_Channel and Bot_Channel.startswith("@"):
        Bot_Channel = Bot_Channel[1:]
    elif Bot_Channel == "":
        Bot_Channel = None

    Link_Root = f"https://{App_Name}.herokuapp.com/"
    Download_Folder = "Files"
    Dev_Channel = "ApplicationsANTER"
    Bot_UserName = None  # The bot will set it after starting
    Part_size = 10 * 1024 * 1024  # (10MB) For Pyrogram
    Buffer_Size = 512 * 1024  # For Quart
    Pre_Dl = 3  # How many parts to download from telegram before client request them
    Separate_Time = 4  # (seconds)  wait time between messages if user send more than one
    Sleep_Threshold = 60  # (Seconds) sleep threshold for flood wait exceptions
    Max_Fast_Processes = 1  # How many links user can update them to fast links at the same time


class Strings:
    start = Config.Start_Message
    dl_link = "🔗 تحميل الرابط"
    st_link = "🎞 عرض الرابط"
    generating_link = "**⏳ أنتظر قليلٱ جار إنشاء الرابط...**"
    bot_channel = "📢 قناة البوت"
    dev_channel = "🤖 المطور"
    fast = "⚡️**تم تحديث الارتباط إلى ارتباط سريع**"
    update_link = "⚡ التحديث للأرتباط السريع"
    update_limited = ("⛔ لا يمكنك فقط تحديث رابط {Config.Max_Fast_Processes} في وقت واحد, "
                      "يرجى الانتظار حتى اكتمال التحديث السابق")
    re_update_link = "🔄 إعادة تحديث الارتباط"
    already_updated = "تم تحديث الارتباط بالفعل"
    wait_update = "⏳ تحديث الأرتباط ..."
    wait = "⏳ أرجو الإنتظار..."
    progress = "⏳ تقدم"
    file_not_found = "⚠️لم يتم العثور على الملف ، يرجى إعادة إرساله مرة أخرى"
    delete_manually_button = "⚠️يمكنك حذفه"
    delete_forbidden = "لا يستطيع الروبوت حذف الرسائل التي مضى عليها أكثر من 48 ساعة ، يمكنك حذف هذه الرسالة يدويًا"
    force_join = "⚠ انضم إلى قناة Bot لاستخدام هذا البوت"
