
#거스름돈을 가장 적은 동전 개수로 지급 (500원 , 100원 , 50원 , 10원) 
list = [0 for i in range(4)] 

sum = int(input("거스름돈을 입력하세요 : "))

while sum != 0 : 
	
  if sum >= 500 :   # 남은 거스름돈의 합이 500원이 넘을 때
		list[0] += 1    # 500원 count
		sum = sum - 500 # 남은 거스름돈에서 500원을 빼줌
	
  elif sum >= 100 : # 남은 거스름돈의 합이 100원이 넘을 때
		list[1] += 1    # 100원 count
		sum = sum - 100 # 남은 거스름돈에서 100원을 빼줌
	
  elif sum >= 50 :  # 50원 count
		list[2] += 1    # 50원 count
		sum = sum - 50  # 남은 거스름돈에서 50원을 빼줌
	
  elif sum >= 10 :  # 10원 count
		list[3] += 1    # 10원 count
		sum = sum - 10  # 남은 거스름돈에서 10원을 빼줌

print("500원 : ",list[0],"개")

print("100원 : ",list[1],"개")

print("50원 : ",list[2],"개") 

print("10원 : ",list[3],"개")
