from telethon import TelegramClient, events
from telethon.tl.functions.messages import SendMessageRequest
from telethon.tl.functions.messages import GetDialogsRequest
import asyncio, time
import asyncio
import base64
from telethon.tl import functions, types
from telethon.tl.functions.messages import GetStickerSetRequest
from telethon.tl.functions.messages import ImportChatInviteRequest as Get


# DATA
api_id = 1724716
api_hash = "00b2d8f59c12c1b9a4bc63b70b461b2f"

iqthon = TelegramClient("Test", api_id, api_hash)
iqthon.start()

StopSpamming = False


# post
async def PostNow(event, chat_id, RepeatParagraph, Delay):
    os_send = await event.client(SendMessageRequest(peer=chat_id, message=RepeatParagraph))
    await asyncio.sleep(int(Delay))

# مؤقت
@iqthon.on(events.NewMessage(outgoing=True, pattern=r'.ن ?(.*)'))
async def RepeatTimer(event):
    global StopSpamming
    
    StopSpamming = False
    
    # الصيغة : ن - عدد ثواني - عدد مرات - الجملة
    MESSAGE = ((event.message.message).replace("ن", "")).split("-")
    try :
        Delay = int(MESSAGE[1])
        RepeatCount = int(MESSAGE[2])
        ChatIdPost = event.chat_id
        RepeatParagraph = MESSAGE[3]
        
        
        try:
            os_success = await event.edit(f'**تم تاكيد الطلب**')
            for x in range(0, int(RepeatCount)):
                if StopSpamming == True:
                    break
                try:
                    await PostNow(event, ChatIdPost, RepeatParagraph, Delay)
                except Exception as error:
                    await event.reply(f'لم يستطيع النشر هنا : {ChatIdPost}\n\nالسبب : {error}')
                    
        except:
            os_failed = await event.edit(f'**بالرجاء التأكد من قيمة عدد الثواني و التكرار**')
    except:
        os_failed = await event.edit(f'**بالرجاء استخدام الصيفة التالية :\n\nالصيغة : ن - عدد ثواني - عدد مرات - الجملة**')
    
# stop
@iqthon.on(events.NewMessage(outgoing=True, pattern=r'.س'))
async def RepeatTimer(event):
    global StopSpamming
    
    StopSpamming = True
    await event.reply('**سيتم ايقاف الأمر قريبا**')


@iqthon.on(events.NewMessage(outgoing=True, pattern=".للخاص ?(.*)"))    
async def gucast(event):
    if not event.out and not is_fullsudo(event.sender_id):
        return await edit_or_reply(event, "هـذا الامـر مقـيد ")
    xx = event.pattern_match.group(1)
    if not xx:
        return edit_or_reply(event, "** 🝳 ⦙   يجـب وضـع نـص مع الامـر للتوجيـه**")
    tt = event.text
    msg = tt[7:]
    await edit_or_reply(event, "** 🝳 ⦙   يتـم الـتوجيـة للخـاص انتـظر قليلا**")
    er = 0
    done = 0
    async for x in bot.iter_dialogs():
        if x.is_user and not x.entity.bot:
            chat = x.id
            try:
                done += 1
                await bot.send_message(chat, msg)
            except BaseException:
                er += 1
    await event.edit(f"🝳 ⦙   تـم بنـجـاح فـي {done} من الـدردشـات , خطـأ فـي {er} من الـدردشـات")
    
@iqthon.on(events.NewMessage(outgoing=True, pattern=".للكروب ?(.*)"))
async def gcast(event):
    if not event.out and not is_fullsudo(event.sender_id):
        return await edit_or_reply(event, "هـذا الامـر مقـيد ")
    xx = event.pattern_match.group(1)
    if not xx:
        return edit_or_reply(event, "**🝳 ⦙   يجـب وضـع نـص مع الامـر للتوجيـه**")
    tt = event.text
    msg = tt[6:]
    event = await edit_or_reply(event, "** 🝳 ⦙   يتـم الـتوجيـة للـمجموعـات انتـظر قليلا**")
    er = 0
    done = 0
    async for x in bot.iter_dialogs():
        if x.is_group:
            chat = x.id
            try:
                done += 1
                await bot.send_message(chat, msg)
            except BaseException:
                er += 1
    await event.edit(f"🝳 ⦙   تـم بنـجـاح فـي {done} من الـدردشـات , خطـأ فـي {er} من الـدردشـات")    
    


iqthon.run_until_disconnected()