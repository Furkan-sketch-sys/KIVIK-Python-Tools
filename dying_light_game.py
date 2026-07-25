x = 0
time = 21

safe_zones = ["Factory-0" , "Industrial Zone" , "Tower-19" , "Old Town" , "Fisherman Village" , "Villa Area"]

while x < len(safe_zones) :
    print(f"\n[SCANNİNG] Time {time} : 00 -> Factory {x+1} : {safe_zones[x]}")


    current_score = int(input(f"Please enter the zombie count for {safe_zones[x]} 0-100 : "))

    if current_score < 25 :
        print(f"[SAFE] : Zombie Count is very low ({current_score}). Sector is clear for shelter.")
        x+=1
        time+=1
        continue

    if current_score >= 95 :
        print(f"[ALERT-BEWARE] : {safe_zones[x]} is captured by Volatiles who are a brutal variant. (Current Score {current_score})")
        print("[SYSTEM] : Due to safety reasons, loop is terminated.")
        break
    
    print(f"[ALERT] : Someone is moving around the place. High-Tension Situation : {current_score}")
    x+=1
    time+=1

        
