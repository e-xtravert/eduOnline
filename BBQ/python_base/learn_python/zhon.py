'''
主要想测试一下中文字符处理问题
'''
import re
from zhon.hanzo import punctuation
line = "测试。。去除标点。。"
print(re.sub("[{}]+".format(punctuation), "", line.decode("utf-8"))) # 需要将str转换为unicode