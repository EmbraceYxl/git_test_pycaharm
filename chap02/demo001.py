# @作者:     易小龙
# @学校:     江西财经大学
# @时间:     2022/2/28 16:58

#
# if __name__ == '__main__':
#     pass

def getBMI(height, weight):
    BMI = weight/pow(height, 2)
    if BMI < 18:
        obesity_degree = '偏瘦'
        words = '多吃一点哦！'
    elif 18 <= BMI < 25:
        obesity_degree = '正常体重'
        words = '继续保持呀！'
    elif 25 <= BMI < 30:
        obesity_degree = '超重'
        words = '适当的运动'
    elif 30 <= BMI < 35:
        obesity_degree = '轻度肥胖'
        words = '一周保持一定频率运动哦！'
    elif 35 <= BMI < 40:
        obesity_degree = '中度肥胖'
        words = '少食多餐，多多运动呀！'
    else:
        obesity_degree = '重度肥胖'
        words = '立马放下手机，出去运动健身！！！'
        return BMI, obesity_degree, words

print(getBMI(80, 1.76))