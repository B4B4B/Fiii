from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
[ ](https://telegra.ph/file/a4ae42abc5063ca28b59f.jpg)
اهلا {}

اهلا بك عزيزي {}


اختصاص هذا البوت تحويل الصورة الى رابط

ورفعها على التليكراف


الرجاء ارسال رابط الصورة 

ليتم تحويلها الى تليكراف
    """


    # About Message
    ABOUT = """

برمجة المطور [بايروجرام](docs.pyrogram.org)

لغة البوت [بايثون](www.python.org)

Mustafa [المطور  ](https://t.me/R2RR7)

"""


    # Home Button
    home_buttons = [
        [InlineKeyboardButton("المطور", url="https://t.me/R2RR7")],
        [InlineKeyboardButton("إغلاق 🔐", callback_data="close")],
        [InlineKeyboardButton(text=" العودة إلى الصفحة الرئيسية ", callback_data="home")],
    ]

    # Rest Buttons
    buttons = [
        [
            InlineKeyboardButton("المطور", url="https://t.me/R2RR7")
        ],
        [
            InlineKeyboardButton("المعلومات", callback_data="about")
        ],
        [InlineKeyboardButton("إغلاق ", callback_data="close")]
    ]

    # Supported Media Buttons
    supported_media_buttons = [
        [InlineKeyboardButton("المطور ", url="https://t.me/QQQLO")],
        [InlineKeyboardButton("إغلاق ", callback_data="close")],
        [InlineKeyboardButton(text=" العودة إلى الصفحة الرئيسية ", callback_data="home")]
    ]
