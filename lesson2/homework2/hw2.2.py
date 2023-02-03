# 2. Петя и Катя – брат и сестра. Петя – студент, а Катя –школьница. Петя помогает Кате по математике. Он задумывает два
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные Петей числа.

def solve(S, P):
    for x in range(1, int(S/2)+1):
        y = S-x
        if x*y == P:
            return (x, y)
    return None

input_data = input().split()
S = int(input_data[0])
P = int(input_data[1])
result = solve(S, P)
if result is None:
    print("No solution")
else:
    print(*result)

