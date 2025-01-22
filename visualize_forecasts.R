# visualize_forecasts.R
visualize_forecasts <- function(data, forecast, title = "Forecast vs Actual") {
  library(ggplot2)
  forecast_dates <- seq.Date(max(data$Date) + 1, by = "day", length.out = length(forecast$mean))
  forecast_df <- data.frame(Date = forecast_dates, Forecast = as.numeric(forecast$mean))
  
  ggplot() +
    geom_line(data = data, aes(x = Date, y = Price), color = "blue") +
    geom_line(data = forecast_df, aes(x = Date, y = Forecast), color = "red") +
    labs(title = title, x = "Date", y = "Price") +
    theme_minimal()
}
