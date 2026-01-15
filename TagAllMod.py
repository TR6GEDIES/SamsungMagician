# ---------------------------------------------------------------------------------
# 鑓塵幗膂蓿f寥寢膃暠瘉甅甃槊槎f碣綮瘋聟碯颱亦尓㍍i:i:i;;:;:: : :
# 澣幗嶌塹傴嫩榛畝皋i袍耘蚌紕欒儼巓襴踟篁f罵f亦尓㍍i:i:i;;:;:: : :
# 漲蔭甃縟諛f麭窶膩I嶮薤篝爰曷樔黎㌢´　　｀ⅷ踟亦尓㍍i:i:i;;:;:: : :
# 蔕漓滿f蕓蟇踴f歙艇艀裲f睚鳫巓襴骸　　　　　贒憊亦尓㍍i:i:i;;:;:: : :
# 榊甃齊爰f懈橈燗殪幢緻I翰儂樔黎夢'”　 　 ,ｨ傾篩縒亦尓㍍i:i:i;;:;:: : :
# 箋聚蜚壊劑薯i暹盥皋袍i耘蚌紕偸′　　　 雫寬I爰曷f亦尓㍍i:i:i;;:;:: : :
# 銕颱麼寰篝螂徑悗f篝嚠篩i縒縡齢　　 　 　 Ⅷ辨f篝I鋗f亦尓㍍i:i:i;;:; : : .
# 碯聟f綴麼辨螢f璟輯駲f迯瓲i軌帶′　　　　　`守I厖孩f奎亦尓㍍i:i:i;;:;:: : : .
# 綮誣撒f曷磔瑩德f幢儂儼巓襴緲′　 　 　 　 　 `守枢i磬廛i亦尓㍍i:i:i;;:;:: : : .
# 慫寫廠徑悗緞f篝嚠篩I縒縡夢'´　　　 　 　 　 　 　 `守峽f徑悗f亦尓㍍i:i:i;;:;:: : : .
# 廛僵I數畝篥I熾龍蚌紕襴緲′　　　　　　　　　　　　　‘守畝皋弊i劍亦尓㍍i:i:i;;:;:: : : .
# 瘧i槲瑩f枢篝磬曷f瓲軌揄′　　　　　　　　　　　　　,gf毯綴徑悗嚠迩忙亦尓㍍i:i:i;;:;::
# 襴罩硼f艇艀裲睚鳫襴鑿緲'　　　　　　　　　　 　 　 奪寔f厦傀揵猯i爾迩忙亦尓㍍i:i:
# 椈棘斐犀耋絎絲絨緲′　　　　　　 　 　 　 　 　 　 　 ”'罨悳萪f蒂渹幇f廏迩忙i亦尓㍍
# 潁樗I瘧德幢i儂巓緲′　　　　　　 　 　 　 　 　 　 r㎡℡〟”'罨椁裂滅楔滄愼愰迩忙亦
# 翦i磅艘溲I搦儼巓登zzz zzz㎜㎜ｧg　 　 緲 g　 　 甯體i爺ゎ｡, ”'罨琥焜毳徭i嵬塰慍絲
# 枢篝磬f曷迯i瓲軌f襴暹 甯幗緲 ,fi'　　 緲',纜｡　　贒i綟碕碚爺ゎ｡ ”'罨皴發傲亂I黹靱
# 緞愾慊嵬嵯欒儼巓襴驫 霤I緲 ,緲　　 ＂,纜穐　　甯絛跨飩i髢馳爺ゎ｡`'等誄I筴碌I畷
# 罩硼I蒻筵硺艇艀i裲睚亀 篳'’,緲　　g亀 Ⅶil齢　　贒罩硼i艇艀裲睚鳫爺靠飭蛸I裘裔
# 椈f棘豢跫跪I衙絎絲絨i爺i㎜iⅣ 　 ,緲i亀 Ⅶ靈,　　甯傅喩I揵揚惹屡絎痙棏敞裔筴敢
# 頬i鞏褂f跫詹雋髢i曷迯瓲軌霤 　 ,緲蔭穐 Ⅶ穐 　 讎椈i棘貅f斐犀耋f絎絲觚f覃黹黍
# 襴蔽戮貲艀舅I肅肄肆槿f蝓Ⅷ 　 緲$慚I穐,疊穐　 甯萪碾f鋗輜靠f誹臧鋩f褂跫詹i雋
# ---------------------------------------------------------------------------------
# 🌐 This project was created https://t.me/SamsungMagician
# ⚠️ Licensed under the GNU AGPLv3.
# 💢 The owner of this script does not have any responsibility or intellectual property rights in relation to this script.
# ---------------------------------------------------------------------------------
# Name: TagAllMod
# Author: https://t.me/SamsungMagician
# ---------------------------------------------------------------------------------

__version__ = (1, 0, 0)

# meta developer: @SamsungMagician

import asyncio
import contextlib
import logging
import random

from aiogram import Bot
from hikkatl.tl.functions.channels import InviteToChannelRequest
from hikkatl.tl.types import Message

from .. import loader, utils
from ..inline.types import InlineCall

logger = logging.getLogger(__name__)


class StopEvent:
    def __init__(self):
        self.state = True

    def stop(self):
        self.state = False


@loader.tds
class TagAllMod(loader.Module):
    """Форк, в котором модули TagAll и TagAll_Bot интегрированы в один"""

    strings = {
        "name": "TagAllMod",
        "bot_error": "🚫 <b>Unable to invite inline bot to chat</b>",
        "_cfg_doc_default_message": "Default message of mentions",
        "_cfg_doc_delete": "Delete messages after tagging",
        "_cfg_doc_use_bot": "Use inline bot to tag people",
        "_cfg_doc_timeout": "What time interval to sleep between each tag message",
        "_cfg_doc_silent": "Do not send message with cancel button",
        "_cfg_doc_cycle_tagging": (
            "Tag all participants over and over again until you stop the script using"
            " the button in the message"
        ),
        "_cfg_doc_cycle_delay": "Delay between each cycle of tagging in seconds",
        "gathering": "🧚‍♀️ <b>Calling participants of this chat...</b>",
        "cancel": "🚫 Cancel",
        "cancelled": "🧚‍♀️ <b>TagAll cancelled!</b>",
        "channel": "Support the developer 💫",
        "welcome": (
            "🖐 <i>Greetings, you have started the module installation. <b>«TagAllMod»</b></i>"
            "\n\n🤍 <i>Thank you for the installation</i>"
            "\n\n⚙️ <i>Create by <code>@SamsungMagician</code></i>"),
    }

    strings_ru = {
        "bot_error": "🚫 <b>Не получилось пригласить бота в чат</b>",
        "_cls_doc": (
            "Отмечает всех участников чата, используя инлайн бот или классическим"
            " методом"
        ),
        "_cfg_doc_default_message": "Сообщение по умолчанию для тегов",
        "_cfg_doc_delete": "Удалять сообщения после тега",
        "_cfg_doc_use_bot": "Использовать бота для тегов",
        "_cfg_doc_timeout": "Время между сообщениями с тегами",
        "_cfg_doc_silent": "Не отправлять сообщение с кнопкой отмены",
        "_cfg_doc_cycle_tagging": (
            "Тегать всех участников снова и снова, пока вы не остановите скрипт,"
            " используя кнопку в сообщении"
        ),
        "_cfg_doc_cycle_delay": "Задержка между циклами тегов в секундах",
        "gathering": "<b>Сбор участников чата...</b>",
        "cancel": "🚫 Отмена",
        "cancelled": "️ <b>Сбор отменен!</b>",
        "channel": "Поддержи разработчика 💫",
        "welcome": (
            "🖐 <i>Приветствую, ты запустил установку модуля <b>«TagAllMod»</b></i>"
            "\n\n🤍 <i>Благодарю за установку</i>"
            "\n\n⚙️ <i>Создан by <code>@SamsungMagician</code></i>"),
    }

    strings_de = {
        "bot_error": "🚫 <b>Einladung des Inline-Bots in den Chat fehlgeschlagen</b>",
        "_cfg_doc_default_message": "Standardnachricht für Erwähnungen",
        "_cfg_doc_delete": "Nachrichten nach Erwähnung löschen",
        "_cfg_doc_use_bot": "Inline-Bot verwenden, um Leute zu erwähnen",
        "_cfg_doc_timeout": (
            "Zeitintervall, in dem zwischen den Erwähnungen gewartet wird"
        ),
        "_cfg_doc_silent": "Nachricht ohne Abbrechen-Button senden",
        "_cfg_doc_cycle_tagging": (
            "Alle Teilnehmer immer wieder erwähnen, bis du das Skript mit der"
            " Schaltfläche in der Nachricht stoppst"
        ),
        "_cfg_doc_cycle_delay": (
            "Verzögerung zwischen jedem Zyklus der Erwähnung in Sekunden"
        ),
        "gathering": "🧚‍♀️ <b>Erwähne Teilnehmer dieses Chats...</b>",
        "cancel": "🚫 Abbrechen",
        "cancelled": "🧚‍♀️ <b>TagAll abgebrochen!</b>",
        "channel": "Unterstütze die Entwickler 💫",
        "welcome": (
            "🖐 <i>Hallo, du hast die Installation des Moduls gestartet <b>«TagAllMod»</b></i>"
            "\n\n🤍 <i>Danke für die Installation</i>"
            "\n\n⚙️ <i>Geschaffen by <code>@SamsungMagician</code></i>"),
    }

    strings_tr = {
        "bot_error": "🚫 <b>Inline botunu sohbete davet edilemedi</b>",
        "_cfg_doc_default_message": "Varsayılan etiket mesajı",
        "_cfg_doc_delete": "Etiketledikten sonra mesajları sil",
        "_cfg_doc_use_bot": "İnsanları etiketlemek için inline botu kullan",
        "_cfg_doc_timeout": "Her etiket mesajı arasında ne kadar bekleneceği",
        "_cfg_doc_silent": "İptal düğmesi olmadan mesaj gönderme",
        "_cfg_doc_cycle_tagging": (
            "Mesajdaki düğmeyi kullanarak betiği durdurana kadar tüm katılımcıları"
            " tekrar tekrar etiketle"
        ),
        "_cfg_doc_cycle_delay": "Etiketleme döngüsü arasındaki gecikme süresi (saniye)",
        "gathering": "🧚‍♀️ <b>Bu sohbetteki katılımcıları çağırıyorum...</b>",
        "cancel": "🚫 İptal",
        "cancelled": "🧚‍♀️ <b>TagAll iptal edildi!</b>",
        "channel": "Geliştirici destek 💫",
        "welcome": (
            "🖐 <i>Selamlar, modül kurulumunu başlattınız <b>«TagAllMod»</b></i>"
            "\n\n🤍 <i>Kurulum için teşekkür ederim</i>"
            "\n\n⚙️ <i>Oluşturuldu by <code>@SamsungMagician</code></i>"),
    }

    strings_uz = {
        "bot_error": (
            "🚫 <b>Inline botni chatga taklif qilish muvaffaqiyatsiz bo‘ldi</b>"
        ),
        "_cfg_doc_default_message": "Odatiy etiket xabari",
        "_cfg_doc_delete": "Etiketdan so‘ng xabarlarni o‘chirish",
        "_cfg_doc_use_bot": "Odamlarni etiketlash uchun inline botdan foydalanish",
        "_cfg_doc_timeout": "Har bir etiket xabari orasida nechta kutish kerak",
        "_cfg_doc_silent": "Bekor tugmasi olmadan xabar jo‘natish",
        "_cfg_doc_cycle_tagging": (
            "Xabar bo‘yicha tugmani ishlatib, skriptni to‘xtatguncha barcha"
            " qatnashuvchilarni qayta-qayta etiketlash"
        ),
        "_cfg_doc_cycle_delay": "Har bir etiketlash tsikli orasida gecikma (soniya)",
        "gathering": "🧚‍♀️ <b>Ushbu chatta qatnashganlarni chaqiraman...</b>",
        "cancel": "🚫 Bekor qilish",
        "cancelled": "🧚‍♀️ <b>TagAll bekor qilindi!</b>",
        "channel": "Ishlab chiquvchini qo'llab-quvvatlang 💫",
        "welcome": (
            "🖐 <i>Salom, siz modulni o'rnatishni boshladingiz <b>«TagAllMod»</b></i>"
            "\n\n🤍 <i>O'rnatish uchun rahmat</i>"
            "\n\n⚙️ <i>Yaratilgan by <code>@SamsungMagician</code></i>"),
    }

    def __init__(self):
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "default_message",
                "@all",
                lambda: self.strings("_cfg_doc_default_message"),
            ),
            loader.ConfigValue(
                "delete",
                False,
                lambda: self.strings("_cfg_doc_delete"),
                validator=loader.validators.Boolean(),
            ),
            loader.ConfigValue(
                "use_bot",
                False,
                lambda: self.strings("_cfg_doc_use_bot"),
                validator=loader.validators.Boolean(),
            ),
            loader.ConfigValue(
                "timeout",
                0.1,
                lambda: self.strings("_cfg_doc_timeout"),
                validator=loader.validators.Float(minimum=0),
            ),
            loader.ConfigValue(
                "silent",
                False,
                lambda: self.strings("_cfg_doc_silent"),
                validator=loader.validators.Boolean(),
            ),
            loader.ConfigValue(
                "cycle_tagging",
                False,
                lambda: self.strings("_cfg_cycle_tagging"),
                validator=loader.validators.Boolean(),
            ),
            loader.ConfigValue(
                "cycle_delay",
                0,
                lambda: self.strings("_cfg_cycle_delay"),
                validator=loader.validators.Integer(minimum=0),
            ),
        )


    async def on_dlmod(self):
        await self.inline.bot.send_photo(
            self._client._self_id,
            "https://pomf2.lain.la/f/n93g4nzd.jpg",
            caption=self.strings("welcome"),
        )

    async def client_ready(self, client, db) -> None:
        self.db = db
        self.client = client

        logger.info("Модуль TagAllMod успешно загружен и готов к работе!")

        await self.request_join(
            "@SamsungMagicianModules",
            self.strings['channel'],
        )

    async def cancel(self, call: InlineCall, event: StopEvent):
        event.stop()
        await call.answer(self.strings("cancel"))

    @loader.command(
        groups=True,
        ru_doc="[текст] - отметить всех участников чата используя бота",
        de_doc="[Text] - Alle Chatteilnehmer erwähnen",
        tr_doc="[metin] - Sohbet katılımcılarını etiketle",
        uz_doc="[matn] - Chat qatnashuvchilarini tegish",
    )
    async def tq(self, message: Message):
        """[текст] - отметить всех участников чата используя бота"""
        args = utils.get_args_raw(message)
        if message.out:
            await message.delete()

        if self.config["use_bot"]:
            try:
                await self._client(
                    InviteToChannelRequest(message.peer_id, [self.inline.bot_username])
                )
            except Exception:
                await utils.answer(message, self.strings("bot_error"))
                return

            with contextlib.suppress(Exception):
                Bot.set_instance(self.inline.bot)

            chat_id = int(f"-100{utils.get_chat_id(message)}")
        else:
            chat_id = utils.get_chat_id(message)

        event = StopEvent()

        if not self.config["silent"]:
            cancel = await self.inline.form(
                message=message,
                text=self.strings("gathering"),
                reply_markup={
                    "text": self.strings("cancel"),
                    "callback": self.cancel,
                    "args": (event,),
                },
            )

        first, br = True, False
        while True if self.config["cycle_tagging"] else first:
            for chunk in utils.chunks(
                [
                    f'<a href="tg://user?id={user.id}">\xad</a>'
                    async for user in self._client.iter_participants(message.peer_id)
                ],
                5,
            ):
                m = await (
                    self.inline.bot.send_message
                    if self.config["use_bot"]
                    else self._client.send_message
                )(
                    chat_id,
                    utils.escape_html(args or self.config["default_message"])
                    + "\xad".join(chunk),
                )

                if self.config["delete"]:
                    with contextlib.suppress(Exception):
                        await m.delete()

                async def _task():
                    nonlocal event, cancel
                    if not self.config["silent"]:
                        return

                    while True:
                        if not event.state:
                            await cancel.edit(self.strings("cancelled"))
                            return

                        await asyncio.sleep(0.1)

                task = asyncio.ensure_future(_task())
                await asyncio.sleep(self.config["timeout"])
                task.cancel()
                if not event.state:
                    br = True
                    break

            if br:
                break

            first = False
            if self.config["cycle_tagging"]:
                await asyncio.sleep(self.config["cycle_delay"])

        if cancel is not None:
            try:
                await cancel.delete()
            except AttributeError:
                try:
                    await cancel.edit(self.strings("cancelled"))
                except:
                    pass
            except Exception as e:
                logger.warning(f"[TagAllMod] Error deleting inline message: {e}")


    async def tagcmd(self, message):
        """.tag <@> <text> - отметить пользователя в чате"""
        args = utils.get_args_raw(message).split(" ")
        reply = await message.get_reply_message()
        user, tag = None, None
        try:
            if len(args) == 1:
                args = utils.get_args_raw(message)
                user = await message.client.get_entity(
                    args if not args.isnumeric() else int(args)
                )
                tag = "ᅠ"
            elif len(args) >= 2:
                user = await message.client.get_entity(
                    args[0] if not args[0].isnumeric() else int(args[0])
                )
                tag = utils.get_args_raw(message).split(" ", 1)[1]
        except:
            return await message.edit("Failed to find a user.")
        await message.delete()
        await message.client.send_message(
            message.to_id,
            f'{tag} <a href="tg://user?id={user.id}">\u2060</a>',
            reply_to=reply.id if reply else None,
        )


    async def tagallcmd(self, message):
        """.tagall <текст> - отметить всех участников чата"""
        args = utils.get_args_raw(message)
        tag = args or "ᅠ"
        await message.delete()
        tags = []
        async for user in message.client.iter_participants(message.to_id):
            tags.append(f"<a href='tg://user?id={user.id}'>\u2060</a>")
        chunkss = list(chunks(tags, 5))
        random.shuffle(chunkss)
        for chunk in chunkss:
            await message.client.send_message(message.to_id, tag + "\u2060".join(chunk))


def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i : i + n]

