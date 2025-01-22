# preprocess_stock_data.R
preprocess_stock_data <- function(data) {
  data <- na.omit(data)
  data <- data[order(data$Date), ]
  return(data)
}
