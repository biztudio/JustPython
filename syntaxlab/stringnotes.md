转义
* \ 用于标识转义字符，如果需要显示 \, 则是 \\
* r'' 标识 '' 内部的字符串默认不转义, 举例 比较 print('\\\t\\') 与 print(r'\\\t\\')


多行
* '''...''' 标识多行内容，这样比自行添加 \n 来得方便


[Python字符串编码](http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431664106267f12e9bef7ee14cf6a8776a479bdec9b9000)
* ASCII 编码用一个字节标识一个字符；
* Unicode 编码通常用两个字节(byte, 16bit)标识一个字符, 所以在ASCII编码的字符转Unicode编码只需要在前面补0, 比如 A 编码对应 (ASCII 01000001 \ Unicode 00000000 01000001)；
* UTF-8 编码是一种"可变长短" Unicode 编码，以节省存储空间。UTF-8 把一个 Unicode 字符根据不同的数字大小编码成 1-6 个字节，对于大量英文字符的文本可以节省空间;
* 通常在计算机内存中，统一使用Unicode编码，当需要保存到硬盘或者需要传输的时候，就转换为UTF-8编码；
* Python3 中，字符串是以Unicode编码的； 



