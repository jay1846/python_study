states_of_korea = ["seoul","daegu","incheon","busan","kwangju"]

# positive index
print(states_of_korea[0])

# negative index
print(states_of_korea[-1])

# edit is possible
states_of_korea[2] = "INCHEON"
print(states_of_korea)

# append
states_of_korea.append("jeju")
print(states_of_korea)

# extend
states_of_korea.extend(["kangwon","gyeongju"])
print(states_of_korea)