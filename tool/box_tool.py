def read_file(path):
	tmp = None
	with open(path,'r', encoding='UTF-8') as f:
		tmp = f.readlines()

	out = []
	for r in tmp:
		out.append(r.split(' '))

	return out

def write_file(path, data):
	with open(path, "w", encoding='UTF-8') as f:
		f.writelines(data)

def approach(data, offset):
	out = []

	for index in range(len(data)):
		tmp = [ int(r) for r in data[index][1:] ]

		for index2 in range(4):
			data[index][index2+1] = tmp[index2] + offset[tmp[-1]][index2]
		
		out.append( ' '.join(str(e) for e in data[index]) )

	return out

if __name__ == '__main__':
	# 可以把自動產生出來的 *.box 數值進行偏移
	# 陣列代表第幾頁 陣列中的數值分別是 x y width height
	offset_conf = [
		[10, 10, 0, 0],
		[10, 10, 0, 0],
		[10, 10, 0, 0],
		[10, 10, 0, 0],
		[10, 10, 0, 0],
		[10, 10, 0, 0],
		[10, 10, 0, 0],
		[10, 10, 0, 0]
	]

	path = "chi_tra.dfkai-sb.exp0.box"
	data = read_file(path)

	out = approach(data, offset_conf)

	write_file("out.box", out)

