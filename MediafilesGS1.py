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
# Name: MediafilesGS1
# Author: https://t.me/SamsungMagician
# ---------------------------------------------------------------------------------

__version__ = (1, 0, 2)

# meta developer: @SamsungMagician (main developer @mqone)

from .. import loader
import logging
import asyncio

@loader.tds
class MediafilesGS1(loader.Module):
    """Отправляет гс с канала https://t.me/MediafilesForModule"""

    strings = {"name": "MediafilesGS1",
               "channel": "💫 Поддержи разработчика",
               "welcome": (
                   "🖐 <i>Приветствую, ты запустил установку модуля <b>„MediafilesGS1“</b></i>"
                   "\n\n🔗 <i>Модуль работает через канал https://t.me/MediafilesForModule</i>"
                   "\n\n🩸 <i>Создан by <code>@SamsungMagician</code></i>"),
               }

    async def on_dlmod(self, client):
        await self.inline.bot.send_photo(
            client._tg_id,
            "https://pomf2.lain.la/f/f6dchfic.jpg",
            caption=self.strings("welcome"),
        )


    async def client_ready(self) -> None:
        logging.info("Модуль MediafilesGS1 успешно загружен!")

        await self.request_join(
            "@SamsungMagicianModules",
            self.strings['channel'],
        )

    # 1
    async def недоксcmd(self, message):
        """— Братан только недокс"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/MediafilesForModule/27",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    # 2
    async def шамильcmd(self, message):
        """— Я чеченец я мусульманин"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/MediafilesForModule/28",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    # 3
    async def анимешникcmd(self, message):
        """— Анимешник бля"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/MediafilesForModule/29",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    # 4
    async def точиклюблюcmd(self, message):
        """— Сильно люблю"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/MediafilesForModule/30",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    # 5
    async def долларыcmd(self, message):
        """— Два доллара"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/MediafilesForModule/31",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    # 6
    async def наебаловоcmd(self, message):
        """— Стоны"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/MediafilesForModule/32",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    # 7
    async def отношенияcmd(self, message):
        """— Сигма"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/MediafilesForModule/33",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    # 8
    async def стандофчекcmd(self, message):
        """— Мне попадается читер"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/MediafilesForModule/34",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    # 9
    async def тупойcmd(self, message):
        """— Потому что похож на негра"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/MediafilesForModule/35",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    # 10
    async def сигматрекcmd(self, message):
        """— Пельмени чаек сигма трек"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/MediafilesForModule/47",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    # 11
    async def бабулька1cmd(self, message):
        """— Я ебу ебу бабульку"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/MediafilesForModule/64",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    # 12
    async def бабулька2cmd(self, message):
        """— Я ебу ебу бабульку"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/MediafilesForModule/65",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    # 13
    async def анимеcmd(self, message):
        """— Я не могу больше себя сдерживать"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/MediafilesForModule/80",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    # 14
    async def девочкаcmd(self, message):
        """— Доброе утро моя девочка"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/MediafilesForModule/82",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    # 15
    async def папанебейcmd(self, message):
        """— А хуй знает что тут происходит"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/MediafilesForModule/85",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    # 16
    async def оксимиронcmd(self, message):
        """— Задание на 5+"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/MediafilesForModule/81",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    # 17
    async def данечкаcmd(self, message):
        """— Д-д-данечка.."""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/MediafilesForModule/115",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    # 18
    async def пасикcmd(self, message):
        """— До меня инфа дошла"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/MediafilesForModule/120",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
