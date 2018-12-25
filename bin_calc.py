# -*- coding:utf-8 -*-

# 导入读取 csv 的 Python 模块
# csv 是 Python 的内置模块，无需安装
import csv
# 导入数学函数库，Python 的内置库
import math

# 注意 floor 和 round 的用法，floor 是取整运算，但不四舍五入
def get_bin_index(wind_speed, bin_size = 0.5):
	return math.floor(wind_speed / bin_size)

	
if __name__ == '__main__':

	# 在这里换成你的实际文件路径
	input_file = '/Users/jiguorui/tmp/33.txt'
	output_file = 'out_put.csv'

	# 用这个结构来存放每个 bin 的中间计算结果
	bin_data_hub = {}

	# 打开数据文件
	with open(input_file) as f:
		
		# csv 读取
		reader = csv.reader(f)
		
		# 这里的 wind_speed_column 要根据你的数据文件修改，0 开始的索引值
		# 比如，如果风速在数据文件的第 1 列，这里应该是 0， 如果是第 2 列这里应该是 1
		# 我这个数据文件的风速在第 4 列，所以是 3
		wind_speed_column = 3

		# 功率的位置，和上述一个道理
		power_column = 21

		# 一行一行遍历整个数据
		for row in reader:
			try:
				# 得到风速数据,
				wind_speed = float(row[wind_speed_column])

				# 得到功率数据
				power = float(row[power_column])

				# 计算 bin 的位置
				bin_index = get_bin_index(wind_speed)

				# 看看是否已经有过计算结果
				if bin_index in bin_data_hub:
					# 如果有就分别计算累计和，次数
					bin_data_hub[bin_index][0] += wind_speed
					bin_data_hub[bin_index][1] += power
					bin_data_hub[bin_index][2] += 1          # 计数
				else:
					# 如果没有, 直接赋值
					bin_data_hub[bin_index] = [wind_speed, power, 1]
			except:
				pass

	# 计算平均值
	for bindex, data_item in bin_data_hub.items():
		wind_average = round(data_item[0]/data_item[2],2)
		power_average = round(data_item[1]/data_item[2],2)

		# 最后添上那个 1 仅仅是为了保持和第 56 行数据结构一致，其实可以不要
		bin_data_hub[bindex] = [wind_average, power_average, 1]

	# 把结果写到 csv 文件里保存
	with open(output_file, 'wt') as fo:
		fo.write("wind_speed, power\n")
		for i in range(48):
			if i in bin_data_hub:
				# 把数字转换成字符串
				row = list(map(str, bin_data_hub[i]))
				# 用逗号隔开
				s_row = ",".join(row)

				# 写出一行结果
				fo.write(s_row)
				fo.write("\n")


			
