n, k, l, c, d, p, nl, np = map(int, input().split())

total_drink = k * l
total_slices = c * d
total_salt = p

toasts_by_drink = total_drink // nl
toasts_by_limes = total_slices
toasts_by_salt = total_salt // np

total_toasts = min(toasts_by_drink, toasts_by_limes, toasts_by_salt)

toasts_per_friend = total_toasts // n

print(toasts_per_friend)
