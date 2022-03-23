import os
from shutil import copy,rmtree
import random

def mk_file(file_path):
    if os.path.exists(file_path):
        rmtree(file_path)
    else:
        os.mkdir(file_path)
        
def main():
    random.seed(0) #给定一个随机种子
    flower_class = [cla for cla in os.listdir(os.getcwd()) if os.path.isdir(os.path.join(os.getcwd(),cla))]
    train_dir = os.path.join(os.getcwd(),"train")
    val_dir = os.path.join(os.getcwd(),"val")
    mk_file(train_dir)
    mk_file(val_dir)

    split_rate = 0.1

    for split in flower_class:
        trian_cla_path = os.path.join(train_dir,split)
        mk_file(trian_cla_path)
        val_cla_path  = os.path.join(val_dir,split)
        mk_file(val_cla_path)


    for cla in flower_class:
        origin_path = os.getcwd()
        cla_path = os.path.join(origin_path,cla)
        images = os.listdir(cla_path)
        num = len(images)
        #给定随机采样的索引
        eval_index = random.sample(images,k=int(num*split_rate))
        for index,image in enumerate(images):
            if image in eval_index:
                image_path = os.path.join(cla_path,image)
                new_image_path = os.path.join(val_dir,cla,image)
                copy(image_path,new_image_path)
            else:
                image_path = os.path.join(cla_path,image)
                new_image_path = os.path.join(train_dir,cla,image)
                copy(image_path,new_image_path)

            print("{} processing is over".format(cla))
        print("\n")
    print("game over!")
