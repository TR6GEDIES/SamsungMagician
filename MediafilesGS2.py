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
# Name: MediafilesGS2
# Author: https://t.me/SamsungMagician
# ---------------------------------------------------------------------------------

__version__ = (1, 0, 2)

# meta developer: @SamsungMagician (main developer @mqone)

from .. import loader, utils
import logging
import asyncio

logger = logging.getLogger(__name__)

@loader.tds
class MediafilesGS2(loader.Module):
    """Отправляет гс с канала https://t.me/MediafilesForModule"""

    strings = {"name": "MediafilesGS2",
               "channel": "Поддержи разработчика 💫",
               "welcome": (
                   "🖐 <i>Приветствую, ты запустил установку модуля <b>„MediafilesGS2“</b></i>"
                   "\n\n🔗 <i>Модуль работает через канал https://t.me/MediafilesForModule</i>"
                   "\n\n🩸 <i>Создан by <code>@SamsungMagician</code></i>"),
               }

    async def on_dlmod(self):
        await self.inline.bot.send_photo(
            self._client._self_id,
            "https://pomf2.lain.la/f/szt9c2fz.jpg",
            caption=self.strings("welcome"),
        )


    async def client_ready(self, client, db) -> None:
        self.db = db
        self.client = client

        logger.info("Модуль MediafilesGS2 успешно загружен!")

        await self.request_join(
            "@SamsungMagicianModules",
            self.strings['channel'],
        )

    # 1
    async def баг1cmd(self, message):
        """— Баг 1"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/MediafilesForModule/36",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    # 2
    async def баг2cmd(self, message):
        """— Баг 2"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/MediafilesForModule/37",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    # 3
    async def баг3cmd(self, message):
        """— Баг 3"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/MediafilesForModule/38",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    # 4
    async def баг4cmd(self, message):
        """— Баг 4"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/MediafilesForModule/39",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    # 5
    async def баг5cmd(self, message):
        """— Баг 5"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/MediafilesForModule/41",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    # 6
    async def баг6cmd(self, message):
        """— Баг 6"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/MediafilesForModule/42",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    # 7
    async def гитлер1cmd(self, message):
        """— Осуждаем такое 1"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/MediafilesForModule/43",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    # 8
    async def гитлер2cmd(self, message):
        """— Осуждаем такое 2"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/MediafilesForModule/44",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    # 9
    async def гитлер3cmd(self, message):
        """— Осуждаем такое 3"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/MediafilesForModule/46",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    # 10
    async def секс1cmd(self, message):
        """— Тихий омут"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/MediafilesForModule/63",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    # 11
    async def секс2cmd(self, message):
        """— Сочные первоклашки"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/MediafilesForModule/77",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    # 12
    async def секс3cmd(self, message):
        """— Популярная игра"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/MediafilesForModule/78",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    # 13
    async def секс4cmd(self, message):
        """— Украинский секс-шоп"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/MediafilesForModule/86",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    # 14
    async def секс5cmd(self, message):
        """— Секс-шоп для пенсионеров"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/MediafilesForModule/87",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
