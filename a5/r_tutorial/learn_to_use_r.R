rm(list = ls(envir = globalenv()), envir = globalenv()); if(!is.null(dev.list())) dev.off(); gc(); cat("\014")

setwd("C:/work/lis4369/a5/r_tutorial")

pdf(file="C:/work/lis4369/a5/r_tutorial/myplotfile.pdf")

library("quantmod")
getSymbols("AAPL")

barChart(AAPL)
barChart(AAPL, subset='last 14 days')
chartSeries(AAPL, subset='last 14 days')
barChart(AAPL['2013-04-1::2013-04-12'])
barChart(AAPL['2013-04-1::'])
barChart(AAPL['2020'])


library("dplyr")

library("ggplot2")
qplot(disp, mpg, data=mtcars)
qplot(disp, mpg, ylim=c(0,35), data=mtcars)
qplot(cty, hwy, data=mpg)
qplot(cty, hwy, data=mpg, geom="jitter")
ggplot(mtcars, aes(x=disp, y=mpg)) + geom_point()
ggplot(mtcars, aes(x=disp, y=mpg)) + geom_line()
ggplot(pressure, aes(x=temperature, y=pressure)) + geom_line()


ggplot(pressure, aes(x=temperature, y=pressure), ylim = 400) + geom_line()

ggplot(pressure, aes(x=temperature, y=pressure)) + geom_line() + geom_point()

barplot(BOD$demand)
barplot(BOD$demand, main="graph of demand")
barplot(BOD$demand, main="graph of demand", names.arg = BOD$time)
cylcount <- table(mtcars$cyl)

barplot(cylcount)

qplot(mtcars$cyl, bins=30)

qplot(factor(mtcars$cyl))
ggplot(mtcars, aes(factor(cyl))) + geom_bar()
boxplot(mtcars$mpg)

rainbow(5)
heat.colors(5)
terrain.colors(5)
topo.colors(5)
cm.colors(5)

mycolors <- rainbow(3)
mycolors2 <- heat.colors(3)
ggplot(mtcars, aes(x=factor(cyl))) + geom_bar(fill=mycolors)
ggplot(mtcars, aes(x=factor(cyl))) + geom_bar(fill=rainbow(3))
barplot(BOD$demand, col = rainbow(6))
barplot(BOD$demand, col = "royalblue3")

testscores <- c(96,71,85,92,82,78,81,68,61,78,86,90)
barplot(testscores)
barplot(testscores, col="blue")

testcolors <- ifelse(testscores >= 80, "blue", "red")
barplot(testscores, col=testcolors)

barplot(testscores, col=testcolors, main="Test scores")
barplot(testscores, col=testcolors, main="Test scores", ylim=c(0,100))
barplot(testscores, col=testcolors, main="Test scores", ylim=c(0,100), las=1)

testscores <- sort(c(96,71,85,92,82,78,81,68,61,78,86,90), decreasing = TRUE)
barplot(testscores, col=testcolors, main="Test scores descending")

qplot(factor(cyl), data=mtcars, geom="bar", fill=factor(cyl))

x <- 11
print(x)

dev.off

png(filename = "cylinder_count.png")
barplot(cylcount)
dev.off

png(filename = "cylinder_count2.png",width = 800, height = 600, units = "px", pointsize = 12, bg = "#ccccff")
barplot(cylcount)
dev.off


png(filename = "cylinder_count3.png",width = 800, height = 600, units = "px", pointsize = 12, bg = "azure")
barplot(cylcount)
dev.off

save.image()
