def interest (principal : int , rate : float , time : int ) -> float:
    return  principal * rate * time 
principal = 1000
rate = .05
time = 3

P = int(principal)
R = float(rate )
T = int(time )

I = P * R * T
print("interest" , I)


