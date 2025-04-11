__version__ = (1, 0, 1)

# Name: MediafilesGS1
# meta developer: @SamsungMagician (main developer @mqone)

from .. import loader
import asyncio

@loader.tds
class MediafilesGS1(loader.Module):
    """Отправляет гс с канала https://t.me/MediafilesForModule"""

    strings = {"name": "MediafilesGS1"}

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
