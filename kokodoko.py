# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

# マップの横幅 w 、縦幅 h 、移動ログの個数 n
w_in, h_in, n_in = input().split()
w = int(w_in)
h = int(h_in)
n = int(n_in)
# 初期位置 x, y
initX_in, initY_in = input().split()
x = int(initX_in)
y = int(initY_in)
# 移動ログ
log_dir = []
log_len = []
for i in range(n):
    l_dir, l_len = input().split()
    log_dir.append(l_dir)
    log_len.append(int(l_len))

# Update the location based on the log
for i in range(n):
    if log_dir[i] == 'U':
        y = y + log_len[i]
    elif log_dir[i] == 'D':
        y = y - log_len[i]
    elif log_dir[i] == 'R':
        x = x + log_len[i]
    elif log_dir[i] == 'L':
        x = x - log_len[i]
    else:
        print("Something Wrong!!")

x = x % w
y = y % h

if x < 0:
    x = w + x
if y < 0:
    y = h + y

print("{} {}".format(x, y))
 


