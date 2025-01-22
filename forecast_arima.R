# forecast_arima.R
forecast_arima <- function(model, h = 30) {
  forecasted <- forecast(model, h = h)
  return(forecasted)
}
