def leaderboard_sort(leaderboard, changes):
    for i in changes:
        
        for j in range(int(i[-1])):
            
            if i[-2] == '+':
                temp = leaderboard.index(i.split(' ')[0])
                leaderboard[temp], leaderboard[temp - 1] = leaderboard[temp - 1], leaderboard[temp]
            else:
                temp = leaderboard.index(i.split(' ')[0])
                leaderboard[temp], leaderboard[temp + 1] = leaderboard[temp + 1], leaderboard[temp]
            
    return leaderboard
