import sys
from sekiro_game_vers2_inside import *
ylife = 5
hcons = 1
just_f = Just_Fight("Секиро", "a", "s", "w", "d", ylife, hcons)
just_f2 = Just_Fight1("Секиро", "a", "s", "w", "d", ylife, hcons)
just_f3 = Just_Fight2("Секиро", "a", "s", "w", "d", ylife, hcons)
secret_f = Secret_Fight("Секиро", "a", "s", "w", "d", ylife, hcons)
boss_f = Boss_fight("Секиро", "a", "s", "w", "d", ylife, hcons)
train = Training("Секиро", "a", "s", "w", "d", ylife, hcons)
op = 0
plus_op = 20
print("Ты оказался в колодце, у тебя головная боль, ты нечего не помнишь")
print("Ты нашел яблоко")
if input("1.Сьесть; 2.Оставить: ") == "1":
    print("Ты сьел яблоко")
else:
    print("Ты не голодный")
print("К тебе подошел какойто мужик средних лет")
print("- Ты кто?")
print("Ты ответил что ты не знаешь")
print("- Странно, что ты нечего на помнишь, наверное ты слишком долго был без сознания")
print("Он попросил пойти к нему домой")
if input("1.Согласится; 2.Отказатся: ") == "1":
    print("Ты согласился")
else:
    print("Ты никак не хотел к ниму идти, но он говорил так убеждающе, что ты все таки согласился")
print("Внезапно ты снова потерял сознание")
print("Ты очнулся у него дома")
print("- Рад что ты очнулся")
if input("1.Узнать что тут происходит; 2.Нечего не говорить: ") == "1":
    print("- Ты попал в мир Елдер, в самый розгар войны, где повстанцы захвачивают все больше и больше земель. И еще они забрали господина Акина в плен")
    print("Ты сказал что этот человек тебе знаком, причем очень сильно")
    print("- Хммммм. Перед тем как его забрали в плен, он сказал что потерял своего синоби, точнее тот потерял сознание. Наверное ты и есть тот синоби")
    print("Ты согласился")
print("- С этого момента я буду называть тебя Секиро")
if input("1.Тренироватся; 2.Не тренироватся: ") == "1":
    train.training()
print("- Наш мир интересен, согласен?")
if input("1.Согласен; 2.Нет: ") == "2":
    print("Твое дело")
print("Ты снова потерял сознание")
print("Ты проснулся в какомто селе")
print("Ты увидел записку")
print('''"Рад что ты проснулся, Секиро. Я отнес тебя прямо в село, но дальше не смог. Тебе надо пройти через это село, лес, и потом ты встретишь замок. Там твой господин. И еще, возле тебя лежит катана. Удачи"''')
print("Ты осмотрел територию, и увидел за селом лес")
print("Ты пошел в путь")
print("Но тебя встретил воен")
print("Видно, он не настроен дружелюбно!")
just_f.fight()
op += plus_op
print(f"Твой опыт: {op}")
just_f = Just_Fight("Секиро", "a", "s", "w", "d", ylife, hcons)
secret_f = Secret_Fight("Секиро", "a", "s", "w", "d", ylife, hcons)
boss_f = Boss_fight("Секиро", "a", "s", "w", "d", ylife, hcons)
print("Ты прошел дальше")
print("Еще один противник")
just_f.fight()
op += plus_op
print(f"Твой опыт: {op}")
just_f = Just_Fight("Секиро", "a", "s", "w", "d", ylife, hcons)
secret_f = Secret_Fight("Секиро", "a", "s", "w", "d", ylife, hcons)
boss_f = Boss_fight("Секиро", "a", "s", "w", "d", ylife, hcons)
print("Ты подошел к дому, где разговаривали 2 человека")
if input("1.Подслушать; 2.Пройти мимо: ") == "1":
    print("- Говорят, у нас завелся синоби")
    print("- Чепуха")
    print("- Он убил уже двоих")
    print("- Это не возможно!!!")
    print("- Факт есть факт")
    print("- Тогда усилить, оборону! Нельзя чтобы он пробрался к Акина!")
print("Ты прошел дальше")
print("Опять очередной противник")
just_f.fight()
op += plus_op
print(f"Твой опыт: {op}")
just_f = Just_Fight("Секиро", "a", "s", "w", "d", ylife, hcons)
secret_f = Secret_Fight("Секиро", "a", "s", "w", "d", ylife, hcons)
boss_f = Boss_fight("Секиро", "a", "s", "w", "d", ylife, hcons)
print("- Не желаете поколдовать?")
if input("1.Поговорить; 2.Проигнорировать: ") == "1":
    print(f"Твой опыт: {op}")
    print("- Могу продать жизненную силу, но конечно не бесплатно!")
    if input("1.Купить жизненную силу(60 опыта); 2.Нечего не покупать: ") == "1":
        if op < 60:
            print("Недостаточно опыта!")
        else:
            op -= 60
            print(f"Твой опыт: {op}")
            print("Ты купил жизненную теперь у тебя + 3 здоровья")
            ylife += 3
            just_f = Just_Fight("Секиро", "a", "s", "w", "d", ylife, hcons)
            just_f1 = Just_Fight1("Секиро", "a", "s", "w", "d", ylife, hcons)
            just_f2 = Just_Fight2("Секиро", "a", "s", "w", "d", ylife, hcons)
            secret_f = Secret_Fight("Секиро", "a", "s", "w", "d", ylife, hcons)
            boss_f = Boss_fight("Секиро", "a", "s", "w", "d", ylife, hcons)

print("Ты пошел дальше")
print("Опять очередной противник")
just_f.fight()
op += plus_op
print(f"Твой опыт: {op}")
just_f = Just_Fight("Секиро", "a", "s", "w", "d", ylife, hcons)
secret_f = Secret_Fight("Секиро", "a", "s", "w", "d", ylife, hcons)
boss_f = Boss_fight("Секиро", "a", "s", "w", "d", ylife, hcons)
print("Ты пошел дальше")
print("Ты заметил много врагов")
if input("1.Идти напролом; 2.Обойти: ") == "1":
    just_f.fight()
    op += plus_op
    print(f"Твой опыт: {op}")
    just_f = Just_Fight("Секиро", "a", "s", "w", "d", ylife, hcons)
    secret_f = Secret_Fight("Секиро", "a", "s", "w", "d", ylife, hcons)
    boss_f = Boss_fight("Секиро", "a", "s", "w", "d", ylife, hcons)
    just_f.fight()
    op += plus_op
    print(f"Твой опыт: {op}")
    just_f = Just_Fight("Секиро", "a", "s", "w", "d", ylife, hcons)
    secret_f = Secret_Fight("Секиро", "a", "s", "w", "d", ylife, hcons)
    boss_f = Boss_fight("Секиро", "a", "s", "w", "d", ylife, hcons)
    just_f.fight()
    op += plus_op
    print(f"Твой опыт: {op}")
    just_f = Just_Fight("Секиро", "a", "s", "w", "d", ylife, hcons)
    secret_f = Secret_Fight("Секиро", "a", "s", "w", "d", ylife, hcons)
    boss_f = Boss_fight("Секиро", "a", "s", "w", "d", ylife, hcons)
    just_f.fight()
    op += plus_op
    print(f"Твой опыт: {op}")
    just_f = Just_Fight("Секиро", "a", "s", "w", "d", ylife, hcons)
    secret_f = Secret_Fight("Секиро", "a", "s", "w", "d", ylife, hcons)
    boss_f = Boss_fight("Секиро", "a", "s", "w", "d", ylife, hcons)
else:
    print("Ты незаметно прокрался среди них")
print("А вот и лес")
print("Ты прошел дальше")
print("- Не желаете поколдовать?")
if input("1.Поговорить; 2.Проигнорировать: ") == "1":
    print("- Могу продать силовую мощь, но конечно не бесплатно!")
    print(f"Твой опыт: {op}")
    if input("1.Купить силовую мощь(80 опыта); 2.Нечего не покупать: ") == "1":
        if op < 80:
            print("Недостаточно опыта!")
        else:
            op -= 80
            print(f"Твой опыт: {op}")
            print("Ты купил силовую мощь, теперь ты наносишь + 1 урон концитрации")
            hcons += 1
            just_f = Just_Fight("Секиро", "a", "s", "w", "d", ylife, hcons)
            just_f1 = Just_Fight1("Секиро", "a", "s", "w", "d", ylife, hcons)
            just_f2 = Just_Fight2("Секиро", "a", "s", "w", "d", ylife, hcons)
            secret_f = Secret_Fight("Секиро", "a", "s", "w", "d", ylife, hcons)
            boss_f = Boss_fight("Секиро", "a", "s", "w", "d", ylife, hcons)
print("Ты пошел дальше")
print("Погоди, это обезьяна? И откуда у нее катана?")
just_f1.fight()
op += plus_op
print(f"Твой опыт: {op}")
just_f1 = Just_Fight1("Секиро", "a", "s", "w", "d", ylife, hcons)
secret_f = Secret_Fight("Секиро", "a", "s", "w", "d", ylife, hcons)
boss_f = Boss_fight("Секиро", "a", "s", "w", "d", ylife, hcons)
print("Ты прошел дальше")
print("Опять обезьяна")
just_f.fight()
op += plus_op
print(f"Твой опыт: {op}")
just_f1 = Just_Fight1("Секиро", "a", "s", "w", "d", ylife, hcons)
secret_f = Secret_Fight("Секиро", "a", "s", "w", "d", ylife, hcons)
boss_f = Boss_fight("Секиро", "a", "s", "w", "d", ylife, hcons)
print("Ты пошел дальше")
print("- Постойте, постойте!")
if input("1.Поговорить; 2.Проигнорировать: ") == "1":
    print("- Помогите мне, пожайлуста! Моего сына утащило ОГРОМНОЕ удовище. Если согласитесь, то я вас туда доставлю, если победите, то я вас щедро награжу!")
    if input("1.Помочь; 2.Отказатся помогать: ") == "1":
        print("- Спасибо!")
        print("Ты потерял сознание")
        print("Ты очнулся в деревне, окутаной огнем")
        print("Ты втретил того самого ОГРОМНОГО чудища")
        print("Это был великан в колодках")
        secret_f.fight()
        print("Ты снова потерял сознание")
        print("Ты снова переместился к той бабке")
        print("- Где мой сын?")
        print("Ты сказал что там его небыло")
        print("Значит умер... все равно спасибо, как и обещала, вот награда")
        print("Теперь ты наносишь + 1 урон концитрации")
        print("И теперь ты будешь получать больше опыта!")
        plus_op += 10
        hcons += 1
        just_f1 = Just_Fight1("Секиро", "a", "s", "w", "d", ylife, hcons)
        boss_f = Boss_fight("Секиро", "a", "s", "w", "d", ylife, hcons)
print("Ты пошел дальше, до замка осталось чуть-чуть")
print("Опять обезьяна")
print("Наверное они охраняют проход")
just_f1.fight()
op += plus_op
print(f"Твой опыт: {op}")
just_f1 = Just_Fight1("Секиро", "a", "s", "w", "d", ylife, hcons)
boss_f = Boss_fight("Секиро", "a", "s", "w", "d", ylife, hcons)
print("Ты прошел дальше")
print("Еще одна обезьяна")
just_f1.fight()
op += plus_op
print(f"Твой опыт: {op}")
just_f1 = Just_Fight1("Секиро", "a", "s", "w", "d", ylife, hcons)
boss_f = Boss_fight("Секиро", "a", "s", "w", "d", ylife, hcons)
print("А вот и ворота в замок")
print("На твоем пути стояло еще 4 обезьяны")
if input("1.Попробывать убить; 2.Пройти незаметно: ") == "1":
    just_f.fight()
    op += plus_op
    print(f"Твой опыт: {op}")
    just_f1 = Just_Fight1("Секиро", "a", "s", "w", "d", ylife, hcons)
    boss_f = Boss_fight("Секиро", "a", "s", "w", "d", ylife, hcons)
    just_f.fight()
    op += plus_op
    print(f"Твой опыт: {op}")
    just_f1 = Just_Fight1("Секиро", "a", "s", "w", "d", ylife, hcons)
    boss_f = Boss_fight("Секиро", "a", "s", "w", "d", ylife, hcons)
    just_f.fight()
    op += plus_op
    print(f"Твой опыт: {op}")
    just_f1 = Just_Fight1("Секиро", "a", "s", "w", "d", ylife, hcons)
    boss_f = Boss_fight("Секиро", "a", "s", "w", "d", ylife, hcons)
else:
    print("Ты неззаметно их прошел")
print("А вот и замок")
print("- Не желаете поколдовать?")
if input("1.Поговорить; 2.Проигнорировать: ") == "1":
    print("- Могу продать жизненную силу, но конечно не бесплатно!")
    print(f"Твой опыт: {op}")
    if input("1.Купить жизненную силу(100 опыта); 2.Нечего не покупать: ") == "1":
        if op < 100:
            print("Недостаточно опыта!")
        else:
            op -= 100
            print(f"Твой опыт: {op}")
            print("Ты купил жизненную, теперь у тебя + 3 сдоровья")
            ylife += 3
            just_f = Just_Fight("Секиро", "a", "s", "w", "d", ylife, hcons)
            just_f1 = Just_Fight1("Секиро", "a", "s", "w", "d", ylife, hcons)
            just_f2 = Just_Fight2("Секиро", "a", "s", "w", "d", ylife, hcons)
            secret_f = Secret_Fight("Секиро", "a", "s", "w", "d", ylife, hcons)
            boss_f = Boss_fight("Секиро", "a", "s", "w", "d", ylife, hcons)
print("Ты пошел дальше")
print("До господина осталось совсем чуть-чуть")
print("Ты встретил самурая")
print("Он совсем не настроен дружелюбно")
just_f2.fight()
op += plus_op
print(f"Твой опыт: {op}")
just_f2 = Just_Fight2("Секиро", "a", "s", "w", "d", ylife, hcons)
boss_f = Boss_fight("Секиро", "a", "s", "w", "d", ylife, hcons)
print("Ты прошел дальше")
print("Очередной самурай")
just_f2.fight()
op += plus_op
print(f"Твой опыт: {op}")
just_f2 = Just_Fight2("Секиро", "a", "s", "w", "d", ylife, hcons)
boss_f = Boss_fight("Секиро", "a", "s", "w", "d", ylife, hcons)
print("- Подождите")
if input("1.Послушать; 2.Проигнорировать: ") == "1":
    print("- Вы встречали мою маму? Она говорит что меня утащил великан.")
    if input("1.Сказать что встречал; 2.Сказать что не встречал: ") == "1":
        print("- Можете показать дорогу к ней?")
        if input("1.Показать дорогу; 2.Не показывать дорогу: ") == "1":
            print("- Спасибо вам огрoмное! В свою благодарность, я вам наколдую!")
            print("Теперь у тебя + 3 урон концитрации")
            hcons += 1
            just_f2 = Just_Fight2("Секиро", "a", "s", "w", "d", ylife, hcons)
            boss_f = Boss_fight("Секиро", "a", "s", "w", "d", ylife, hcons)
print("Ты пошел дальше")
print("Опять очередной самурай")
just_f2.fight()
op += plus_op
print(f"Твой опыт: {op}")
just_f2 = Just_Fight2("Секиро", "a", "s", "w", "d", ylife, hcons)
boss_f = Boss_fight("Секиро", "a", "s", "w", "d", ylife, hcons)
print("Ты подошел к дому")
print("Услышал разговор двух человек")
if input("1.Подслушать; 2.Пройти мимо: ") == "1":
    print("- Как думаешь, синоби сможет пробраться в главную башню?")
    print("- Если и сможет, Иссин Элдера об этом позаботится")
    print("- Согласен")
print("Ты пошел дальше")
print("Очередной самурай")
just_f2.fight()
op += plus_op
print(f"Твой опыт: {op}")
just_f2 = Just_Fight2("Секиро", "a", "s", "w", "d", ylife, hcons)
boss_f = Boss_fight("Секиро", "a", "s", "w", "d", ylife, hcons)
