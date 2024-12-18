x <- mtcars$mpg
y <- mtcars$disp

plot(x,y, bty = "l", axes = FALSE)
axis(side = 2, tick = TRUE,las = 1)
