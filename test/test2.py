"""
@author: MH
@contact: menghedianmo@163.com
@file: test2.py
@time: 2018/7/24 10:31

        LocalStack<线程隔离栈>
"""
from werkzeug.local import LocalStack
# 实例化县城隔离栈
s = LocalStack()

# 将想要隔离的对象推入到栈中
s.push('dm')

# 取栈顶元素
print(s.top)

# top方法并不会清除掉栈内元素
print(s.top)

# 出栈，释放资源（释放栈顶元素）
s.pop()

# 出栈以后栈内资源被释放，所以栈顶元素为空
print(s.top)
