# Project Description

[Lesson](https://learn.udacity.com/nd880?version=4.2.1&partKey=cd0569&lessonKey=73fb1eb0-fea4-46ad-95a7-73ff311bcf57&conceptKey=ba111b20-90e9-41bc-946b-647d4c40496d&tab=lesson)[Downloads](https://learn.udacity.com/nd880?version=4.2.1&partKey=cd0569&lessonKey=73fb1eb0-fea4-46ad-95a7-73ff311bcf57&conceptKey=ba111b20-90e9-41bc-946b-647d4c40496d&tab=resources)

## Smart Beta and Portfolio Optimization

In this project, you will build a smart beta portfolio and compare it to a benchmark index. To find out how well the smart beta portfolio did, you’ll calculate the tracking error against the index. You’ll then build a portfolio by using quadratic programming to optimize the weights. Your code will rebalance this portfolio and calculate turn over to evaluate the performance. You’ll use this metric to find the optimal rebalancing Frequency. For the dataset, we'll be using the end of day from Quotemedia.

# Rubric

Use this project rubric to understand and assess the project criteria.

## Part 1: Smart Beta Portfolio

|Criteria|Submission Requirements|
|---|---|
|Compute Index Weights|The function `generate_dollar_volume_weights` computes dollar volume weights.|
|Compute ETF Weights|The function `calculate_dividend_weights` computes dividend weights.|
|Compute Returns|The function `generate_returns` computes returns.|
|Compute Weighted Returns|The function `generate_weighted_returns` computes weighted returns.|
|Compute Cumulative Returns|The function `calculate_cumulative_returns` computes cumulative returns.|
|Compute Tracking Error|The function `tracking_error` computes tracking error.|

## Part 2: Portfolio Optimization

|Criteria|Submission Requirements|
|---|---|
|Compute Covariance|The function `get_covariance_returns` computes covariance of the returns.|
|Compute Optimal Weights using Quadratic Programming|The function `get_optimal_weights` computes optimal weights.|
|Rebalance Portfolio|The function `rebalance_portfolio` computes weights for each rebalancing of the portfolio.|
|Calculate Portfolio Turnover|The function `get_portfolio_turnover` computes cost of all the rebalancing.|