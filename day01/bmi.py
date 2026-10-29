# bmi.py 计算 BMI 并给出区间
height = float(input("请输入身高（米，如 1.75）: "))
weight = float(input("请输入体重（公斤）: "))


bmi = weight / (height ** 2)
print(f"你的 BMI 是 {bmi:.2f}")

if bmi < 18.5:
	print("偏瘦")	
elif bmi < 24:
	print("正常")
elif bmi < 28:
	print("偏胖")
else:
	print("肥胖")
