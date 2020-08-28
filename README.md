child_allowance
===
system for keeping track of my 3 kid's allowances & expenses.


## usage

create Tony and give him 40 bux to start his life:
```shell
$ python child_allowance.py --create Tony 40

csv:
childname;transaction_id;transaction_date;transaction_amount;new_amount;description
Tony;1;2020-04-06 19:50:04;40;40;creation of record
```

give Tony some money for a good job done:
```shell
$ python child_allowance.py Tony 5 "weekend child labor"

csv:
childname;transaction_id;transaction_date;transaction_amount;new_amount;description
Tony;1;2020-04-06 19:50:04;40;40;creation of record
Tony;2;2020-04-20 16:20:56;5;45;weekend child labor
```

Tony wants to spend some money on candy:
```shell
$ python child_allowance.py Tony -15 "expensive candy"

csv:
childname;transaction_id;transaction_date;transaction_amount;new_amount;description
Tony;1;2020-04-06 19:50:04;40;40;creation of record
Tony;2;2020-04-20 16:20:56;5;45;weekend child labor
Tony;3;2020-08-25 10:20:03;-15;30;expensive candy
```

Just check the current status of Tony's savings:
```shell
$ python child_allowance.py --info Tony

output:
current: ['Tony', '3', '2020-08-25 10:20:03', '-15', '30', 'expensive candy']
```

## TODO

* automatically add amount for each period child receives allowance (cron)
    - I.E. automatically add €2 every sunday on the week kid is here
* change name to "child_economy" or similar since it includes more than just allowance
