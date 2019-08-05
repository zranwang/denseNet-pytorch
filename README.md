# denseNet-pytorch--车牌字符分类  
一、主要贡献为：  
1.使用denseNet结合多尺度pooling，实现车牌字符分类，加入多尺度pooling，特征增强，网络收敛更加快，泛化能力变强，在两次epoch后，准确率达到95%以上，最后的准确率达到99%以上。  
2.收集了65种车牌字符样本，每种有350个样本。  
3.在文件夹dataProcessing中，实现了如何让DataLoader读取自己样本，主要实现在myDataset.py文件中。  
4.文件paddingImage.py将图像填充，扩大到35*35  
5.文件train_valid_split.py用来分隔训练集和测试集  
6.文件generate_txt.py，生成每张图片的路径和对应标签，最后写在txt文件上  
  
二、环境要求：  
PyTorch >=1.0.0  
CUDA  
fire（pip install fire）  
  
三、使用  
python ./code/demo.py --efficient True  
  
四、参考  
https://github.com/gpleiss/efficient_densenet_pytorch  
