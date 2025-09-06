## Breakout Strategy Project

In this project, you will implement the breakout strategy. You'll find and remove any outliers. You'll test to see if it has the potential to be profitable using a Histogram and P-Value. For the dataset, we'll be using the end of day from Quotemedia.

# Project: Breakout Strategy

## Generate Signal

| Criteria                               | Submission Requirements                                                                                               |
| -------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| Compute the Highs and Lows in a Window | The function `get_high_lows_lookback` computes the maximum and minimum of the closing prices over a window of days.   |
| Compute Long and Short Signals         | The function `get_long_short` computes long and short signals using a breakout strategy.                              |
| Filter Signals                         | The function `filter_signals` filters out repeated long or short signals.                                             |
| Lookahead Close Prices                 | The function `get_lookahead_prices` gets the close price days ahead in time.                                          |
| Lookahead Price Returns                | The function `get_return_lookahead` generates the log price return between the closing price and the lookahead price. |
| Compute the Signal Return              | The function `get_signal_return` generates the signal returns.                                                        |

## Evaluate Signal

|Criteria|Submission Requirements|
|---|---|
|Histogram|Correctly answers the question “What do the histograms tell you about the signal returns?"|

## Outliers

| Criteria                | Submission Requirements                                            |
| ----------------------- | ------------------------------------------------------------------ |
| Kolmogorov-Smirnov Test | The function `calculate_kstest` calculates the ks and p values.    |
| Find Outliers           | The function `find_outliers` returns the list of outlying symbols. |