__version__ = (1, 0, 0)

# Name: FakeDoxing
# meta developer: @SamsungMagician (main developer @mqone)

from .. import loader, utils
from asyncio import sleep
import random

@loader.tds
class UpgradeDoxing(loader.Module):
    """Фейк докс модуль"""

    strings = {'name': 'UpgradeDoxing'}

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
