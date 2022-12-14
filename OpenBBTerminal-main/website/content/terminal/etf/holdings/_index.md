```
usage: holdings [-l LIMIT] [-h] [--export {csv,json,xlsx}]
```

See what is inside an ETF holdings.

```
optional arguments:
  -l LIMIT, --limit LIMIT
                        Number of holdings to get (default: 10)
  -h, --help            show this help message (default: False)
  --export {csv,json,xlsx}
                        Export raw data into csv, json, xlsx (default: )
```

Example:
```
2022 Oct 27, 08:21 (๐ฆ) /etf/ $ holdings

                           ETF Holdings                           
โโโโโโโโโณโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโณโโโโโโโโโโโณโโโโโโโโโโโโ
โ       โ Name                            โ % Of Etf โ Shares    โ
โกโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโฉ
โ AAPL  โ Apple Inc.                      โ 7.06%    โ 169672324 โ
โโโโโโโโโผโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโผโโโโโโโโโโโผโโโโโโโโโโโโค
โ MSFT  โ Microsoft Corporation           โ 5.74%    โ 83765412  โ
โโโโโโโโโผโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโผโโโโโโโโโโโผโโโโโโโโโโโโค
โ AMZN  โ Amazon.com, Inc.                โ 3.28%    โ 99548898  โ
โโโโโโโโโผโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโผโโโโโโโโโโโผโโโโโโโโโโโโค
โ GOOGL โ Alphabet, Inc.                  โ 1.92%    โ 67345732  โ
โโโโโโโโโผโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโผโโโโโโโโโโโผโโโโโโโโโโโโค
โ TSLA  โ Tesla, Inc.                     โ 1.82%    โ 29915424  โ
โโโโโโโโโผโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโผโโโโโโโโโโโผโโโโโโโโโโโโค
โ GOOG  โ Alphabet, Inc.                  โ 1.73%    โ 60222505  โ
โโโโโโโโโผโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโผโโโโโโโโโโโผโโโโโโโโโโโโค
โ BRK.B โ Berkshire Hathaway Inc.         โ 1.60%    โ 20277701  โ
โโโโโโโโโผโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโผโโโโโโโโโโโผโโโโโโโโโโโโค
โ UNH   โ UnitedHealth Group Incorporated โ 1.55%    โ 10505922  โ
โโโโโโโโโผโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโผโโโโโโโโโโโผโโโโโโโโโโโโค
โ JNJ   โ Johnson & Johnson               โ 1.38%    โ 29530061  โ
โโโโโโโโโผโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโผโโโโโโโโโโโผโโโโโโโโโโโโค
โ XOM   โ Exxon Mobil Corporation         โ 1.35%    โ 46810082  โ
โโโโโโโโโดโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโดโโโโโโโโโโโดโโโโโโโโโโโโ
```

