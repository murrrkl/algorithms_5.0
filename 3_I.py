file = open('input.txt', 'r')
file1 = open('output.txt', 'w')

lines = file.readlines()

com1 = "Total goals for " # 16 <Название команды> — количество голов, забитое данной командой за все матчи
com2 = "Mean goals per game for " # 24 <Название команды> - среднее количество голов, забиваемое данной командой за один матч
com3 = "Total goals by " # 15 <Имя игрока> - количество голов, забитое данным игроком за все матчи
com4 = "Mean goals per game by " # 23 <Имя игрока> - среднее количество голов, забиваемое данным игроком за один матч его команды
com5 = "Goals on minute " # 16 <Минута> by <Имя игрока> - количество голов, забитых данным игроком ровно на указанной минуте матча
com6 = "Goals on first " #  15 <T> minutes by <Имя игрока> — количество голов, забитых данным игроком на минутах с первой по T-ю включительно.
com7 = "Goals on last " # 14 <T> minutes by <Имя игрока> — количество голов, забитых данным игроком на минутах с (91 - T)-й по 90-ю включительно
com8 = "Score opens by " # 15 <Название команды> — сколько раз данная команда открывала счет в матче.

commands = {} # Команда: [голы, 0 - открыла матч, кол-во матчей]
players = {} # Игрок: [команда, 0 - открыл матч, кол-во голов, {минута_гол: кол-во, минута_гол: кол-во}

name_f = ""
name_s = ""
score_f = 0
score_s = 0
count_comm = 0

cur_min = 91
open_name = ""

for i in range (len(lines)):
    s = lines[i]
    s = s.replace("\n", "")
    if "-" in s:
        end_name = s.find('"', 1)
        name_f = s[1:end_name]
        start_name = s.find('"', end_name + 1)
        end_name = s.find('"', start_name + 1)
        name_s = s[start_name + 1:end_name]
        sep = s.find(':')

        score_f = int(s[sep-2: sep])
        score_s = int(s[sep+1:])

        if name_f not in commands:
            commands[name_f] = [0, 0, 0]
        if name_s not in commands:
            commands[name_s] = [0, 0, 0]

        commands[name_f][0] += score_f
        commands[name_s][0] += score_s
        commands[name_f][2] += 1
        commands[name_s][2] += 1
        cur_min = 91
    elif score_f != 0 or score_s != 0:
        last_space = s.rfind(" ")
        player_name = s[:last_space]
        minute = int(s[last_space:-1])

        if player_name not in players:
            if score_f != 0:
                players[player_name] = [name_f, 0, 0, {}]      
            else:
                players[player_name] = [name_s, 0, 0, {}]

        if score_f != 0:
            score_f -= 1
        else:
            score_s -= 1

        players[player_name][2] += 1

        if minute not in players[player_name][3]:
            players[player_name][3][minute] = 0
        players[player_name][3][minute] += 1

        if cur_min > minute:
            cur_min = minute
            open_name = player_name

        if score_f == 0 and score_s == 0:
            players[open_name][1] += 1 # Открыл матч
            commands[players[open_name][0]][1] += 1

    else:
        if count_comm != 0:
            file1.write("\n")
        count_comm += 1
        if com1 in s:
            comm_name = s[17:-1]
            if comm_name in commands:
                file1.write(str(commands[comm_name][0]))
            else:
                file1.write("0")
        elif com2 in s:
            name = s[24:]
            name = name.replace('"', "")
            if name in commands:
                file1.write(str(commands[name][0] / commands[name][2]))
            else:
                file1.write("0")
        elif com3 in s:
            p_name = s[15:]
            if p_name in players:
                file1.write(str(players[p_name][2]))
            else:
                file1.write("0")
        elif com4 in s:
            p_name = s[23:]
            if p_name in players:
                file1.write(str(players[p_name][2] / commands[players[p_name][0]][2]))
            else:
                file1.write("0")
            
        elif com5 in s:
            p_name = s[16:]
            space = p_name.find(" ")
            minute = int(p_name[:space])
            p_name = p_name[space + 4:]
            if p_name in players and minute in players[p_name][3]:
                file1.write(str(players[p_name][3][minute]))
            else:
                file1.write("0")
        elif com6 in s:
            p_name = s[15:]
            space = p_name.find(" ")
            minute = int(p_name[:space])
            p_name = p_name[space + 12:]
            count = 0
            if p_name in players:
                for m in players[p_name][3]:
                    if m <= minute:
                        count += players[p_name][3][m]
            file1.write(str(count))
        elif com7 in s:
            p_name = s[14:]
            space = p_name.find(" ")
            minute = 91 - int(p_name[:space])
            p_name = p_name[space + 12:]
            count = 0
            if p_name in players:
                for m in players[p_name][3]:
                    if m >= minute:
                        count += players[p_name][3][m]
            file1.write(str(count))
        elif com8 in s:
            name = s[15:]
            if '"' in name:
                name = name.replace('"', "")
                if name in commands:
                    file1.write(str(commands[name][1]))
                else:
                    file1.write("0")
            else:
                if name in players:
                    file1.write(str(players[name][1]))
                else:
                    file1.write("0")

file.close
file1.close
