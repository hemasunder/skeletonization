import pickle
import os


#train files

train_files = os.listdir(r'E:\soulpage\Cyient\skeletonization\dataset\Starting Kit Pixel\train')
test_files = os.listdir(r'E:\soulpage\Cyient\skeletonization\dataset\Starting Kit Pixel\test')

ann_dict = {'train':train_files, 'val':test_files}

with open(r'E:\soulpage\Cyient\skeletonization\dataloader\annotation\fold0.pkl','wb') as f:
    pickle.dump(ann_dict,f)

# with open(r'E:\soulpage\Cyient\skeletonization\dataloader\annotation\fold011.pkl','rb') as f:
#     ann = pickle.load(f)
# print(ann)