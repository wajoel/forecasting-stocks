# fit_ets_model.R
fit_ets_model <- function(data) {
  library(forecast)
  ts_data <- ts(data$Price, frequency = 252)
  ets_model <- ets(ts_data)
  return(ets_model)
}
