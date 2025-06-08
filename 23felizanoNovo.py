from time import sleep
press = input('Pressione Enter para iniciar a contagem regressiva')
for c in range(10, 0, -1):
    print('\033[1m',c)
    sleep(1)
print('\033[1;33mHAPPY NEW YEAR!\033[m')
