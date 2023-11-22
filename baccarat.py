import random  # 导入random模块，用于生成随机数
import re
import time

suits = ['黑桃一   ', '红心一   ', '梅花一   ', '方块一   ', '黑桃二   ', '红心二   ', '梅花二   ', '方块二   ',
         '黑桃三   ', '红心三   ', '梅花三   ', '方块三   ', '黑桃四   ', '红心四   ', '梅花四   ', '方块四   ',
         '黑桃五   ', '红心五   ', '梅花五   ', '方块五   ', '黑桃六   ', '红心六   ', '梅花六   ', '方块六   ',
         '黑桃七   ', '红心七   ', '梅花七   ', '方块七   ', '黑桃八   ', '红心八   ', '梅花八   ',
         '方块八   ']  # 定义扑克牌的花色和点数
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']  # 定义扑克牌的点数
deck = [suit + rank for suit in suits for rank in ranks]  # 生成八副完整的扑克牌
remaining_deck = deck.copy()  # 复制一副扑克牌，用于剩余的牌

    # 校正数值并判定大小函数
def compare(c1,c2):
    if c1 < 10:
        c1 = c1
    elif 10 <= c1 < 20:
        c1 = c1 - 10
    else:
        c1 = 0
    if c2 < 10:
        c2 = c2
    elif 10 <= c2 < 20:
        c2 = c2 - 10
    else:
        c2 = 0
    if c1 > c2:
        print("闲", c1, "点  庄", c2, "点\n闲赢")
    elif c1 < c2:
        print("闲", c1, "点  庄", c2, "点\n庄赢")
    else:
        print("闲", c1, "点  庄", c2, "点\n和局")

    # 提取数字函数
def extract_numbers(a):
    numbers = re.findall('\d', a)
    return int(''.join(numbers))


while True:  # 无限循环，直到牌抽完或者用户选择退出
    if not remaining_deck:  # 如果剩余的牌为空
        print("牌已抽完，请重新开始。")
        break  # 跳出循环


    # 每回合开局抽取四张卡
    # 从剩余的牌中随机抽取
    card1 = random.choice(remaining_deck)
    card2 = random.choice(remaining_deck)
    card3 = random.choice(remaining_deck)
    card4 = random.choice(remaining_deck)
    print("闲第一张:", card1, "\n闲第二张:", card3, "\n庄第一张:", card2, "\n庄第二张:", card4)
    # 从卡池中移除已抽卡牌
    remaining_deck.remove(card1)
    remaining_deck.remove(card2)
    remaining_deck.remove(card3)
    remaining_deck.remove(card4)
    # 转换JKQA
    card1 = card1.replace('J', '10').replace('Q', '10').replace('K', '10').replace('A', '1')
    card2 = card2.replace('J', '10').replace('Q', '10').replace('K', '10').replace('A', '1')
    card3 = card3.replace('J', '10').replace('Q', '10').replace('K', '10').replace('A', '1')
    card4 = card4.replace('J', '10').replace('Q', '10').replace('K', '10').replace('A', '1')


    card1point = extract_numbers(card1)
    card2point = extract_numbers(card2)
    card3point = extract_numbers(card3)
    card4point = extract_numbers(card4)

    # 输出首次发牌两家点数
    player = card1point + card3point
    banker = card2point + card4point
    if player < 10:
        playerpoint = player
    elif 10 <= player <= 19:
        playerpoint = player - 10
    else:
        playerpoint = player - 20
    if banker < 10:
        bankerpoint = banker
    elif 10 <= banker <= 19:
        bankerpoint = banker - 10
    else:
        bankerpoint = banker - 20
    time.sleep(2)
    print(playerpoint, bankerpoint)

    #补牌判定
    if playerpoint == 8 or playerpoint == 9 or bankerpoint == 8 or bankerpoint == 9:#天牌情况
        result = compare(playerpoint, bankerpoint)  # 判定结果
        print("天牌")
        user_input = input("是否继续？输入c继续，其他键退出游戏：")
        if user_input.lower() == "c":
            continue  # 继续下一轮循环
        else:
            break
    #补牌情况
    elif 0 <= playerpoint < 6:  #闲补牌（0~6）
        card5 = random.choice(remaining_deck)
        time.sleep(2)
        print("闲补牌：", card5)
        remaining_deck.remove(card5)  # 从剩余的牌中移除这张牌
        card5 = card5.replace('J', '10').replace('Q', '10').replace('K', '10').replace('A', '1')
        card5point = extract_numbers(card5)
        Lastpointplayer = playerpoint + card5point

        #庄补牌情况（闲需要补牌)
        if bankerpoint == 0 or bankerpoint == 1 or bankerpoint ==2: #庄两张和（0~2）补牌
            card6 = random.choice(remaining_deck)
            time.sleep(2)
            print("庄补牌：", card6)
            remaining_deck.remove(card6)  # 从剩余的牌中移除这张牌
            card6 = card6.replace('J', '10').replace('Q', '10').replace('K', '10').replace('A', '1')
            card6point = extract_numbers(card6)
            Lastpointbanker = bankerpoint + card6point
            time.sleep(2)
            result = compare(Lastpointplayer,Lastpointbanker) #判定结果
            user_input = input("是否继续？输入c继续，其他键退出游戏：")
            if user_input.lower() == "c":
                continue  # 继续下一轮循环
            else:
                break
        elif bankerpoint == 3:  #庄两张和3点补牌情况
            if card5point == 8:#庄两张和3点无需补牌
                time.sleep(2)
                result = compare(Lastpointplayer, bankerpoint)#判定结果
                user_input = input("是否继续？输入c继续，其他键退出游戏：")
                if user_input.lower() == "c":
                    continue  # 继续下一轮循环
                else:
                    break
            else:#庄两张和3点补牌
                card7 = random.choice(remaining_deck)
                time.sleep(2)
                print("庄补牌：", card7)
                remaining_deck.remove(card7)  # 从剩余的牌中移除这张牌
                card7 = card7.replace('J', '10').replace('Q', '10').replace('K', '10').replace('A', '1')
                card7point = extract_numbers(card7)
                Lastpointbanker = bankerpoint + card7point
                time.sleep(2)
                result = compare(Lastpointplayer, Lastpointbanker)  # 判定结果
                user_input = input("是否继续？输入c继续，其他键退出游戏：")
                if user_input.lower() == "c":
                    continue  # 继续下一轮循环
                else:
                    break
        elif bankerpoint == 4:#庄两张和4点补牌情况
            if card5point == 10 or card5point == 1 or card5point == 8 or card5point == 9:#庄两张和4无需补牌
                time.sleep(2)
                result = compare(Lastpointplayer, bankerpoint)  # 判定结果
                user_input = input("是否继续？输入c继续，其他键退出游戏：")
                if user_input.lower() == "c":
                    continue  # 继续下一轮循环
                else:
                    break
            else:# 庄两张和4补牌
                card8 = random.choice(remaining_deck)
                time.sleep(2)
                print("庄补牌：", card8)
                remaining_deck.remove(card8)  # 从剩余的牌中移除这张牌
                card8 = card8.replace('J', '10').replace('Q', '10').replace('K', '10').replace('A', '1')
                card8point = extract_numbers(card8)
                Lastpointbanker = bankerpoint + card8point
                time.sleep(2)
                result = compare(Lastpointplayer, Lastpointbanker)  # 判定结果
                user_input = input("是否继续？输入c继续，其他键退出游戏：")
                if user_input.lower() == "c":
                    continue  # 继续下一轮循环
                else:
                    break
        elif bankerpoint == 5:# 庄两张和5点补牌情况
            if card5point == 10 or card5point == 1 or card5point == 2 or card5point == 3 or card5point == 8 or card5point == 9:  # 庄两张和5无需补牌
                time.sleep(2)
                result = compare(Lastpointplayer, bankerpoint)  # 判定结果
                user_input = input("是否继续？输入c继续，其他键退出游戏：")
                if user_input.lower() == "c":
                    continue  # 继续下一轮循环
                else:
                    break
            else:  # 庄两张和5补牌
                card9 = random.choice(remaining_deck)
                time.sleep(2)
                print("庄补牌：", card9)
                remaining_deck.remove(card9)  # 从剩余的牌中移除这张牌
                card9 = card9.replace('J', '10').replace('Q', '10').replace('K', '10').replace('A', '1')
                card9point = extract_numbers(card9)
                Lastpointbanker = bankerpoint + card9point
                time.sleep(2)
                result = compare(Lastpointplayer, Lastpointbanker)  # 判定结果
                user_input = input("是否继续？输入c继续，其他键退出游戏：")
                if user_input.lower() == "c":
                    continue  # 继续下一轮循环
                else:
                    break
        elif bankerpoint == 6:# 庄两张和6点补牌情况
            if card5point == 6 or card5point == 7:# 庄两张和6补牌
                card10 = random.choice(remaining_deck)
                time.sleep(2)
                print("庄补牌：", card10)
                remaining_deck.remove(card10)  # 从剩余的牌中移除这张牌
                card10 = card10.replace('J', '10').replace('Q', '10').replace('K', '10').replace('A', '1')
                card10point = extract_numbers(card10)
                Lastpointbanker = bankerpoint + card10point
                time.sleep(2)
                result = compare(Lastpointplayer, Lastpointbanker)  # 判定结果
                user_input = input("是否继续？输入c继续，其他键退出游戏：")
                if user_input.lower() == "c":
                    continue  # 继续下一轮循环
                else:
                    break
            else:  # 庄两张和6无需补牌
                time.sleep(2)
                result = compare(Lastpointplayer, bankerpoint)  # 判定结果
                user_input = input("是否继续？输入c继续，其他键退出游戏：")
                if user_input.lower() == "c":
                    continue  # 继续下一轮循环
                else:
                    break
        else:#其他情况庄无需补牌（庄大于等于7）
            time.sleep(2)
            result = compare(Lastpointplayer, bankerpoint)  # 判定结果
            user_input = input("是否继续？输入c继续，其他键退出游戏：")
            if user_input.lower() == "c":
                continue  # 继续下一轮循环
            else:
                break
    elif playerpoint == 6 or playerpoint == 7: #闲无需补牌情况（6~7点）
        if bankerpoint < 6:#庄两张和0~5补牌
            card11 = random.choice(remaining_deck)
            time.sleep(2)
            print("庄补牌：", card11)
            remaining_deck.remove(card11)  # 从剩余的牌中移除这张牌
            card11 = card11.replace('J', '10').replace('Q', '10').replace('K', '10').replace('A', '1')
            card11point = extract_numbers(card11)
            Lastpointbanker = bankerpoint + card11point
            time.sleep(2)
            result = compare(playerpoint, Lastpointbanker)  # 判定结果
            user_input = input("是否继续？输入c继续，其他键退出游戏：")
            if user_input.lower() == "c":
                continue  # 继续下一轮循环
            else:
                break
        else:#庄两张和6点及以上无需补牌
            time.sleep(2)
            result = compare(playerpoint, bankerpoint)  # 判定结果
            user_input = input("是否继续？输入c继续，其他键退出游戏：")
            if user_input.lower() == "c":
                continue  # 继续下一轮循环
            else:
                break
    else:  #不存在的情况
        print("嘻嘻")
        break
