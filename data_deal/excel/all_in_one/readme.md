# 为什么要用 `vbaProject.bin` ?
本身这个vba在这里没啥作用,`xlswriter` 在保存带有vba or 宏的excel文件时,必须以.xlsm后缀结束(其实这是excel本身的限制)
目前实验如果没有 `workbook.add_vba_project('./vbaProject.bin')`, 即便保存为 .xlsm 也无法打开该文件
索性就在其他带有宏操作的 .xlsm 导出了一个 `vbaProject.bin`, 但实际并没有启用它

# 目录层级的格式
本py只适用于文件层级为 `./file_path0/xxx.txt`  `./file_path1/sec_path/xxx.txt` 的内容解析,并导入至对应的sheet,生成目录
其中`sec_path`需要手动修改循环中`break`条件

# 文件内容
文件名及文件内容需要自己修改脚本进行解析

