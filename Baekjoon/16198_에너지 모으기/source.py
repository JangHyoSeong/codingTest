N = int(input())
weights = list(map(int, input().split()))

def find_max(weights, energy):
    if len(weights) == 2:
        return energy
    
    max_energy = 0

    for i in range(1, len(weights) - 1):
        energy_sum  = weights[i-1] * weights[i+1]
        new_weights = weights[:i] + weights[i+1:]
        max_energy = max(max_energy, find_max(new_weights, energy + energy_sum))

    
    return max_energy

print(find_max(weights, 0))