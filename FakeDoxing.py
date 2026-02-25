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
# Name: FakeDoxing
# Author: https://t.me/SamsungMagician
# ---------------------------------------------------------------------------------

__version__ = (1, 0, 0)

# meta developer: @SamsungMagician (main developer @none)

import logging
from .. import loader, utils
from asyncio import sleep
import random

logger = logging.getLogger(__name__)

@loader.tds
class FakeDoxing(loader.Module):
    """Форк на фейк докс модуль. Извиняйте, потерял изначального разработчика("""

    strings = {'name': 'FakeDoxing',
               "channel": "Поддержи разработчика 💫",
               "welcome": (
                   "🖐 <i>Приветствую, ты запустил установку модуля <b>«FakeDoxing»</b></i>"
                   "\n\n🤍 <i>Благодарю за установку</i>"
                   "\n\n⚙️ <i>Создан by <code>@SamsungMagician</code></i>"),
               }

    async def on_dlmod(self):
        await self.inline.bot.send_photo(
            self._client._self_id,
            "https://pomf2.lain.la/f/zcb6y6q.jpg",
            caption=self.strings("welcome"),
        )

    async def client_ready(self, client, db) -> None:
        self.db = db
        self.client = client

        await self.request_join(
            "@SamsungMagicianModules",
            self.strings['channel'],
        )

    @loader.command(alias='доксинг')
    async def doxing(self, message):
        """[реплай] - запуск фейк доксинга"""

        dox_msg = [
            "⛓ <b>Нᴀчиnᴀю ᴅ0ᴋs...</b>",
            "☠️ <b>3aпр0s принят, п0лучаю инф0рмацию...</b>", 
            "🚫 <b>п0шᴇл нахуй</b>"
            ]

        dox_welcome = random.choice(dox_msg)

        message = await utils.answer(message, dox_welcome)
        await sleep(2)

        request_msg = [
            "💣 <b>П0лʏчᴀю 3ᴀпр0s</b> <code>[ 3% ] </code>",
            "💥 <b>Инф0рмᴀция не нᴀйдена"
            ]

        request = random.choice(request_msg)

        await utils.answer(message, request)
        await sleep(1)

        await utils.answer(message, "🔄 <b>Sвᴇᴘяю s иnф0рмᴀциᴇй и3 бᴀ3 дᴀннblx</b> <code> [ 7% ]")
        await sleep(1)

        await utils.answer(message, "❌ <b>Дᴀннblᴇ ʜᴇ s0ʙпᴀли, п0вт0ряᴇᴍ 3ᴀпр0с..</b> <code> [ 13% ]</code>")
        await sleep(1)

        await utils.answer(message, "♻️ <b>0брᴀбᴀтblвᴀю инф0рмᴀцию...</b> <code> [ 17% ]</code>")
        await sleep(1.5)

        await utils.answer(message, "♻️ <b>0брᴀбᴀтblвᴀю инф0рмᴀцию...</b> <code> [ 24% ]</code>")
        await sleep(1)

        await utils.answer(message, "🌀 <b>Ysкоряю процᴇss</b> <code> [ 37% ]</code>")
        await sleep(1)

        await utils.answer(message, "🌀 <b>Ysкоряю процᴇss</b> <code> [ 53% ]</code>")
        await sleep(1)

        await utils.answer(message, "🌀 <b>Ysкоряю процᴇss</b> <code> [ 78% ]</code>")
        await sleep(1)

        await utils.answer(message, "✅ <b>Инф0рмᴀция нᴀйдᴇʜᴀ</b> <code> [ 94% ]</code>")
        await sleep(0.6)

        await utils.answer(message, "🔁 <b>вblв0жу...</b> <code> [ 100% ]</code>")
        await sleep(1)

        possible_numbers = [
            10000000000, 99999999999, 666666666, 282823483, 8889238883466, 3838339333, 833828483, 819283748, 3829444678, 79236932583, 79230352252, 79236785664
        ]

        random_number = random.choice(possible_numbers)

        countries = ["Пидоров", "Россия", "США", "Уёбищ", "Хохлятия", "Чуркостан", "Хуегрызов", "Позорстан", "Подкидышей", "Путина", "Хохлов", "Хуестан", "Мегадиперсупербольшойчленсосаламоямамкастан"]
        regions = ["Нигерская область", "Москва", "Калифорния", "Подвальная область", "Канализация", "Хуесосов", "Фанатов моего хуя", "Конченых пидоров", "Мамкиных подсосов", "Детей Дурова"]
        operators = ["Телепузик", "Мегафон", "Билайн", "Далбаёб", "Еблан", "Пидорас", "Бездарь", "Подкидыш", "Зародыш", "Неадерталец", "Натурал", "Фанат хуя Дурова", "Конченая мразь", "Мама", "Павел Дуров"]
        names = ["Пидор", "моя мать шлюха", "умер от СПИДа", "Шлюха", "Хуесос", "Далбаёб", "Конченый", "Идиот", "клаьал", "Дуров Павел", "Путин Владимир Владимирович", "Александр Хуесосов Безмамышь", "Спермоглотатель 9000"]
        addresses = ["Россия, Санкт-Петербург", "Украина, Подвал", "Подвал, Член негра", "Мамина Пизда", "Залуповка", "Хуесоскино", "Церковь имени Моего Члена", "Канава Зелеского", "Город Омск, улица Куйбышева 77, Третий этаж 105 квартира", "Ничего больше не придумала"]
        birth_dates = ["14.01.2005 (19 лет)", "16.06.6666 (ченахуй)", "14.08.8 (пасхалко)", "сегодня", "ещё не родился", "помер 3 года назад", "никогда не рождался", "05.05.05 (20 лет)", "00.00.-8456 (10 000+ лет)", "34 год до н.э", "01.01.1488 (хз)", "777.07.17 (7 лет)"]
        viewers_counts = [0, 1000, 5000, 837, 364, 63, 7, 8, 37, 928, 1488, 666, 999, 333, 999999999, 78942267, 7777777, 666666, 333, 22, 1, 4444, 55555, 88888888, 1000000000000, 53793467, 345, 234, 223, 2023, 69, 52, 1, 57899753]
        reputations_positive = [0, 10, 383, 47, 3633, 99993, 77383, 100, 200, 837, 364, 63, 7, 8, 37, 928, 1488]
        reputations_negative = [100, 383, 395, 849, 48593, 999999999999, 200, 300, 3357, 4572, 344, 468, 678, 789, 3345, 34672]
        social_marks = ["🙄 Ноунейм (0)", "🤔 Известный (1)", "🌐 Проверенный! (2)", "🛡️ Деффер (3)", "📛 Скамер (4)", "🐷 Хохол (5)", "💎 𝐕𝐈𝐏 (6)", "🇷🇺 Бог (7)", "😎 Уважаемый (8)", "💩 Безмамышь (9)", "🔰 Сильнейший (10)", "💻 Программист (11)", "🤫🧏 Сигма (12)", "🤰 Шлюха (13)", "💸 Бизнесмен (14)", "🐒 Квадробобер (Квадробер) (15)"]
        comments_counts = [100, 500, 729, 374, 203, 748, 28, 0, 73, 9542, 9999999999999999, 4578, 335, 356, 478, 789, 753, 3457]

        random_birth_date = random.choice(birth_dates)
        viewers_count = random.choice(viewers_counts)
        reputation = f"({random.choice(reputations_positive)})👍 ({random.choice(reputations_negative)})👎"
        social_mark = random.choice(social_marks)
        comments_count = random.choice(comments_counts)

        result_message = [
            (f"📱<b>├ Номер:</b> <code>{random_number}</code>", ""),
            (f"<b>├ Страна:</b> <code>{random.choice(countries)}</code>", ""),
            (f"<b>├ Регион:</b> <code>{random.choice(regions)}</code>", ""),
            (f"<b>└ Оператор:</b> <i>{random.choice(operators)}</i>\n", ""),
            (f"📓 <b>Возможные имена:\n└</b>  <i>{random.choice(names)}</i>\n", ""),
            (f"🏠 <b>Возможные адреса:</b> \n<i>{random.choice(addresses)}</i>\n", ""),
            (f"🏥 <b>Дата рождения:</b> <code>{random_birth_date}</code>\n", ""),
            (f"👁 <b>Интересовались:</b> <code>{viewers_count}</code> человек", ""),
            (f"🏅 <b>Репутация:</b> <i>{reputation}</i>", ""),
            (f"💬 <b>Социальная метка:</b> <code>{social_mark}</code>", ""),
            (f"💬 <b>Комментариев:</b> <code>{comments_count}</code>", "")
        ]

        start_text = ""

        for info, section in result_message:
            if section:
                start_text += f"<b>{section}</b>\n"

            start_text += info + "\n"

            await message.edit(start_text)
            await sleep(0.5)
