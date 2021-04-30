from collections import defaultdict
s = ["mission statement","a quick bite to eat","a chip off the old block","chocolate bar","mission impossible","a man on a mission","block party","eat my words","bar of soap"]
s = ["writing code", "code rocks"]
s = ["I like bubblegum",
"bubblegum that is pink",
"hi, how are you today",
"today on this fine day",
"day that is sunny"]

words = defaultdict(list)
ans = []

for i in s:
	split = i.split()
	startingWord = split[0]
	words[startingWord].append(split[1:])

for i in s:
	endingWord = i.split()[-1]
	for phrase in words[endingWord]:
		combo = [i] + phrase
		ans.append(" ".join(combo))

	


print(ans)