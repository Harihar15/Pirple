''' a game for those who are fooled by their friends '''
# In this game a friend of yours told you that you are facing a specific direction (either North or South)
# You don't know directions to confirm whether he is truthful or not
# But you know the time and where the sun is, it can either be to your right or to your left
# A fact that everyone knows that sun rises from east and sets in west

Time = 10                             # 24 hr format

Friend_Stat = "north"                 # Friend statement ---> You are facing north

Sun = "left"                         # sun is at your right

if Time > 12 and Sun == "left":
    if Friend_Stat == "north":
        print("Your friend is fooling you ,You are facing South")
    else:
        print("Friend is truthful and Honest,You can rely on him")


elif Time < 12 and Sun == "left":
    if Friend_Stat == "north":
        print("Friend is truthful and Honest,You can rely on him")
    else:
        print("Your friend is fooling you ,You are facing South")


elif Time > 12 and Sun == "right":
    if Friend_Stat == "north":
        print("Friend is truthful and Honest,You can rely on him")
    else:
        print("Your friend is fooling you ,You are facing South")


elif Time < 12 and Sun == "right":
    if Friend_Stat == "north":
        print("Your friend is fooling you ,You are facing South")
    else:
        print("Friend is truthful and Honest,You can rely on him")

elif Time == 12:
    print("Wait for more time to see whether sun is to you left or right (sun is over your head)")