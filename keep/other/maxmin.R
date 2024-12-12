out <- c("fizz", "buzz", "bazz")
nums <- c(3,5,7)

x <- 17


fizzbuzz <- \(n) {
  strings <- c("fizz", "buzz", "bazz")
  numbers <- c(3,5,7)
  modulos <- n %% numbers == 0
  paste0(strrep(n, !sum(modulos)), strings[modulos], collapse = "")
}


maxmin < \(n) {
  digits <- as.numeric(strsplit(as.character(n), "")[[1]])

  min_value <- min(digits)
  min_last_index <- length(digits) + 1 - which.min(rev(digits))
  not_min_first_index <- which.min(digits == min_value)
  if(not_min_first_index < min_last_index) {
    digits[min_last_index] = digits[not_min_first_index]
    digits[not_min_first_index] = min_value
  }

}
