import time

def stopwatch(mode): 
    input("Press ENTER to start")
    
    localTime = time.strftime("%X")
    startTime = localTime.split(':')
    
    totalStartSeconds = int(startTime[0]) * 3600 + int(startTime[1]) * 60 + int(startTime[2])
    
    
    option = ''
    while option != 'S' or option != 's':
        option = input("E for elapsed time\nS to stop: ")
        
        if (option != 'e' and option != 'E' and option != 's' and option != 'S'):
            print("Incorrect value")
            continue
        
        currentLocalTime = time.strftime("%X")
        currentTime = currentLocalTime.split(':')
        
        currentSeconds = int(currentTime[0]) * 3600 + int(currentTime[1]) * 60 + int(currentTime[2])            
        elapsedTime = currentSeconds - totalStartSeconds
        
        hours = elapsedTime // 3600
        minutes = (elapsedTime % 3600) // 60
        seconds = (elapsedTime % 3600) % 60
        
        if (option == 'E' or option == 'e'):
            
            print(str(hours).rjust(2, '0'), ':' + str(minutes).rjust(2, '0'), ':' + str(seconds).rjust(2, '0'))
            
        elif (option == 'S' or option == 's'):
            
            print(str(hours).rjust(2, '0'), ':' + str(minutes).rjust(2, '0'), ':' + str(seconds).rjust(2, '0'))
            
            break
        
    mode = 0
    
    return mode