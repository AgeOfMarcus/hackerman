def merge_list(list1, list2):
	res = list1
	for i in list2:
		if not i in res:
			res.append(i)
	return res

def merge_dict(dict1, dict2):
	res = dict1
	for i in dict2:
		if not i in res:
			res[i] = dict2[i]
	return res
