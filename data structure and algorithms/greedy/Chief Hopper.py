#lope for 1 to  increase 1
def chiefHopper(arr):
    start_energy = 0
    for i in range(10**10):
        energy = start_energy
        # check for current energy
        for item in arr:
            energy = energy * 2 - item
            if energy < 0:
                break
        if energy >= 0:
            return start_energy
        start_energy = i 
