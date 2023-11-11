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
    
    return Time

def Analitic_profit (Hour, Day, Time_Use, Client_Hour, Money_Hour):
    Profit = (((int(Time_Use) * int(Money_Hour)) * int(Client_Hour))*(int(Hour)/int(Time_Use)))*int(Day)
    return Profit

def PC_Price_One (PC_list, i):
    File = PC_list[i]
    F = open (File, 'r')

    #Части
    F.readline ()
    Motherboard = int(F.readline ())
    F.readline ()
    GPU = int(F.readline ())
    F.readline ()
    CPU = int(F.readline ())
    F.readline ()
    HDD = int(F.readline ())
    F.readline ()
    SSD = int(F.readline ())
    F.readline ()
    RAM = int(F.readline ())
    F.readline ()
    Power_supply_unit = int(F.readline ())
    F.readline ()
    CPU_Fan = int(F.readline ())
    F.readline ()
    Fan = int(F.readline ())
    F.readline ()
    Case = int(F.readline ())
    F.readline ()
    Screen = int(F.readline ())
    F.readline ()
    Keyboard = int(F.readline ())
    F.readline ()
    Mouse = int(F.readline ())
    F.readline ()
    Headphones = int(F.readline ())
    F.readline ()
    Table = int(F.readline ())
    F.readline ()
    Chair = int(F.readline ())
    F.readline ()
    #Доп. информация
    RAM_Quantity = int(F.readline ())
    F.readline ()
    HDD_Quantity = int(F.readline ())
    F.readline ()
    SSD_Quantity = int(F.readline ())

    F.close()
    
    PC_Money = Expenses_Club_PC (Motherboard,GPU,CPU,HDD,SSD,RAM,Power_supply_unit,CPU_Fan,
                                 Fan,Case,Screen,Keyboard,Mouse,Headphones,Table,Chair,
                                 RAM_Quantity,HDD_Quantity,SSD_Quantity)
    return PC_Money

def Software_One (PC_list, i):
    File = PC_list[i]
    F = open (File, 'r')

    for i in range(42):
        F.readline ()

    Game_1 = F.readline ()
    F.readline ()
    Game_2 = F.readline ()
    F.readline ()
    Game_3 = F.readline ()
    F.readline ()
    Game_4 = F.readline ()
    F.readline ()
    Game_5 = F.readline ()
    F.readline ()
    Game_6 = F.readline ()
    F.readline ()
    Game_7 = F.readline ()
    F.readline ()
    Game_8 = F.readline ()
    F.readline ()
    Game_9 = F.readline ()
    F.readline ()
    Game_10 = F.readline ()
    F.readline ()
    Game_11 = F.readline ()
    F.readline ()
    Game_12 = F.readline ()

    F.close()

    Game_1 = Game_1[0]
    Game_2 = Game_2[0]
    Game_3 = Game_3[0]
    Game_4 = Game_4[0]
    Game_5 = Game_5[0]
    Game_6 = Game_6[0]
    Game_7 = Game_7[0]
    Game_8 = Game_8[0]
    Game_9 = Game_9[0]
    Game_10 = Game_10[0]
    Game_11 = Game_11[0]
    Game_12 = Game_12[0]

    Game_list = (Game_1,Game_2,Game_3,Game_4,Game_5,Game_6,Game_7,Game_8,Game_9,Game_10,Game_11,Game_12)
    return Game_list

def Money_One (PC_list, i):
    File = PC_list[i]
    F = open (File, 'r')

    for i in range(39):
        F.readline ()

    Money = F.readline ()
    Money = Money[0:2]

    F.close()
    return Money

def Expenses_Club_PC (Motherboard,GPU,CPU,HDD,SSD,RAM,Power_supply_unit,CPU_Fan,Fan,
                      Case,Screen,Keyboard,Mouse,Headphones,Table,Chair,RAM_Quantity,
                      HDD_Quantity,SSD_Quantity):

    #Материнская плата
    if str(Motherboard) == "0":
        Motherboard_Price = 0
    elif str(Motherboard) == "1":
        Motherboard_Price = 48
    elif str(Motherboard) == "2":
        Motherboard_Price = 164
    elif str(Motherboard) == "3":
        Motherboard_Price = 360
    else:
        Motherboard_Price = 0

    #GPU
    if str(GPU) == "0":
        GPU_Price = 0
    elif str(GPU) == "1":
        GPU_Price = 68
    elif str(GPU) == "2":
        GPU_Price = 130
    elif str(GPU) == "3":
        GPU_Price = 246
    elif str(GPU) == "4":
        GPU_Price = 417
    elif str(GPU) == "5":
        GPU_Price = 830
    else:
        GPU_Price = 0

    #CPU
    if str(CPU) == "0":
        CPU_Price = 0
    elif str(CPU) == "1":
        CPU_Price = 29
    elif str(CPU) == "2":
        CPU_Price = 58
    elif str(CPU) == "3":
        CPU_Price = 89
    elif str(CPU) == "4":
        CPU_Price = 116
    elif str(CPU) == "5":
        CPU_Price = 130
    elif str(CPU) == "6":
        CPU_Price = 194
    elif str(CPU) == "7":
        CPU_Price = 170
    elif str(CPU) == "8":
        CPU_Price = 289
    elif str(CPU) == "9":
        CPU_Price = 438
    elif str(CPU) == "10":
        CPU_Price = 610
    else:
        CPU_Price = 0

    #HDD
    if str(HDD) == "0":
        HDD_Price = 0
    elif str(HDD) == "1":
        HDD_Price = 32
    elif str(HDD) == "2":
        HDD_Price = 58
    elif str(HDD) == "3":
        HDD_Price = 120
    elif str(HDD) == "4":
        HDD_Price = 210
    else:
        HDD_Price = 0

    #SSD
    if str(SSD) == "0":
        SSD_Price = 0
    elif str(SSD) == "1":
        SSD_Price = 50
    elif str(SSD) == "2":
        SSD_Price = 90
    elif str(SSD) == "3":
        SSD_Price = 170
    else:
        SSD_Price = 0

    #ОЗУ
    if str(RAM) == "0":
        RAM_Price = 0
    elif str(RAM) == "1":
        RAM_Price = 12
    elif str(RAM) == "2":
        RAM_Price = 30
    elif str(RAM) == "3":
        RAM_Price = 40
    elif str(RAM) == "4":
        RAM_Price = 80
    elif str(RAM) == "5":
        RAM_Price = 98
    elif str(RAM) == "6":
        RAM_Price = 138
    elif str(RAM) == "7":
        RAM_Price = 200
    else:
        RAM_Price = 0

    #Блок питания
    if str(Power_supply_unit) == "0":
        Power_supply_unit_Price = 0
    elif str(Power_supply_unit) == "1":
        Power_supply_unit_Price = 30
    elif str(Power_supply_unit) == "2":
        Power_supply_unit_Price = 46
    elif str(Power_supply_unit) == "3":
        Power_supply_unit_Price = 70
    elif str(Power_supply_unit) == "4":
        Power_supply_unit_Price = 100
    elif str(Power_supply_unit) == "5":
        Power_supply_unit_Price = 130
    elif str(Power_supply_unit) == "6":
        Power_supply_unit_Price = 200
    else:
        Power_supply_unit_Price = 0

    #Охлаждение процессора
    if str(CPU_Fan) == "0":
        CPU_Fan_Price = 0
    elif str(CPU_Fan) == "1":
        CPU_Fan_Price = 26
    elif str(CPU_Fan) == "2":
        CPU_Fan_Price = 90
    else:
        CPU_Fan_Price = 0

    #Охлаждение корпуса
    if str(Fan) == "0":
        Fan_Price = 0
    elif str(Fan) == "1":
        Fan_Price = 18
    elif str(Fan) == "2":
        Fan_Price = 64
    else:
        Fan_Price = 0

    #Корпус
    if str(Case) == "0":
        Case_Price = 0
    elif str(Case) == "1":
        Case_Price = 17
    elif str(Case) == "2":
        Case_Price = 34
    elif str(Case) == "3":
        Case_Price = 68
    elif str(Case) == "4":
        Case_Price = 120
    elif str(Case) == "5":
        Case_Price = 200
    else:
        Case_Price = 0

    #Монитор
    if str(Screen) == "0":
        Screen_Price = 0
    elif str(Screen) == "1":
        Screen_Price = 27
    elif str(Screen) == "2":
        Screen_Price = 70
    elif str(Screen) == "3":
        Screen_Price = 133
    elif str(Screen) == "4":
        Screen_Price = 270
    elif str(Screen) == "5":
        Screen_Price = 570
    else:
        Screen_Price = 0

    #Клавиатура
    if str(Keyboard) == "0":
        Keyboard_Price = 0
    elif str(Keyboard) == "1":
        Keyboard_Price = 14
    elif str(Keyboard) == "2":
        Keyboard_Price = 36
    elif str(Keyboard) == "3":
        Keyboard_Price = 68
    else:
        Keyboard_Price = 0

    #Мышь
    if str(Mouse) == "0":
        Mouse_Price = 0
    elif str(Mouse) == "1":
        Mouse_Price = 8
    elif str(Mouse) == "2":
        Mouse_Price = 20
    elif str(Mouse) == "3":
        Mouse_Price = 46
    elif str(Mouse) == "4":
        Mouse_Price = 160
    else:
        Mouse_Price = 0

    #Наушники
    if str(Headphones) == "0":
        Headphones_Price = 0
    elif str(Headphones) == "1":
        Headphones_Price = 25
    elif str(Headphones) == "2":
        Headphones_Price = 70
    elif str(Headphones) == "3":
        Headphones_Price = 120
    else:
        Headphones_Price = 0

    #Стол
    if str(Table) == "0":
        Table_Price = 0
    elif str(Table) == "1":
        Table_Price = 23
    elif str(Table) == "2":
        Table_Price = 66
    elif str(Table) == "3":
        Table_Price = 210
    elif str(Table) == "4":
        Table_Price = 300
    elif str(Table) == "5":
        Table_Price = 780
    else:
        Table_Price = 0

    #Стул
    if str(Chair) == "0":
        Chair_Price = 0
    elif str(Chair) == "1":
        Chair_Price = 13
    elif str(Chair) == "2":
        Chair_Price = 169
    elif str(Chair) == "3":
        Chair_Price = 460
    else:
        Chair_Price = 0

    Price = (int(Motherboard_Price) + int(GPU_Price) + int(CPU_Price) + (int(HDD_Price) * int(HDD_Quantity))
             + (int(SSD_Price) * int(SSD_Quantity)) + (int(RAM_Price) * int(RAM_Quantity)) + int(Power_supply_unit_Price) +
             int(CPU_Fan_Price) + int(Fan_Price) + int(Case_Price) + int(Screen_Price) + int(Keyboard_Price) +
             int(Mouse_Price) + int(Headphones_Price) + int(Table_Price) + int(Chair_Price))
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
    
