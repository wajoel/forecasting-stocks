# fit_arima_model.R
fit_arima_model <- function(data) {
  library(forecast)
  ts_data <- ts(data$Price, frequency = 252) # Assuming daily data
  arima_model <- auto.arima(ts_data)
  return(arima_model)
}
