import telebot



bot = telebot.TeleBot('YOUR BOT TOKEN')

ls = YOUR TOKEN ADM
chat_id = YOUR CHATID
consolee = YOUR CHATID CONSOLE
console = YOUR CHATID CONSOLE
test = IDK
tanya = IDK
chat_shop = YOUR CHATID CHATSHOP CONSOLE
chat_game = YOUR CHATID CHATGAME


pers1 = "фурину" # Вставляете актуальных персонажей для круток
pers2 = "байджу"
persh = 'блейда'
persh2 = 'none'




standart = ['Мона', 'Дилюк', 'Дилюк', 'Дэхья', 'Кэ цин', 'Цици', 'Тигнари', "Джинн", 'Тигнари',
                               'небесное крыло', 'Дэхья', "Джинн", 'Меч сокола', 'Кэ цин', 'небесный меч',
                               'Волчья погибель', 'Небесное величие', 'Мона', 'нефритовый коршун', 'Цици', 'небесная ось',
                               'Цици', 'Молитва святым ветрам'
                        , 'небесный атлас', 'лук амоса']

fourpers = ['барбара', 'беннет', 'бэйдоу', 'горо', 'диона', 'дори', 'кавех', 'кандакия', 'кирара', 'коллеи', 'кэйа', 'лайла', 'лиза', 'сара', 'сахароза', 'саю', 'синцю', 'синобу', 'синьянь', 'сянлин', 'тома', 'фарузан','фишль', 'хэйдзо', 'чунюнь', 'эмбер', 'мика', 'юньцзинь', 'нин гуан', 'ноэлль', 'яньфэй', 'яояо', 'розария', 'рэйзор', 'фремине', 'линетт']


fiveweap = ['Аква симулякрум','Первый великий фокус', 'Великолепие лазурного свода', 'Вечное лунное сияние', 'Волчья погибель', 'Воспоминания Тулайтуллы', 'Громовой пульс', 'Драгоценный омут', 'Истина кагура', 'Ключ Хадж-нисут', 'Клятва свободы', 'Краснорогий камнеруб', 'Кромсатель пиков', 'Лук Амоса', 'Маяк тростникового моря', 'Меч Сокола', 'Молитва святым ветрам', 'Небесная ось', 'Небесное величие', 'Небесное крыло', 'Небесный атлас', 'Небесный меч', 'Некованый', 'Нефритовый коршун', 'Охотничья тропа', 'Память о пыли', 'Первый великий фокус', 'Песнь разбитых сосен', 'Покоритель вихря', 'Полярная звезда', 'Посох алых песков', 'Посох Хомы', 'Рассекающий туман', 'Свет лиственного разреза', 'Сияющая жатва', 'Сновидения тысячи ночей', 'Усмиритель бед', 'Харан гэппаку фуцу', 'Элегия погибели']
fourweap = ['Вспышка во тьме', 'Меч Фавония', 'Драконий рык', 'Хамаюми', 'Черногорская бритва', 'Черногорский длинный меч', 'Грандиозный финал глубин', 'Кодекс Фавония', 'Каменное копьё', 'Гроза драконов', 'Плод восполнения', 'Улов', 'Королевский гримуар', 'Деревянный клинок', 'Легендарный клинок Иссин (пробуждённый)', 'Дождерез', 'Королевское копьё', 'Бесструнный', 'Стальное жало', 'Благодатный владыка вод', 'Морской атлас', 'Белая тень', 'Меч-флейта', 'Истории Додоко', 'Церемониальный двуручный меч', 'Говорящая палица', 'Зелёный лук', 'Иссушитель', 'Черногорский боевой лук', 'Гаснущие сумерки', 'Око клятвы', 'Приближённый короля', 'Солнечная жемчужина', 'Перевозчик Флёв Сандр', 'Церемониальные мемуары', 'Лунное сияние ксифоса', 'Вальс Нирваны Ночи', 'Крест-копьё Китаин', 'Черногорская пика', 'Копьё Драконьего хребта', 'Сверкание чистых вод', 'Мелодия покоя', 'Составной лук', 'Скитающаяся звезда', 'Баллада фьордов', 'Токабо сигурэ', 'Луна Моун', 'Королевский двуручный меч', 'Киноварное веретено', 'Легендарный клинок Иссин (сломанный)', 'Охотник во тьме', 'Церемониальный меч', 'Око сознания', 'Кагоцурубэ Иссин', 'Режущий волны плавник', 'Королевский лук', 'Пика полумесяца', 'Меч нисхождения', 'Ржавый лук', 'Черногорский агат', 'Церемониальный лук', 'Кольцо Хакусин', 'Осквернённое желание', 'Меч аристократов', 'Прототип: Звёздный блеск', 'Песнь странника', 'Хищник', 'Каменный меч', 'Двуручный меч Фавония', 'Плод вечной мерзлоты', 'Кацурагикири Нагамаса', 'Смертельный бой', 'Чёрный меч', 'Меч драконьей кости', 'Прототип: Янтарь', 'Цветок в латах', 'Копьё Фавония', 'Ода анемонии', 'Прототип: Злоба', 'Аквамарин Махайры', 'Боевой лук Фавония', 'Пронзающий луну', 'Вино и песни', 'Жертвенный нефрит', 'Справедливая награда', 'Заснеженное звёздное серебро', 'Наследник слепящего солнца', 'Прототип: Архаичный', 'Акуомару', 'Клюв ибиса', 'Регалия леса', 'Амэнома Кагэути', 'Волчий клык', 'Тень волны', 'Копьё послания ветров', 'Прототип: Полумесяц', 'Меч-колокол']


