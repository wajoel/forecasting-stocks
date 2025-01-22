# forecast_ets.R
forecast_ets <- function(model, h = 30) {
  forecasted <- forecast(model, h = h)
  return(forecasted)
}
