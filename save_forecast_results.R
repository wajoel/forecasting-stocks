# save_forecast_results.R
save_forecast_results <- function(forecast, file_name) {
  write.csv(forecast, file_name, row.names = FALSE)
  message("Forecast results saved to ", file_name)
}
