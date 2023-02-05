# warm-up

Скрипт свапает ETH => coin в одной из трех сетей : arbitrum / optimism / arbitrum nova. 

Настройка :

1. В ```config.py``` меняем значения переменных :
- CHAIN = сеть с которой работаем ( NOVA | ARBITRUM | OPTIMISM )
- FROM_AMOUNT = от какого кол-ва eth свапать
- TO_AMOUNT = до какого кол-ва eth свапать
- RM_AMOUNT = кол-во цифр после точки
- SLEEP_FROM = sleep от (в секундах) между swap и следующим кошельком
- SLEEP_TO = sleep до (в секундах) между swap и следующим кошельком
- FROM_COIN = от какого кол-ва монет покупать (дефолт 1)
- TO_COIN = до какого кол-ва покупапать (>= 1)
- RM_WALLETS = True если нужно рандомизировать кошельки, False если не нужно
- COINS = сюда можно добавить монеты, нужно указать address и symbol монеты, я уже добавил несколько, для обычного прогрева хватит

2. В файл ```private_keys.txt``` добавляем приватники от кошельков. Пустых строк быть не должно.
3. Запускаем файл ```run.py```

I'm = админ паблика https://t.me/hodlmodeth, отправитель редких гемов в [[ chat ]](http://t.me/chathodlmodeth) и главный, но не самый умный кодер чата [[ code ]](https://t.me/code_hodlmodeth) . Все вопросы по кодингу туда.

Donate (eth / bsc / arbitrum / op) : 0xb7415DB78c886c67DBfB25D3Eb7fcd496dAf9021
