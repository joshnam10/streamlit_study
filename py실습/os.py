import os

print(os.listdir('algorithm'))

for folder in ['intro','algorithm']:
    for file in os.listdir(folder):
        print("./"+folder+"/"+file)
