
"""
Req # 1 : Input to the function is the car speed and output shall be speed level
Req # 2 :Function shall calculate output to be :
		If          Speed < 0    Level shall be Invalid 
		If     0 <= Speed < 40  Level shall be Low
		If    40 <= Speed < 120 Level shall be Normal
		If   120 <= Speed < 200 Level shall be High
		If   200 <= Speed < 220 Level shall be V.High 
		If   220 <  Speed       Level shall be Invalid


"""

def speed_level(speed):
    if speed < 0:
        return "Invalid"
    elif 0 <= speed < 40:
        return "Low"
    elif 40 <= speed < 120:
        return "Normal"
    elif 120 <= speed < 200:
        return "High"
    elif 200 <= speed < 220:
        return "V.High"
    elif speed >= 220:
        return "Invalid"


"""
Req # 1 : Input to the function is student Scores and output student Level
Req# 2 : Function shall calculate output to be :
		If         Score < 0    Level shall be Invalid 
		If    0 <= Score < 50   Level shall be Failed 
		If   50 <= Score < 65   Level shall be Passed
		If   65 <= Score < 75   Level shall be Good
		If   75 <= Score < 85   Level shall be V.Good
		If   85 <= Score < 100  Level shall be Excellent 
		If  100 <  Score        Level shall be Invalid

-1 =Invalid      49 =Failed    64 =Passed     74 =Good      84=V.Good        99 =Excellent
 0=Failed        50 =Passed    65  =Good      75 =V.Good    85 =Excellent    100 Invalid
 1=Failed        51 =Passed    66  =Good      76 =V.Good    86 =Excellent    101=Invalid
"""

def score_level(score):
    if score < 0:
        return "Invalid"
    elif 0 <= score < 50:
        return "Failed"
    elif 50 <= score < 65:
        return "Passed"
    elif 65 <= score < 75:
        return "Good"
    elif 75 <= score < 85:
        return "V.Good"
    elif 85 <= score < 100:
        return "Excellent"
    elif score >= 100:
        return "Invalid"
