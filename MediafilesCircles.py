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
# Name: MediafilesCircles
# Author: https://t.me/SamsungMagician
# ---------------------------------------------------------------------------------

__version__ = (1, 0, 4)

# meta developer: @SamsungMagician (idea by @mqone)

from .. import loader, utils
import asyncio
import logging

logger = logging.getLogger(__name__)

@loader.tds
class MediafilesCircles(loader.Module):
    """Отправляет кружки"""

    strings = {"name": "MediafilesCircles",
               "channel": "Поддержи разработчика 💫",
               "welcome": (
                   "🖐 <i>Приветствую, ты запустил установку модуля <b>«MediafilesCircles»</b></i>"
                   "\n\n🤍 <i>Благодарю за установку</i>"
                   "\n\n⚙️ <i>Создан by <code>@SamsungMagician</code></i>"),
               }

    async def on_dlmod(self):
        await self.inline.bot.send_photo(
            self._client._self_id,
            "https://pomf2.lain.la/f/5ew1n33q.jpg",
            caption=self.strings("welcome"),
        )


    async def client_ready(self, client, db) -> None:
        self.db = db
        self.client = client

        logger.info("Модуль MediafilesCircles успешно загружен!")

        await self.request_join(
            "@SamsungMagicianModules",
            self.strings['channel'],
        )


    async def дефcmd(self, message):
        """— Деф1"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/MediafilesForModule/13",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def деф2cmd(self, message):
        """— Деф2"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/MediafilesForModule/7",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def деф3cmd(self, message):
        """— Прокуратура глаз бога"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/MediafilesForModule/11",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def кровьcmd(self, message):
        """— Кровь самочек"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/MediafilesForModule/10",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def сисяндрыcmd(self, message):
        """— Сисяндры"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/MediafilesForModule/12",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def миягиcmd(self, message):
        """— Мияги"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/MediafilesForModule/14",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def лютыйcmd(self, message):
        """— Лютый"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/MediafilesForModule/15",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def подшарcmd(self, message):
        """— Подшар 52"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/MediafilesForModule/16",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return



    async def недобавляйтеcmd(self, message):
        """— Недобавляйте меня"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/MediafilesForModule/17",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def смехcmd(self, message):
        """— Троллфейс"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/MediafilesForModule/18",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def ракеткаcmd(self, message):
        """— Ракетка Асхаб"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/MediafilesForModule/19",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def дозаcmd(self, message):
        """— Перебор дозы"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/MediafilesForModule/20",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def сигмаcmd(self, message):
        """— Сигма based"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/MediafilesForModule/21",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def цыганеcmd(self, message):
        """— Цыгане в моде"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/MediafilesForModule/22",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def осуждаюcmd(self, message):
        """— Осуждаю Глебасик"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/MediafilesForModule/23",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def доза2cmd(self, message):
        """— Перебор дозы2"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/MediafilesForModule/24",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def веляcmd(self, message):
        """— Веля стоны"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/MediafilesForModule/25",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def ботанcmd(self, message):
        """— А вот фиг вам"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/MediafilesForModule/59",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def боксcmd(self, message):
        """— А вот фиг вам"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/MediafilesForModule/68",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def борзыйcmd(self, message):
        """— А вот фиг вам"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/MediafilesForModule/72",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def скибидиcmd(self, message):
        """— Скибиди подшар"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/MediafilesForModule/73",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def салехардcmd(self, message):
        """— В Салехарде любят"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/MediafilesForModule/102",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def ванекcmd(self, message):
        """— Ай леф ай тигр"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/MediafilesForModule/83",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def твичараcmd(self, message):
        """— Твич момент"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/MediafilesForModule/95",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def голдаcmd(self, message):
        """— Дай голды"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/MediafilesForModule/98",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def биллиcmd(self, message):
        """— В наших сердцах"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/MediafilesForModule/99",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def фанатcmd(self, message):
        """— Фанаты заебали меня"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/MediafilesForModule/100",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def гамарджобаcmd(self, message):
        """— Что он вытворяет"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/MediafilesForModule/101",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def казимирcmd(self, message):
        """— Пасасите дилду"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/MediafilesForModule/104",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def казимир2cmd(self, message):
        """— Идите нахуй"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/MediafilesForModule/105",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def разъеб1cmd(self, message):
        """— Нет иди нахуй"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/MediafilesForModule/107",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def разъеб2cmd(self, message):
        """— Пизда динамикам"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/MediafilesForModule/108",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def разъеб3cmd(self, message):
        """— Сердешко"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/MediafilesForModule/109",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def пиздаcmd(self, message):
        """— Пизда"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/MediafilesForModule/110",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def разъеб4cmd(self, message):
        """— Первое правило подписчиков"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/MediafilesForModule/111",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def разъеб5cmd(self, message):
        """— Я бы хотел заказать"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/MediafilesForModule/112",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def разъеб6cmd(self, message):
        """— Профессии"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/MediafilesForModule/113",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def антивирусcmd(self, message):
        """— Хуйня антивирус"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/MediafilesForModule/114",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def пиздюкcmd(self, message):
        """— Расслабляется молодой человек"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/MediafilesForModule/116",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def легендаcmd(self, message):
        """— Да нахер вообще это комментить"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/MediafilesForModule/117",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def заходcmd(self, message):
        """— Заходик в котакбаса"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/MediafilesForModule/119",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def танецcmd(self, message):
        """— Сегодня я покажу вам танец..."""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/MediafilesForModule/121",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def трюкачcmd(self, message):
        """— АХХАХАХАХХАХАХ"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/MediafilesForModule/123",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def сисяндры2cmd(self, message):
        """— Ну блять, ясен хуй что это"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/MediafilesForModule/124",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def джедайcmd(self, message):
        """— Non comment"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/MediafilesForModule/125",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

