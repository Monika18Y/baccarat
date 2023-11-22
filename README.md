# baccarat 百家乐
Implement baccarat game based on Python
基于Python实现baccarat游戏

# Introduce 介绍
This program basically implements the card dealing of the Baccarat game. The game rules are taken from the relevant entries in Wikipedia and are basically the same as the Macau gameplay.

本程序基本实现了百家乐游戏的发牌，游戏规则取自维基百科中相关词条，与澳门玩法基本无异

Since I am a beginner in Python, the code has problems such as bloat and inefficiency in many places. I welcome your criticisms and corrections. Thank you.

由于本人是python初学者，因此代码在很多地方存在臃肿低效等问题，欢迎大家批评指正，谢谢


# Game process 游戏过程
1. Automatically draw 4 poker cards at the beginning

开局自动抽取4张扑克

3.  Determine whether to draw cards

判定是否补牌

5.  Compare the banker and player points

判断两家点数大小


# Code analysis 代码简析
1.  Define eight decks of playing cards with suits and kings removed
定义八副含花色去除大小王的扑克牌
2.  Build judgment function
构建判断函数
3.  4 cards are drawn at the beginning (according to standard baccarat rules, the same below)
开局抽取4张卡（按照标准百家乐规则，下同）
4.  Convert JQKA card type to points
转换JQKA牌型为点数
5.  Determine the subsequent licensing situation and automatically decide whether to issue cards based on the situation
判断后续发牌情况，根据情况自动决定是否发牌
6.  Compare the point of the banker and player and output the result
判定两家点数大小并输出结果


# Statement 声明
This program is only for communication and learning of Python programs. No one may use it to violate local regulations.
本程序仅供Python程序交流学习，任何人不得用于违反当地法规
