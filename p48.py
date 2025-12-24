sent = "The sun rises in the east.".lower()
cc = {}
for s in sent:
	if s != "." and s != " ":
		if s in cc:
			cc[s] = cc[s] + 1
		else:
			cc[s] = 1
for k,v in cc.items():
	print(f"{k}={v}")