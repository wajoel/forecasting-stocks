# plot_stock_prices.R
plot_stock_prices <- function(data) {
  library(ggplot2)
  ggplot(data, aes(x = Date, y = Price)) +
    geom_line(color = "blue") +
    labs(title = "Historical Stock Prices", x = "Date", y = "Price") +
    theme_minimal()
}
