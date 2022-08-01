from locale import currency

currenncy_deno = {2000:0, 500:0, 200:0, 100:0, 50:0, 20:0, 10:0, 5:0, 2:0, 1:0}
N = int(input("Please enter the amount: "))
deno = N

for curr in currenncy_deno.keys():
    if deno != 0:
        currenncy_deno[curr] = deno // curr
        deno = deno % curr
    
for curr in currenncy_deno.keys():
    if currenncy_deno[curr] != 0:
        print('%d: %d' %(curr, currenncy_deno[curr]))
