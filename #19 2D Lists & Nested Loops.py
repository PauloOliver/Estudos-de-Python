#Video assistido: https://www.youtube.com/watch?v=rfscVS0vtbw&t=2298s
#"2D Lists & Nested Loops"

number_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]

print(number_grid[1][1])
#Primeiro linha depois coluna

for row in number_grid:
    for col in row:
        print(col)