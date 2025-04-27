__version__ = (1, 0, 0)

# Name: MediafilesCircles
# meta developer: @SamsungMagician (main developer @mqone)

from .. import loader
import asyncio

@loader.tds
class MediafilesCircles(loader.Module):
    """Отправляет кружки с канала https://t.me/MediafilesForModule"""

    strings = {"name": "MediafilesCircles"}

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
            "https://t.me/MediafilesForModule/79",
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

