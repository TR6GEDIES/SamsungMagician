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
# Name: HerokuSupport
# Author: https://t.me/SamsungMagician
# ---------------------------------------------------------------------------------

__version__ = (1, 0, 3)

# Name: HerokuSupport
# meta developer: @SamsungMagician (idea by @hikka_dmod)

from .. import loader, utils
from asyncio import sleep
import logging

logger = logging.getLogger(__name__)

@loader.tds
class HerokuSupport(loader.Module):
    """Заметки из саппорта хероку"""
    strings = {'name': 'HerokuSupport',
               "channel": "Поддержи разработчика 💫",
               "welcome": (
                   "🖐 <i>Приветствую, ты запустил установку модуля <b>«HerokuSupport»</b></i>"
                   "\n\n🤍 <i>Благодарю за установку</i>"
                   "\n\n⚙️ <i>Создан by <code>@SamsungMagician</code></i>"),
               }


    async def on_dlmod(self):
        await self.inline.bot.send_photo(
            self._client._self_id,
            "https://pomf2.lain.la/f/ro1zbpz.jpg",
            caption=self.strings("welcome"),
        )


    async def client_ready(self, client, db) -> None:
        self.db = db
        self.client = client

        logger.info("Модуль HerokuSupport успешно загружен!")

        await self.request_join(
            "@SamsungMagicianModules",
            self.strings['channel'],
        )


    @loader.command(alias="гдемодули")
    async def wheremodule(self, message):
        """[гдемодули] - Показать каталог каналов с модулями"""
        await message.edit("🌘")
        await sleep(.2)
        await message.edit("🌘 <b>Heroku</b>")
        await sleep(.2)
        await message.edit("🌘 <b>HerokuModules</b>")
        await sleep(.2)
        await message.edit("""
<emoji document_id=5983093054842606366>💠</emoji> <b>Официальные каналы с модулями:</b>

<emoji document_id=5996651729725166075>🖤</emoji> <a href="https://t.me/hikarimods">Hikka ㉿ Modules</a> <a href="https://t.me/hikariatama">(Владелец)</a>
<emoji document_id=5357138701442884456>💎</emoji> <a href="https://t.me/morisummermods">morisummer.mods</a> <a href="https://t.me/morisummer">(владелец)</a>
<emoji document_id=5798665810532634979>☢️</emoji> <a href="https://t.me/cakestwix_mods">cakestwix mods</a> (владелец) <i>[???]</i>
<emoji document_id=5352988457364888590>🦋</emoji> <a href="https://t.me/nalinormods">Nalinor FTG modules</a> <a href="https://t.me/nalinor">(владелец)</a> 
<emoji document_id=5282857272123341907>🥺</emoji> <a href="https://t.me/AstroModules">𝘼𝙨𝙩𝙧𝙤 𝙈𝙤𝙙𝙪𝙡𝙚𝙨</a> <a href="https://t.me/den4iksuperostryyper4ik">(владелец)</a> 
<emoji document_id=5427350279882285811>🙂</emoji> <a href="https://t.me/vsecoder_m">@vsecoder modules</a> <a href="https://t.me/vsecoder">(владелец)</a> 
<emoji document_id=5854847315658936343>👻</emoji> <a href="https://t.me/mm_mods">MM-Mods</a> <a href="https://t.me/sonnestinkt">(владелец)</a>
<emoji document_id=5425082717538625159>🐱</emoji> <a href="https://t.me/apodiktum_modules">[Apodiktum] Modules</a> <a href="https://t.me/anon97945">(владелец)</a>
<emoji document_id=5469957648243760108>😛</emoji> <a href="https://t.me/shadow_modules">sh. modules</a> <a href="https://t.me/dev_ssh">(владелец)</a>
<emoji document_id=5377752800706963596>🏳️</emoji> <a href="https://t.me/wilsonmods">𓆩✧𓆪 • All-in-One: Commits</a> (владелец) <i>[???]</i>
<emoji document_id=5785127566809501260>🔴</emoji> <a href="https://t.me/amoremods">Amoremods -> Hikamorumods</a> (владелец) <i>[???]</i>
<emoji document_id=5764913852986692329>🌙</emoji> <a href="https://t.me/DorotoroMods">DorotoroMods</a> (владелец)<i> [???]</i>
<emoji document_id=5819027790921470358>❤️‍🔥</emoji> <a href="https://t.me/HikkaFTGmods">hikka龴ftg-modules</a> <a href="https://t.me/lotosiiiik">(владелец)</a>
<emoji document_id=5384182615857178765>🙂</emoji> <a href="https://t.me/nercymods">nerc mods</a> <a href="https://t.me/n3rcy">(владелец)</a>
<emoji document_id=5785393210536759261>🐱</emoji> <a href="https://t.me/hikka_mods">H:Mods</a> (владелец) <i>[???]</i>
<emoji document_id=5452130639157407569>❤️</emoji> <a href="https://t.me/sqlmerr_m">sqlmerr modules</a> <a href="https://t.me/sqlmerr">(владелец)</a>

<emoji document_id=5897920748101571572>🌟</emoji> <b>Неофициальные каналы с модулями:</b>

<emoji document_id=5341805221519565699>🏳️</emoji> <a href="https://t.me/userbotik">Юзер Ботик</a> (владелец) <i>[???]</i>
<emoji document_id=6037400386564787839>🩸</emoji> <a href="https://t.me/kshmods">KSH:MODS</a> (владелец) <i>[???]</i>
<emoji document_id=5319061797729216610>😈</emoji> <a href="https://t.me/BruhHikkaModules">BHikkaMods (main)</a> <a href="https://t.me/MuRuLOSE">(владелец)</a>
<emoji document_id=5316555418024030560>😈</emoji> <a href="https://t.me/module_free2">userbot modules | collection of modules 2.0 | troll module |</a> (владелец) <i>[???]</i>
<emoji document_id=5316792530283538053>👁‍🗨</emoji> <a href="https://t.me/HikkTutor">Юзер Бот</a> (владелец) <i>[???]</i>
<emoji document_id=5316950202827942245>💀</emoji> <a href="https://t.me/RUIS_VlP">RUIS MODS</a> (владелец) <i>[???]</i>
<emoji document_id=5316644422631304409>🐺</emoji> <a href="https://t.me/eremod">Ere Modules</a> <a href="https://t.me/EPEMEN">(владелец)</a>
<emoji document_id=5339573638116946172>💀</emoji> <a href="https://t.me/aki_modules">Aki Modules | Shitty Hikka Modules</a> (владелец) <i>[???]</i>
<emoji document_id=5339154505143430802>😈</emoji> <a href="https://t.me/SemenMeens">ℋℯ𝓇ℴ𝓀𝓊 𝒶𝓃𝒹 ℋ𝒾𝓀𝓀𝒶 𝓂ℴ𝒹𝓊𝓁ℯ</a> (владелец) <i>[???]</i>
<emoji document_id=5355080475805228911>😈</emoji> <a href="https://t.me/xensidemod">Modules By XenSide</a> (владелец) <i>[???]</i>
<emoji document_id=5447425034333210344>🖤</emoji> <a href="https://t.me/SomeScripts">Какие-то скрипты</a> (владелец) <i>[???]</i>
<emoji document_id=5449398928288006064>☠️</emoji> <a href="https://t.me/unneyon_hmods">@unneyon: hikka mods</a> (владелец) <i>[???]</i>
<emoji document_id=5451829394446237662>🐇</emoji> <a href="https://t.me/codrago_m">C:Mods</a> <a href="https://t.me/codrago">(владелец)</a>
<emoji document_id=5454059109538087325>🌟</emoji> <a href="https://t.me/FAmods">FAmods</a> <a href="https://t.me/vecax">(владелец)</a>
<emoji document_id=5395716153530140157>😵</emoji> <a href="https://t.me/wmodules">Werpyock modules</a> (владелец) <i>[???]</i>
<emoji document_id=5188212415010982800>🤩</emoji> <a href="https://t.me/AmekaMods">Ameka Mods | AmeMods</a> (владелец) <i>[???]</i>
<emoji document_id=5215420315571605459>🤩</emoji> <a href="https://t.me/yg_modules">yg | modules</a> (владелец) <i>[???]</i>
<emoji document_id=5226462234107987549>🤩</emoji> <a href="https://t.me/FModules">F:Modules</a> <a href="https://t.me/Fixyres">(владелец)</a>""")

    @loader.command(alias="почемубан")
    async def whyban(self, message):
        """[почемубан] - Показать возможные причины блокировки аккаунта"""
        await message.edit("🌘")
        await sleep(.2)
        await message.edit("🌘 <b>Heroku</b>")
        await sleep(.2)
        await message.edit("🌘 <b>Heroku WhyBanned?</b>")
        await sleep(.2)
        await message.edit("""
<emoji document_id=5436113877181941026>❓</emoji> <b>За что могут удалить аккаунт?</b>

<emoji document_id=5282843764451195532>🖥</emoji> <b>Использование модулей, которые делают много запросов к API. Пример: spam, autoreact, autoprofile, ghoul, lovemagic, magictext, trashguy и другие.</b> <em>Это могут быть как модули на измену профиля, изменение иди отправку сообщений в большом количестве, авточиталка, которая читает все ваши чаты и многие-многие другие. Решение: .api_fw_protection - включить лимитер запросов. Могут быть ложные срабатывания.</em>

<emoji document_id=5395444514028529554>🫦</emoji> <b>Малый возраст аккаунта.</b> <em>Рекомендуемый — не менее полугода, но с премиумом рекомендуемый не менее двух-трех недель.</em>

<emoji document_id=5447410659077661506>🌐</emoji> <b>Страна аккаунта.</b> <em>Страны на -стан (Узбеки*стан*, Туркмени*стан* и т.д) больше подвержены блокировкам, чем остальные.</em>

<emoji document_id=5246762912428603768>📉</emoji> <b>Малый прогрев аккаунта.</b> <em>Если ты в Телеграме общаешься с 1-2 людьми = редко, вероятность бана возрастает. Если ты постоянно проявляешь живую активность и состоишь во множестве чатов - она снижается.</em>

<emoji document_id=5449875686837726134>👎</emoji> <b>Скам-модули.</b> <em>Несмотря на наличие базовой защиты от удаления аккаунта в Hikka, это все равно возможно. Скачивайте модули только из официальных источников.
Но если вы скачали скам модуль и вам еще не снесли аккаунт вы можете выгрузить модуль и перезагрузить хикку, так вероятность удаления аккаунта становится намного ниже.</em>

<emoji document_id=5452069934089641166>❓</emoji> <b>Дефолтные креды.</b> <em>Если вы не знаете что это и следуете инструкции, можете пропустить этот пункт. Не используйте дефолтные ключи. Они дают бо‌льшие флудвейты и вероятность бана. Это касается к примеру API конфига от тг, его используют много людей и он часто подвергается флудвейтам и банам.</em>

<emoji document_id=5274099962655816924>❗️</emoji> <em>Но даже выполняя все пункты выше вы все еще имеете вероятность бана аккаунта, если у вас есть возможность и деньги купите себе телеграм премиум, он помогает от большинства флудвейтов телеграма.</em>

<emoji document_id=5332533929020761310>✅</emoji> Взято из <a href="https://t.me/heroku_talks">тык</a>""")


    @loader.command(alias="какюзерлэнд")
    async def howuserland(self, message):
        """[какюзерлэнд] - Показать инструкцию по установке Heroku на UserLAnd"""
        await message.edit("🌘")
        await sleep(.2)
        await message.edit("🌘 <b>Heroku</b>")
        await sleep(.2)
        await message.edit("🌘 <b>Heroku install</b>")
        await sleep(.2)
        await message.edit("🌘 <b>Heroku install UserLAnd</b>")
        await sleep(.2)
        await message.edit("""
<emoji document_id=5436113877181941026>❓</emoji> <b>Как установить Heroku на <em>UserLAnd?</em></b>
        
<emoji document_id=5348324054161967894>1️⃣</emoji> <b>Установи <em>UserLAnd</em> по <a href="https://play.google.com/store/apps/details?id=tech.ula">ссылке</a></b>

<emoji document_id=5350559846632537457>2️⃣</emoji> <b>Открой его, выбери <em>Ubuntu</em> —> <em>Minimal</em> —> <em>Terminal</em></b>

<emoji document_id=5350719542106540014>3️⃣</emoji> <b>Жди установки дистрибутива, можешь налить чаю.</b>

<emoji document_id=5350505304842846481>4️⃣</emoji> <b>После успешной установки перед тобой откроется терминал, пиши туда:</b>

<pre language="bash">sudo apt update && sudo apt upgrade -y && sudo apt install python3 git python3-pip -y && git clone https://github.com/coddrago/Heroku && cd Heroku && sudo pip install -r requirements.txt && python3 -m hikka</pre>

<emoji document_id=5348566874433011485>5️⃣</emoji> <b>В конце установки появится <em>ссылка</em>, переходи по ней и <em>вводи данные</em> своего аккаунта для входа.</b>

<emoji document_id=5332533929020761310>✅</emoji> Взято из <a href="https://t.me/heroku_talks">тык</a>""")


    @loader.command(alias="каквсл")
    async def howwsl(self, message):
        """[каквсл] - Показать инструкцию по установке Heroku на WSL"""
        await message.edit("🌘")
        await sleep(.2)
        await message.edit("🌘 <b>Heroku</b>")
        await sleep(.2)
        await message.edit("🌘 <b>Heroku install</b>")
        await sleep(.2)
        await message.edit("🌘 <b>Heroku install WSL</b>")
        await sleep(.2)
        await message.edit("""
<emoji document_id=5436113877181941026>❓</emoji> <b>Как установить Heroku на <em>WSL?</em></b>

<emoji document_id=5348324054161967894>1️⃣</emoji> <b>Скачай <em>WSL</em>.</b>

Для этого открой PowerShell с правами администратора и напиши <code>wsl --install -d Ubuntu-22.04</code>

⚠️ <em>Для установки WSL необходима Windows 10 build 2004 или Windows 11 любой версии и ПК с поддержкой виртуализации. Для установки на более ранние версии ОС обратись к</em> <a href="https://learn.microsoft.com/ru-ru/windows/wsl/install-manual">этой странице</a>

<emoji document_id=5350559846632537457>2️⃣</emoji> <b>Перезагрузи ПК и запусти приложение <em>Ubuntu 22.04.x</em></b>

<emoji document_id=5350719542106540014>3️⃣</emoji> <b>Вставь в него команду (ПКМ):</b>

<code>curl -Ss https://bootstrap.pypa.io/get-pip.py | python3</code>

⚠️ <em>При появлении желтых предупреждений введи</em> <code>export PATH="/home/username/.local/bin:$PATH"</code> <em>заменив /home/username/.local/bin на тот путь, о котором говорится в сообщении</em>

<emoji document_id=5350505304842846481>4️⃣</emoji> <b>Вставь команду (ПКМ):</b>

<code>clear && git clone https://github.com/coddrago/Heroku && cd Heroku && pip install -r requirements.txt && python3 -m hikka</code>

<emoji document_id=5332533929020761310>✅</emoji> Взято из <a href="https://t.me/heroku_talks">тык</a>""")


    @loader.command(alias="какхиккахост")
    async def howhikkahost(self, message):
        """[какхиккахост] - Показать инструкцию по установке Heroku на HikkaHost_bot"""
        await message.edit("🌘")
        await sleep(.2)
        await message.edit("🌘 <b>Heroku</b>")
        await sleep(.2)
        await message.edit("🌘 <b>Heroku install</b>")
        await sleep(.2)
        await message.edit("🌘 <b>Heroku install HikkaHost</b>")
        await sleep(.2)
        await message.edit("""
<emoji document_id=5436113877181941026>❓</emoji> <b>Как установить Heroku на <em>HikkaHost?</em></b>

<emoji document_id=5348324054161967894>1️⃣</emoji> <b>Перейдите на <em>@hikkahost_bot</em>.</b>

<emoji document_id=5350559846632537457>2️⃣</emoji> <b>Выберите <em>«Установить»</em>.</b>

<emoji document_id=5350719542106540014>3️⃣</emoji> <b>Выберите <em>«🪐 Heroku»</em>.</b>

<emoji document_id=5350505304842846481>4️⃣</emoji> <b>И продолжайте установку.</b>

<emoji document_id=5348566874433011485>5️⃣</emoji> <b>После этого вы получите ссылку, откройте ее и войдите в свой аккаунт.</b>

<emoji document_id=5332533929020761310>✅</emoji> Взято из <a href="https://t.me/heroku_talks">тык</a>""")


    @loader.command(alias="каклавхост")
    async def howlavhost(self, message):
        """[каклавхост] - Показать инструкцию по установке Heroku на LavHostBot"""
        await message.edit("🌘")
        await sleep(.2)
        await message.edit("🌘 <b>Heroku</b>")
        await sleep(.2)
        await message.edit("🌘 <b>Heroku install</b>")
        await sleep(.2)
        await message.edit("🌘 <b>Heroku install LavHost</b>")
        await sleep(.2)
        await message.edit("""
<emoji document_id=5436113877181941026>❓</emoji> <b>Как установить Heroku на <em>LavHost?</em></b>

<emoji document_id=5348324054161967894>1️⃣</emoji> <b>Перейдите на <em>@lavhostbot</em>.</b>

<emoji document_id=5350559846632537457>2️⃣</emoji> <b>Введите команду /buy, выберите и оплатите счет.</b>

<emoji document_id=5350719542106540014>3️⃣</emoji> <b>При необходимости отправьте квитанцию об оплате.</b>

<emoji document_id=5350505304842846481>4️⃣</emoji> <b>После подтверждения оплаты введите /install и выберите Heroku.</b>

<emoji document_id=5348566874433011485>5️⃣</emoji> <b>Следуйте инструкциям бота.</b>

<emoji document_id=5332533929020761310>✅</emoji> Взято из <a href="https://t.me/heroku_talks">тык</a>""")


    @loader.command(alias="ффмпег")
    async def ffmpeg(self, message):
        """[ффмпег] - Показать инструкцию по установке FFMPEG на Heroku"""
        await message.edit("🌘")
        await sleep(.2)
        await message.edit("🌘 <b>Heroku</b>")
        await sleep(.2)
        await message.edit("🌘 <b>Heroku install</b>")
        await sleep(.2)
        await message.edit("🌘 <b>Heroku install FFMPEG</b>")
        await sleep(.2)
        await message.edit("""
<emoji document_id=5436113877181941026>❓</emoji> <b>Как установить FFMPEG на <em>Heroku?</em></b>

<emoji document_id=5348324054161967894>1️⃣</emoji> <b>Установка на <em>Railway</em>:</b>

<pre language="bash">.terminal apt update && apt install ffmpeg libavcodec-dev libavutil-dev libavformat-dev libswscale-dev libavdevice-dev -y</pre>

<emoji document_id=5350559846632537457>2️⃣</emoji> <b>Установка на <em>Custom Server</em>:</b>

<pre language="bash">.terminal sudo apt update && sudo apt install ffmpeg libavcodec-dev libavutil-dev libavformat-dev libswscale-dev libavdevice-dev -y</pre>

<emoji document_id=5350719542106540014>3️⃣</emoji> <b>Установка на <em>Termux</em>:</b>

<pre language="bash">.terminal pkg install ffmpeg -y</pre>

<emoji document_id=5350505304842846481>4️⃣</emoji> <b>И после прописываем</b> <code>.restart -f</code>

<emoji document_id=5332533929020761310>✅</emoji> Взято из <a href="https://t.me/hikka_talks">тык</a>""")


    @loader.command(alias="решение")
    async def solution(self, message):
        """[решение] - Показать гайд по решению любых ошибок!"""
        await message.edit("🌘")
        await sleep(.2)
        await message.edit("🌘 <b>Heroku</b>")
        await sleep(.2)
        await message.edit("🌘 <b>Heroku guide</b>")
        await sleep(.2)
        await message.edit("""
<emoji document_id=5370964879773539088>😯</emoji> <b> Лучший гайд по решению любых ошибок!</em></b>

<tg-spoiler>http://www.translate.ru/
https://translate.google.com/?hl=ru
https://translate.yandex.ru/
http://www.reverso.net/text_translation.aspx?lang=RU
https://translator.microsoft.com/
http://www.systranet.com/translate</tg-spoiler>

<emoji document_id=5332533929020761310>✅</emoji> Взято из <a href="https://t.me/hikka_talks">тык</a>""")
