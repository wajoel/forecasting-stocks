# simulate_stock_data.R
simulate_stock_data <- function(days = 365, start_price = 100) {
  set.seed(123)
  returns <- rnorm(days, mean = 0.0005, sd = 0.02)
  prices <- cumprod(1 + returns) * start_price
  dates <- seq.Date(Sys.Date() - days, Sys.Date(), by = "days")
  stock_data <- data.frame(Date = dates, Price = prices)
  return(stock_data)
}
