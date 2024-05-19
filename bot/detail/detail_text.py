from aiogram.utils.i18n import gettext as _
from aiogram.utils.text_decorations import markdown_decoration

def channel_detail(chat):
    text = markdown_decoration.bold(f'''
Chat
ID: {markdown_decoration.code(chat.id)}
Name: {chat.title}
Username: {chat.username}
Count users: {chat.get_member_count()}
    ''')
    return text

def start_text(msg):
    text = markdown_decoration.bold(msg.from_user.full_name + _('Assalom alaykum\n\n'
                                                                'UstozShogird kanalining rasmiy botiga xush kelibsiz!\n'
                                                                '/help ordam buyrugi orqali nimalarga qodir ekanligimni bilib oling!'))
    return text


def start_detail_keyboard(msg):
    text = markdown_decoration.bold(msg + _(' topish uchun ariza berish\n\n'
                                            'Hozir sizga birnecha savollar beriladi. \n'
                                            'Har biriga javob bering.\n'
                                            'Oxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va arizangiz Adminga yuboriladi.'''))
    return text


def appeal_detail():
    text = markdown_decoration.bold(_('🕰 Murojaat qilish vaqti: \n'
                                      'Qaysi vaqtda murojaat qilish mumkin?\n'
                                      'Masalan, 9:00 - 18:00'''))
    return text


def area_detail():
    text = markdown_decoration.bold(_('🌐 Hudud: \n\n'
                                      'Qaysi hududdansiz?\n'
                                      'Viloyat nomi, Toshkent shahar yoki Respublikani kiriting.'))
    return text


def contact_detail():
    text = markdown_decoration.bold(_(f'📞 Aloqa:\n\nBog`lanish uchun raqamingizni kiriting\n'
                                      f'Yoki pastgi tugmani bosing?\n'
                                      f'Masalan, +998 90 123 45 67'))
    return text


def technology_detail():
    text = markdown_decoration.bold(_('📚 Texnologiya:\n\n'
                                      'Talab qilinadigan texnologiyalarni kiriting?\n'
                                      'Texnologiya nomlarini vergul bilan ajrating.\n Masalan, Java, C++, C#'))
    return text


def price_detail():
    text = markdown_decoration.bold(_('💰 Narxi:\n\nTolov qilasizmi yoki Tekinmi?\nKerak bo`lsa, Summani kiriting?'))
    return text


def name_detail():
    text = markdown_decoration.bold(_('Ism, familiyangizni kiriting!'))
    return text


def detail_job():
    text = markdown_decoration.bold(_('👨🏻‍💻 Kasbi:\n\nIshlaysizmi yoki o`qiysizmi?\nMasalan, Talaba'))
    return text


def detail_goal():
    text = markdown_decoration.bold(_('🔎 Maqsad:\n\nMaqsadingizni qisqacha yozib bering.'))
    return text


def age_detail():
    text = markdown_decoration.bold(_('🕑 Yosh:\n\nYoshingizni kiriting?\nMasalan, 19'))
    return text
