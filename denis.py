#ну импорты что сказать?
import time
import random
import threading



stop_games = False
x = 0

#The function itself with the game
#Хотя нахуй идите если вы пендосы переведёте если что. Сама функция с игрой
def igra():
    #сука глобалы в кс хули
    global stop_games
    global random_time
    global x    
    
    #Создание рандом таймера + деление на 2 что бы когда прошла половина таймер исчез
    random_time = random.randint(8,30)
    x = random_time / 2
    
    while random_time != -1:
        #Таймер тут есть
        if random_time > x:
            print(random_time)
            random_time -= 1
            time.sleep(1)
            
        #Таймер исчезает тут    
        elif random_time < x:
            
            if stop_games:
                
                if random_time > 0:
                    print(f'''

Осталось {random_time} секунд''')
                    
                elif random_time == 0:
                    print('''

Вы победили!!!!''')
                break
            random_time -= 1
            time.sleep(1) 
        
#Функция которая включает инпут когда проподает таймер
def stop_game():
    global stop_games
    global x
    #Функция ждёт когда пройдёт половина таймера
    time.sleep(x)
    
    while random_time > 0:
        user_input = input('Напишите stop: ')
        
        if user_input.lower() == "stop":
            stop_games = True
        
        #А это если ты еблан и написал не stop а ыещз
        else:
            print("Веденна не правильная команда попробуйте снова")
            stop_game()

        
        
#запуск потоков
threading.Thread(target=igra).start()        
threading.Thread(target=stop_game, daemon=True).start()

#zxc???#zxc???#zxc???#zxc???#zxc???#zxc???#zxc???#zxc???#zxc???#zxc???#zxc???#zxc???#zxc???#zxc???#zxc???
#zxc???#zxc???#zxc???#zxc???#zxc???#zxc???#zxc???#zxc???#zxc???#zxc???#zxc???#zxc???#zxc???#zxc???#zxc???
#zxc???#zxc???#zxc???#zxc???#zxc???#zxc???#zxc???#zxc???#zxc???#zxc???#zxc???#zxc???#zxc???#zxc???#zxc???
#zxc???#zxc???#zxc???#zxc???#zxc???#zxc???#zxc???#zxc???#zxc???#zxc???#zxc???#zxc???#zxc???#zxc???#zxc???
#zxc???#zxc???#zxc???#zxc???#zxc???#zxc???#zxc???#zxc???#zxc???#zxc???#zxc???#zxc???#zxc???#zxc???#zxc???
#zxc???#zxc???#zxc???#zxc???#zxc???#zxc???#zxc???#zxc???#zxc???#zxc???#zxc???#zxc???#zxc???#zxc???#zxc???
#zxc???#zxc???#zxc???#zxc???#zxc???#zxc???#zxc???#zxc???#zxc???#zxc???#zxc???#zxc???#zxc???#zxc???#zxc???
#zxc???#zxc???#zxc???#zxc???#zxc???#zxc???#zxc???#zxc???#zxc???#zxc???#zxc???#zxc???#zxc???#zxc???#zxc???
#zxc???#zxc???#zxc???#zxc???#zxc???#zxc???#zxc???#zxc???#zxc???#zxc???#zxc???#zxc???#zxc???#zxc???#zxc???
