import logging

# asctime : 生成された時刻を人間が読める書式で表したもの。
# levelname : メッセージのための文字のロギングレベル ('DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL')。
# message : msg % args として求められた、ログメッセージ。 Formatter.format()

logging.basicConfig(filename='samplelog.txt',level=logging.DEBUG,format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('プログラム開始')

def factorial(n):
    logging.debug('factorial({})開始'.format(n))
    total = 1
    for i in range(n + 1):
        total = 1
        for i in range(1, n + 1):
            total *= i
            logging.debug('i = {},total={}'.format(i,total))
    logging.debug('factorial({})'.format(n))
    return total

print(factorial(5))
logging.debug('プログラム終了')

