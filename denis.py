import time
import random
import threading



stop_games = False
x = 0

def igra():
    global stop_games
    global random_time
    global x    
    
    random_time = random.randint(8,30)
    x = random_time / 2
    
    while random_time != -1:
        
        if random_time > x:
            print(random_time)
            random_time -= 1
            time.sleep(1)
            
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
        

def stop_game():
    global stop_games
    global x
    
    time.sleep(x)
    
    while random_time > 0:
        user_input = input('Напишите stop: ')
        
        if user_input.lower() == "stop":
            stop_games = True
            
        else:
            print("Веденна не правильная команда попробуйте снова")
            stop_game()

        
        

threading.Thread(target=igra).start()        
threading.Thread(target=stop_game, daemon=True).start()
