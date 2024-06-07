import time
import os
print ("Для индентитификации ПК назовите файл PC_(Номер)!")
PC_list = []

i = 1
Name = "PC/PC_"
while 1 > 0:
    Name_Data = (Name + str(i) + ".txt")
    if os.path.exists(Name_Data) == True:
        PC_list.append(Name_Data)
        i = i + 1
    elif os.path.exists(Name_Data) == False:
        break

Stop_list = [""," "]
True_list = ["Y","y","Д","д"]
False_list = ["N","n","Н","н"]
Avto_list = ["А","A","а","a"]
Manual_list = ["Р","R","р","r"]
D_Mode = False

def D_Start ():
    Start = time.perf_counter()
    return Start

def D_Stop ():
    print ("")
    print ("Время выполнения: " + str(time.perf_counter()-Start))
    print ("")

def Profit (seconds):
    minutes = seconds // 60
    hours = minutes // 60
    days = hours // 24
    months = days // 30  # Приблизительное значение
    years = days // 365  # Приблизительное значение

    seconds %= 60
    minutes %= 60
    hours %= 24
    days %= 30
    months %= 12

    return [int(years), int(months), int(days), int(hours), int(minutes), int(seconds)]

def Analitic_profit (Hour, Day, Time_Use, Client_Hour, Money_Hour):
    Profit = (((int(Time_Use) * int(Money_Hour)) * int(Client_Hour))*(int(Hour)/int(Time_Use)))*int(Day)
    return Profit

def PC_Price_One (PC_list, i):
    File = PC_list[i]
    with open(File, 'r') as F:
        lines = F.readlines()

    #Части
    Motherboard = int(lines[1])
    GPU = int(lines[3])
    CPU = int(lines[5])
    HDD = int(lines[7])
    SSD = int(lines[9])
    RAM = int(lines[11])
    Power_supply_unit = int(lines[13])
    CPU_Fan = int(lines[15])
    Fan = int(lines[17])
    Case = int(lines[19])
    Screen = int(lines[21])
    Keyboard = int(lines[23])
    Mouse = int(lines[25])
    Headphones = int(lines[27])
    Table = int(lines[29])
    Chair = int(lines[31])
    #Доп. информация
    RAM_Quantity = int(lines[33])
    HDD_Quantity = int(lines[35])
    SSD_Quantity = int(lines[37])

    PC_Money = Expenses_Club_PC (Motherboard,GPU,CPU,HDD,SSD,RAM,Power_supply_unit,CPU_Fan,
                                 Fan,Case,Screen,Keyboard,Mouse,Headphones,Table,Chair,
                                 RAM_Quantity,HDD_Quantity,SSD_Quantity)
    return PC_Money

def Software_One (PC_list, i):
    File = PC_list[i]
    with open(File, 'r') as F:
        lines = F.readlines()

    Game_list = [lines[i][0] for i in range(42, 66, 2)]
    return Game_list

def Money_One (PC_list, i):
    File = PC_list[i]
    with open(File, 'r') as F:
        lines = F.readlines()

    Money = lines[39][0:2]
    return Money

def Expenses_Club_PC (Motherboard,GPU,CPU,HDD,SSD,RAM,Power_supply_unit,CPU_Fan,Fan,
                      Case,Screen,Keyboard,Mouse,Headphones,Table,Chair,RAM_Quantity,
                      HDD_Quantity,SSD_Quantity):

    #Материнская плата
    Motherboards_List = {
        "0": 0,
        "1": 48,
        "2": 164,
        "3": 360
    }
    Motherboard_Price = Motherboards_List.get(Motherboard)

    #GPU
    GPUs_List = {
        "0": 0,
        "1": 68,
        "2": 130,
        "3": 246,
        "4": 417,
        "5": 830
    }
    GPU_Price = GPUs_List.get(GPU)

    #CPU
    CPUs_List = {
        "0": 0,
        "1": 29,
        "2": 58,
        "3": 89,
        "4": 116,
        "5": 130,
        "6": 194,
        "7": 170,
        "8": 189,
        "9": 438,
        "10": 610
    }
    CPU_Price = CPUs_List.get(CPU)

    #HDD
    HDDs_List = {
        "0": 0,
        "1": 32,
        "2": 58,
        "3": 120,
        "4": 210
    }
    HDD_Price = HDDs_List.get(HDD)

    #SSD
    SSDs_List = {
        "0": 0,
        "1": 50,
        "2": 90,
        "3": 170
    }
    SSD_Price = SSDs_List.get(SSD)

    #ОЗУ
    RAMs_List = {
        "0": 0,
        "1": 12,
        "2": 30,
        "3": 40,
        "4": 80,
        "5": 98,
        "6": 138,
        "7": 200
    }
    RAM_Price = RAMs_List.get(RAM)

    #Блок питания
    Power_supply_units_List = {
        "0": 0,
        "1": 30,
        "2": 46,
        "3": 70,
        "4": 100,
        "5": 130,
        "6": 200
    }
    Power_supply_unit_Price = Power_supply_units_List.get(Power_supply_unit)

    #Охлаждение процессора
    CPU_Fans_List = {
        "0": 0,
        "1": 26,
        "2": 90
    }
    CPU_Fan_Price = CPU_Fans_List.get(CPU_Fan)

    #Охлаждение корпуса
    Fans_List = {
        "0": 0,
        "1": 18,
        "2": 64
    }
    Fan_Price = Fans_List.get(Fan)

    #Корпус
    Cases_List = {
        "0": 0,
        "1": 17,
        "2": 34,
        "3": 68,
        "4": 120,
        "5": 200
    }
    Case_Price = Cases_List.get(Case)

    #Монитор
    Screens_List = {
        "0": 0,
        "1": 27,
        "2": 70,
        "3": 133,
        "4": 270,
        "5": 570
    }
    Screen_Price = Screens_List.get(Screen)

    #Клавиатура
    Keyboards_List = {
        "0": 0,
        "1": 14,
        "2": 36,
        "3": 68
    }
    Keyboard_Price = Keyboards_List.get(Keyboard)

    #Мышь
    Mouses_List = {
        "0": 0,
        "1": 8,
        "2": 20,
        "3": 46,
        "4": 160
    }
    Mouse_Price = Mouses_List.get(Mouse)

    #Наушники
    Headphones_List = {
        "0": 0,
        "1": 25,
        "2": 70,
        "3": 120
    }
    Headphones_Price = Headphones_List.get(Headphones)

    #Стол
    Tables_List = {
        "0": 0,
        "1": 23,
        "2": 66,
        "3": 210,
        "4": 300,
        "5": 780
    }
    Table_Price = Tables_List.get(Table)

    #Стул
    Chairs_list = {
        "0": 0,
        "1": 13,
        "2": 169,
        "3": 460
    }
    Chair_Price = Chairs_list.get(Chair)

    Price = (Motherboard_Price + GPU_Price + CPU_Price + (HDD_Price * HDD_Quantity) + (SSD_Price * SSD_Quantity) + (RAM_Price * RAM_Quantity) + Power_supply_unit_Price + CPU_Fan_Price + Fan_Price + Case_Price + Screen_Price + Keyboard_Price + Mouse_Price + Headphones_Price + Table_Price + Chair_Price)
    return Price

while 1 > 0:
    print ("")
    print ("Финансовая панель клуба")
    print ("0 - Закрыть панель")
    print ("D - Активация Debag Mode")
    print ("1 - Подсчёт дохода клуба")
    print ("2 - Подсчёт окупаемости")
    print ("3 - Стоимость нового рабочего места")
    print ("4 - Подробная информация")
    print ("5 - ПО для рабочих мест")
    com = input ("")

    if com == "0":
        break
    elif com == "D": #Режим проверки
        print ("")
        
        if D_Mode == False:
            D_Mode = True
        elif D_Mode == True:
            D_Mode = False

        print ("Debag Mode: " + str(D_Mode))

    elif com == "1": #Подсчёт доходности
        print ("")

        com = input ("Выберите режим работы (А/Р): ")
        if com in Stop_list:
            com = "Р"

        if com in Avto_list:
            print ("Индентифецированно " + str(len(PC_list)) + " ПК.")
            print ("")
            Money_S = 0
            PC = len (PC_list)

            for i in range(len(PC_list)):
                Money_S = Money_S + int(Money_One (PC_list, i))
            Money = Money_S / len(PC_list)
        elif com in Manual_list:
            PC = input ("Количество ПК: ")
            Money = input ("Стоимость часа использования ПК ($\час): ")
            print ("")

        if PC in Stop_list:
            PC = "0"
        if Money in Stop_list:
            Money = "0"

        if D_Mode == True:
            Start = D_Start ()

        print ("График работы: " + str(24) + "/" + str(7))
        print ("Доход за рабочий год: " + str (int(Analitic_profit (24, 360, 1, PC, Money))) + " $.")
        print ("Доход за 6 рабочих месяцев: " + str (int(Analitic_profit (24, 180, 1, PC, Money))) + " $.")
        print ("Доход за рабочий месяц: " + str (int(Analitic_profit (24, 30, 1, PC, Money))) + " $.")
        print ("Доход за 7 рабочих дней: " + str (int(Analitic_profit (24, 7, 1, PC, Money))) + " $.")
        print ("Доход за 1 рабочий день: " + str (int(Analitic_profit (24, 1, 1, PC, Money))) + " $.")
        print ("Доход за 12 рабочих часов: " + str (int(Analitic_profit (12, 1, 1, PC, Money))) + " $.")
        print ("Доход за 1 рабочий час: " + str (int(Analitic_profit (1, 1, 1, PC, Money))) + " $.")

        if D_Mode == True:
            D_Stop ()

    elif com == "3": #Стоимость ПК
        print ("")
        print ("Стоимость нового рабочего места")
        print ("ПК")
        Motherboard = input ("Уровень материнской платы [0|1|2|3]: ")
        GPU = input ("Уровень видеокарты [0|1|2|3|4|5]: ")
        CPU = input ("Уровень процессора [0|1|2|3|4|5|6|7|8|9|10]: ")
        HDD = input ("Уровень HDD [0|1|2|3|4]: ")
        SSD = input ("Уровень SSD [0|1|2|3]: ")
        RAM = input ("Уровень ОЗУ [0|1|2|3|4|5|6|7]: ")
        Power_supply_unit = input ("Уровень блока питания [0|1|2|3|4|5|6]: ")
        CPU_Fan = input ("Уровень охлаждения процессора [0|1|2]: ")
        Fan = input ("Уровень охлаждения корпуса [0|1|2]: ")
        Case = input ("Уровень корпуса [0|1|2|3|4|5]: ")
        print ("")
        print ("Переферия")
        Screen = input ("Уровень монитора [0|1|2|3|4|5]: ")
        Keyboard = input ("Уровень клавиатуры [0|1|2|3]: ")
        Mouse = input ("Уровень мышки [0|1|2|3|4]: ")
        Headphones = input ("Уровень наушников [0|1|2|3]: ")
        print ("")
        print ("Доп. расходы")
        Table = input ("Уровень стола [0|1|2|3|4|5]: ")
        Chair = input ("Уровень стула [0|1|2|3]: ")

        if D_Mode == True:
            D_Start ()

        if Motherboard in Stop_list:
            Motherboard = "0"
        if GPU in Stop_list:
            GPU = "0"
        if CPU in Stop_list:
            CPU = "0"
        if HDD in Stop_list:
            HDD = "0"
        if SSD in Stop_list:
            SSD = "0"
        if RAM in Stop_list:
            RAM = "0"
        if Power_supply_unit in Stop_list:
            Power_supply_unit = "0"
        if CPU_Fan in Stop_list:
            CPU_Fan = "0"
        if Fan in Stop_list:
            Fan = "0"
        if Case in Stop_list:
            Case = "0"
        if Screen in Stop_list:
            Screen = "0"
        if Keyboard in Stop_list:
            Keyboard = "0"
        if Mouse in Stop_list:
            Mouse = "0"
        if Headphones in Stop_list:
            Headphones = "0"
        if Table in Stop_list:
            Table = "0"
        if Chair in Stop_list:
            Chair = "0"

        if RAM > "0":
            if Motherboard == "1":
                RAM_Quantity = input ("Количесво плашек ОЗУ (2 мах): ")

                if Motherboard == "1" and int(RAM_Quantity) > 2:
                    RAM_Quantity = 2
                
            elif Motherboard == "2":
                RAM_Quantity = input ("Количесво плашек ОЗУ (4 max): ")

                if Motherboard == "2" and int(RAM_Quantity) > 4:
                    RAM_Quantity = 4
            
            elif Motherboard == "3":
                RAM_Quantity = input ("Количесво плашек ОЗУ (2 мах): ")

                if Motherboard == "3" and int(RAM_Quantity) > 2:
                    RAM_Quantity = 2
        else:
            RAM_Quantity = 0

        if HDD > "0":
            HDD_Quantity = input ("Количесво HDD: ")

            if int(HDD_Quantity) > 3:
                HDD_Quantity = 3
        else:
            HDD_Quantity = 0

        if SSD > "0":
            SSD_Quantity = input ("Количесво SSD: ")

            if int(SSD_Quantity) > 2:
                SSD_Quantity = 2
        else:
            SSD_Quantity = 0
        
        print ("Стоимость ПК: " + str(int(Expenses_Club_PC (Motherboard,GPU,CPU,HDD,SSD,RAM,Power_supply_unit,CPU_Fan,Fan,
                      Case,Screen,Keyboard,Mouse,Headphones,Table,Chair,RAM_Quantity,HDD_Quantity,SSD_Quantity))) + " $.")

        if D_Mode == True:
            D_Stop ()

    elif com == "4": #Подробная информация
        print ("")
        print ("Индентифецированно " + str(len(PC_list)) + " ПК.")
        print ("")
        Money_list = []
        Price_list = []
        for i in range(len(PC_list)):
            print ("ПК №" + str(i+1))
            Money = Money_One (PC_list, i)

            if D_Mode == True:
                Start = D_Start ()

            print ("Цена: " + str(PC_Price_One (PC_list, i)) + " $.")
            print ("Доходность за 1 час: " + str(Money) + " $.")

            Prof = int(Money)/3600
            Second = PC_Price_One (PC_list, i)/round(Prof,3)
            Round_Second = round(Second, 0)

            Time = Profit(Round_Second)
            second = Time[5]
            minute = Time[4]
            hour = Time[3]
            day = Time[2]
            month = Time[1]
            year = Time[0]

            if second > 0 and minute == 0 and hour == 0 and day == 0 and month == 0 and year == 0:
                print ("ПК окупится за " + str(second) + ".")
            elif minute > 0 and hour == 0 and day == 0 and month == 0 and year == 0:
                print ("ПК окупится за " + str(minute) + ":" + str(second) + ".")
            elif hour > 0 and day == 0 and month == 0 and year == 0:
                print ("ПК окупится за " + str(hour) + ":" + str(minute) + ":" + str(second) + ".")
            elif day > 0 and month == 0 and year == 0:
                print ("ПК окупится за " + str(day) + ":" + str(hour) + ":" + str(minute) + ": " + str(second) + ".")
            elif month > 0 and year == 0:
                print ("ПК окупится за " + str(month) + ":" + str(day) + ":" + str(hour) + ":" + str(minute) + ":" + str(second) + ".")
            elif year > 0:
                print ("ПК окупится за " + str(year) + ":" + str(month) + ":" + str(day) + ":" + str(hour) + ":" + str(minute) + ":" + str(second) + ".")
            
            print ("")
            Money_list.append (int(Money))

            if D_Mode == True:
                D_Stop ()

        Money_len = len(Money_list)
        Money = sum(Money_list)
        Money_SR = round((Money/Money_len),2)

        for i in range(len(PC_list)):
            Price = PC_Price_One (PC_list, i)
            Price_list.append (int(Price))
        Price = sum(Price_list)
        
        print ("Стоимость рабочих мест: " + str(Price) + " $.")
        print ("Общая доходность за час: " + str(int(Money)) + " $.")
        print ("Средняя доходность с ПК: " + str(Money_SR) + " $.")

    elif com == "2": #Подсчёт окупаемости
        print ("")
        Price = 0
        Money = 0

        com = input ("Выберите режим работы (А/Р): ")
        if com in Stop_list:
            com = "Р"

        if com in Avto_list:
            print ("Индентифецированно " + str(len(PC_list)) + " ПК.")
            print ("")
            Price = input ("Стоимость ($): ")
            
            for i in range(len(PC_list)):
                Money = Money + int(Money_One (PC_list, i))
            PC = len(PC_list)

        elif com in Manual_list:
            Price = input ("Стоимость ($): ")
            Money = input ("Доход ПК ($/час): ")
            PC = input ("Количество ПК: ")

        if Price in Stop_list:
            Price = "0"
        if Money in Stop_list:
            Money = "0"
        if PC in Stop_list:
            PC = "0"

        if D_Mode == True:
            Start = D_Start ()

        Prof = (int(Money)*int(PC))/3600
        Second = int(Price)/round(Prof,3)
        Round_Second = round(Second, 0)
    
        Time = Profit(Round_Second)
        second = Time[5]
        minute = Time[4]
        hour = Time[3]
        day = Time[2]
        month = Time[1]
        year = Time[0]
        
        if second > 0 and minute == 0 and hour == 0 and day == 0 and month == 0 and year == 0:
            print ("Сумма " + str(Price) + " окупится за " + str(second) + ".")
        elif minute > 0 and hour == 0 and day == 0 and month == 0 and year == 0:
            print ("Сумма " + str(Price) + " окупится за " + str(minute) + ":" + str(second) + ".")
        elif hour > 0 and day == 0 and month == 0 and year == 0:
            print ("Сумма " + str(Price) + " окупится за " + str(hour) + ":" + str(minute) + ":" + str(second) + ".")
        elif day > 0 and month == 0 and year == 0:
            print ("Сумма " + str(Price) + " окупится за " + str(day) + ":" + str(hour) + ":" + str(minute) + ": " + str(second) + ".")
        elif month > 0 and year == 0:
            print ("Сумма " + str(Price) + " окупится за " + str(month) + ":" + str(day) + ":" + str(hour) + ":" + str(minute) + ":" + str(second) + ".")
        elif year > 0:
            print ("Сумма " + str(Price) + " окупится за " + str(year) + ":" + str(month) + ":" + str(day) + ":" + str(hour) + ":" + str(minute) + ":" + str(second) + ".")

        if D_Mode == True:
            D_Stop ()

    elif com == "5": #ПО для компьютеров
        print ("")
        print ("Индентифецированно " + str(len(PC_list)) + " ПК.")
        print ("")
        PC = int(len(PC_list))


        Subscription = input ("Стоимость подписки антивируса [0|1|2|3]: ")
        if Subscription in Stop_list:
            Subscription = "0"

        if Subscription == "0":
            Subscription = 0
        elif Subscription == "1":
            Subscription = 15
        elif Subscription == "2":
            Subscription = 50
        elif Subscription == "3":
            Subscription = 160

        Games = []

        for i in range(int(PC)):
            print ("")
            print ("Игры на ПК №" + str(i+1))

            Software = Software_One (PC_list, i)

            Game = 0
            No_Game = 0
            Game_1 = str(Software[0]) #Mood
            Game_2 = str(Software[1]) #Car Cry 5
            Game_3 = str(Software[2]) #Grand Auto 4
            Game_4 = str(Software[3]) #Half-Lifa 4
            Game_5 = str(Software[4]) #Need for sped
            Game_6 = str(Software[5]) #Dota 3
            Game_7 = str(Software[6]) #Sins 8
            Game_8 = str(Software[7]) #Ctulhu
            Game_9 = str(Software[8]) #Assasin`s Cried 2
            Game_10 = str(Software[9]) #Kaptial: War Zone
            Game_11 = str(Software[10]) #Mincraft
            Game_12 = str(Software[11]) #Call of Dad

            if D_Mode == True:
                Start = D_Start ()

            if Game_1 in True_list:
                Game = Game + 20
            elif Game_1 in False_list:
                No_Game = No_Game + 20
                
            if Game_2 in True_list:
                Game = Game + 32
            elif Game_2 in False_list:
                No_Game = No_Game + 32
                
            if Game_3 in True_list:
                Game = Game + 32
            elif Game_3 in False_list:
                No_Game = No_Game + 32
                
            if Game_4 in True_list:
                Game = Game + 16
            elif Game_4 in False_list:
                No_Game = No_Game + 16
                
            if Game_5 in True_list:
                Game = Game + 22
            elif Game_5 in False_list:
                No_Game = No_Game + 22
                
            if Game_6 in True_list:
                Game = Game + 8
            elif Game_6 in False_list:
                No_Game = No_Game + 8
                
            if Game_7 in True_list:
                Game = Game + 16
            elif Game_7 in False_list:
                No_Game = No_Game + 16
                
            if Game_8 in True_list:
                Game = Game + 14
            elif Game_8 in False_list:
                No_Game = No_Game + 14
                
            if Game_9 in True_list:
                Game = Game + 32
            elif Game_9 in False_list:
                No_Game = No_Game + 32
                
            if Game_10 in True_list:
                Game = Game + 10
            elif Game_10 in False_list:
                No_Game = No_Game + 10
                
            if Game_11 in True_list:
                Game = Game + 26
            elif Game_11 in False_list:
                No_Game = No_Game + 26
                
            if Game_12 in True_list:
                Game = Game + 32
            elif Game_12 in False_list:
                No_Game = No_Game + 32

            print ("Стоимость игр на ПК №" + str(i+1) + ": " + str(Game) + " $.")
            if No_Game > 0:
                print ("Для полного набора игр нужно: " + str(No_Game) + " $.")
            Games.append (Game)

            if D_Mode == True:
                D_Stop ()

        list_Games = sum(Games)

        print ("")
        print ("Антивирус на 1 ПК: " + str(round(Subscription/int(PC),2)) + " $.")
        print ("Общяя стоимость игр: " + str(int(list_Games)) + " $.")
        
    
    else:
        print ("Неизвестная команда!")
    
