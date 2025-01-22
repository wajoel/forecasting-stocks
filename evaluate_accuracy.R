# evaluate_forecast.R
evaluate_forecast <- function(actual, predicted) {
  rmse <- sqrt(mean((actual - predicted)^2))
  mae <- mean(abs(actual - predicted))
  return(list(RMSE = rmse, MAE = mae))
}
