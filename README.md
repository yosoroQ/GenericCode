# 各代码说明

```python
Deep Sea Trash

    -- rename.py #重命名（视频帧导出后可以根据文件夹命名批量修改文件名）

    -- uiqm.py #计算图像平均UIQM

    -- UCIQE3.py #计算图像平均UCIQE

    -- test3.py (Average PSNR、Average SSIM) #计算图像平均PSNR和SSIM

    -- divide.py #划分train、val、test

    -- enhance-deep-sea-image #数据增强处理

        -- utils #子代码

            -- fusion.py 

            -- LACC.py 

        -- main.py #训练

        -- test_time.py #和main差不多，多一个“测试时间” 
```

```python
Beach litter

    -- crop.py #按尺寸裁剪，默认1080*1080

    -- ColorJitter.py #变换颜色（亮度、对比度、色调、饱和度调整、）

    -- flip.py #水平翻转、提高亮度 

    -- rrandom.py #内含GPU加速

    -- divide.py #划分train、val、test
    
    -- rename.py #重命名（视频帧导出后可以根据文件夹命名批量修改文件名）
```

```shell
Linux

	cd
	
	ls
	
	rm -rf directoryname #非空文件夹（文件）
	
	unzip filename.zip #linux解压文件
	
	tar -cvf archive.tar /path/to/directory #linux压缩文件
	
	mv old_name new_name #重命名文件或目录 

	cp /path/to/folder1/*.jpg /path/to/folder2/ #复制1的文件夹图片到2的文件夹 

	find /path/to/folder1 -type f | wc -l #显示该文件夹下有多少文件	
```







