child_allowance
===
system for keeping track of my 3 kid's allowances & expenses.


## usage

create Tony and give him 40 bux to start his life:
```bash
$ python child_allowance.py --create Tony 40

# csv => Tony;1;2020-04-06 19:50:04;40;40;creation of record
```

give Tony some money for a good job done:
```bash
$ python child_allowance.py Tony 5 "weekend child labor"

# csv => Tony;1;2020-04-20 16:20:56;5;45;weekend child labor
```

Tony wants to spend some money on candy:
```bash
$ python child_allowance.py Tony -15 "expensive candy"

# csv => Tony;1;2020-08-25 10:20:03;-15;30;expensive candy
```

### TODO

soon

* better command-line interface for adding transactions?

later

* automatically add amount for each period child receives allowance
