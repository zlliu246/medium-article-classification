import os 

for i in range(51, 101):
    cmd = f'rm data/normal/{i}.txt'
    os.system(cmd)
    print(cmd)