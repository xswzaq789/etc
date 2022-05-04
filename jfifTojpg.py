import os
import glob


files = glob.glob("C://Users//a//Desktop//AI전공//수입맥주-학습용//AI전공//호가든로제//*.*")


for name in files :
    if not os.path.isdir(name) :
        src = os.path.splitext(name)
        os.rename(name,  src[0] + '.jpg')
