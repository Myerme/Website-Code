import os

desktop= os.path.join(os.path.join(os.environ['USERPROFILE']), "Downloads")
print(desktop)

x = 1
for x in range(5):
#while True:
    NewFolder = "you are an idiot" + str(x)
    FolderPath = os.path.join(desktop, NewFolder)
    os.mkdir(FolderPath)
   # x = x + 1