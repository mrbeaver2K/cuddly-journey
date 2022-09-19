import os
import random
import shutil

chosen = random.choice(os.listdir("./photos"))
os.unlink("../daily/cat.jpg")
shutil.copy("./photos/" + chosen, "../daily/")
os.rename("../daily/" + chosen, "../daily/cat.jpg")