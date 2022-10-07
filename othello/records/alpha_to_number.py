
def transfer(record: str) -> list:
    kifu = [record[x:x+2] for x in range(0, len(record), 2)]
    return kifu


def to_number(kifu: list):
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    num = ['1', '2', '3', '4', '5', '6', '7', '8']

    for i in range(8):
        kifu = kifu.replace(alpha[i], num[i])
    return kifu

def to_text(kifu):
    with open('record_n.txt', 'w') as f:
        f.write('Y\n')
        f.write('kataoka\n')
        f.write('takeya\n')
        for i in range(len(kifu)):
           f.write(kifu[i] + '\n')

def read_text(data):
    with open(data, 'r') as f:
        kifu = f.readline()
    return kifu

kifu = read_text('record1.txt')
to_text(list(to_number(kifu)))

print("ファイルを生成しました！")