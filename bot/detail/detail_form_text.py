from aiogram.utils.i18n import gettext as _, lazy_gettext as __
from aiogram.utils.text_decorations import markdown_decoration


def detail_form(msg, data: dict):
    button = data.get('button')
    employee = _('Hodim')
    need = _('kerak')
    age = _('🕑 Yosh')
    technology = _('Texnologiya')
    contact = _('Aloqa')
    area = _('Hudud')
    salary = _('Narxi')
    job = _('Kasbi')
    appeal = _('Murojaat qilish vaqti')
    goal = _('Maqsad')
    if button == __('Hodim'):
        employee = _('🏢 Idora')
        age = _('✍️Mas\'ul')
        salary = _('Maosh')
        job = _('Ish vaqti')
        goal = _('Qo`shimcha ma`lumot')
    text = markdown_decoration.bold(f'''
{button} {need} :

👨‍💼 {employee}: {data.get('name')}
{age}: {data.get('age')}
📚 {technology}: {data.get('technology')} 
📞 {contact}: {data.get('contact')}
🌐 {area}: {data.get('area')}
💰 {salary}: {data.get('price')}
👨🏻‍💻 {job}: {data.get('job')}
🕰 {appeal}: {data.get('appeal')}
📝 {goal}: {data.get('goal')}

Telegram: @{msg.from_user.username}
#{button}
    ''')
    return text


def detail_channel(info_chat):
    text = markdown_decoration.bold(f'''
Info {info_chat.type if info_chat.type != 'private' else info_chat.type + ' ' + 'bot'}
Name: {info_chat.full_name}
Username: {info_chat.username}
Chat ID: {markdown_decoration.code(info_chat.id)}
Tasdiqlashni bosing
    ''')
    return text