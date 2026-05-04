import json
import math

with open("", 'r', encoding = 'utf-8')as f:
    i = json.load(f)

lst = []
time = 0
for j in i:
    t = j.get('time')
    time += t
    lst.append(t)

avg_time = time/len(i)

s = 0
for j in i:
    t = j.get('time')
    x = (t - avg_time)**2
    s += x

variance = s/len(i)
sd = math.sqrt(variance)

print(f'avg time: {avg_time :.2f}')
print(f'variance: {variance :.2f}')
print(f'standard deviation: {sd :.2f}')
print(f'max time: {max(lst):.2f}')
print(f'min time: {min(lst):.2f}')