burgers, drinks, sides = map(int, input().split())

burger_money = list(map(int, input().split()))
drinks_money = list(map(int, input().split()))
sides_money = list(map(int, input().split()))


num_of_set = min(burgers, drinks, sides)

burger_sum = sum(burger_money)
drinks_sum = sum(drinks_money)
sides_sum = sum(sides_money)
no_sale_sum = burger_sum + drinks_sum + sides_sum

burger_money.sort(reverse=True)
drinks_money.sort(reverse=True)
sides_money.sort(reverse=True)

for i in range(num_of_set):
    burger_money[i] *= 0.9
    drinks_money[i] *= 0.9
    sides_money[i] *= 0.9

burger_sum = sum(burger_money)
drinks_sum = sum(drinks_money)
sides_sum = sum(sides_money)
sale_sum = burger_sum + drinks_sum + sides_sum

print(no_sale_sum)
print(int(sale_sum))