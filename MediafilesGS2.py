__version__ = (1, 0, 2)

# Name: MediafilesGS2
# meta developer: @SamsungMagician (main developer @mqone)

from .. import loader
import asyncio

@loader.tds
class MediafilesGS2(loader.Module):
    """Отправляет гс с канала https://t.me/MediafilesForModule"""

    strings = {"name": "MediafilesGS2"}

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
