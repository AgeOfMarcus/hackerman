def merge_list(list1, list2):
	res = list1
	for i in list2:
		if not i in res:
			res.append(i)
	return res
