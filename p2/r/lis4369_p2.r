rm(list = ls(envir = globalenv()), envir = globalenv()); if(!is.null(dev.list())) dev.off(); gc(); cat("\014")
setwd("C:/work/lis4369/p2/r")
file.remove('lis4369_p2_output.txt')
file.remove("plot_1.png")
file.remove("plot_2.png")
sink("lis4369_p2_output.txt", append=FALSE, split=TRUE)

text <- c("1) Display all data from file:",
          "2) Display 1st 10 records:",
          "3) Display last 10 records:",
          "4) Display file structure (see notes above):",
          "5) Display column names (see notes above):",
          "6) Display 1st record/row with column names (see notes above):",
          "7) Display 2nd column data (mpg), using column number:",
          "8) Display column data (cyl), using column name:",
          "9) Display row/column data (3,4), that is, one field, using square bracket notation (see above):",
          "10) Display all data for cars having greater than 4 cylinders:",
          "11) Display all cars having more than 4 cylinders *and* greater than 5 gears:",
          "12) Display all cars having more than 4 cylinders *and* exactly 4 gears:",
          "13) Display all cars having more than 4 cylinders *or* exactly 4 gears:",
          "14) Display all cars having more than 4 cylinders that do *not* have 4 gears:",
          "15) Display total number of rows (only the number):",
          "16) Display total number of columns (only the number):",
          "17) Display total number of dimensions (i.e., rows and columns):",
          "18) Display data frame structure - same as info in Python:",
          "19) Get mean, median, minimum, maximum, quantiles, variance, and standard deviation of horsepower:",
          "20) summary() prints min, max, mean, median, and quantiles (also, number of NA's, if any.):")

cat("###################################################\n",
    "R Language Reference Notes:\n",
    "\tUse head and tail to look at first few and last few records.\n",
    "\tUse str and names to look at structure and column names of a data frame.\n",
    "\tUse $ notation to look at a particular column name.\n",
    "\tUse [] square brakcets (row, column) notation to look at a particular value.\n\n",
    "\tAlso, conditional section in R:\n",
    "\tSelect data in I row and J column (one field) for DataFrameX: DataFrame[I,J]\n",
    "\tAlternatively:\n",
    "\tData in I row: DataFrameX[I,] # display row/record I with column names\n",
    "\tData in J column: DataFrameX$J_Column_Name, or DataFrameX[,J]\n",
    "\tNOTE: R uses 1 for first record/row. Python uses 0!",
    "\n\n")

cat("*** Assignment Requirements ***\n\n",
    "1. Use Assignment 5 screenshots and R Manual to backward-engineer the following requirements:\n",
    "2. Resources:\n",
    "\ta. R Manual: https://cran.r-project.org/doc/manuals/r-release/R-lang.pdf\n",
    "\tb. R for Data Science: https://r4ds.had.co.nz/\n",
    "3. Use Motor Trend Car Road Tests data:\n",
    "\ta. Research the data! https://stat.ethz.ch/R-manual/R-devel/library/datasets/html/mtcars.html\n",
    "\tb. url = \"http://vincentarelbundock.github.io/Rdatasets/csv/datasets/mtcars.csv\"\n",
    "Note: Use variable \"cars\" to read file into. (See Assignment 5 for reading .csv files.\n",
    "###################################################\n\n") 

url = "http://vincentarelbundock.github.io/Rdatasets/csv/datasets/mtcars.csv"
cars <- read.csv(file=url,head=TRUE,sep=",")

cat(text[1],"\n")
cars
cat("\n")

cat(text[2],"\n")
head(cars,10)
cat("\n")

cat(text[3],"\n")
tail(cars,10)
cat("\n")

cat(text[4],"\n")
str(cars)
cat("\n")

cat(text[5],"\n")
names(cars)
cat("\n")

cat(text[6],"\n")
cars[1,]
cat("\n")

cat(text[7],"\n")
cars[2,]
cat("\n")

cat(text[8],"\n")
cars$cyl
cat("\n")

cat(text[9],"\n")
cars[3,4]
cat("\n")

cat(text[10],"\n")
cars[cars$cyl>4,]
cat("\n")

cat(text[11],"\n")
cars[cars$cyl>4 &cars$gear>4,]
cat("\n")

cat(text[12],"\n")
cars[cars$cyl>4 &cars$gear==4,]
cat("\n")

cat(text[13],"\n")
cars[cars$cyl>4 |cars$gear==4,]
cat("\n")

cat(text[14],"\n")
cars[cars$cyl>4 &cars$gear!=4,]
cat("\n")

cat(text[15],"\n")
nrow(cars)
cat("\n")

cat(text[16],"\n")
ncol(cars)
cat("\n")

cat(text[17],"\n")
dim(mtcars)
cat("\n")

cat(text[18],"\n")
str(cars)
cat("\n")

cat(text[19],"\n")
cat("\t","a. Mean: ")
mean(cars$hp, na.rm=TRUE)
cat("\t", "b. Median: ")
median(cars$hp, na.rm=TRUE)
cat("\t", "c. Min: ")
min(cars$hp, na.rm=TRUE)
cat("\t", "d. Max: ")
max(cars$hp, na.rm=TRUE)
cat("\t", "e. Quantile:\n")
quantile(cars$hp, na.rm=TRUE)
cat("\t", "f. Variance: ")
var(cars$hp, na.rm=TRUE)
cat("\t", "g. Standard Deviation: ")
sd(cars$hp, na.rm=TRUE)
cat("\n")

cat(text[20],"\n")
summary(cars$hp, na.rm=TRUE)
cat("\n")

cat("Two plots (*must* include *your* name in title): 1) Uses qplot(); 2) Uses plot()\n")
library(ggplot2)

cat("\t1) Uses qplot()")
png(file="plot_1.png")
qplot(disp, mpg, data=cars, color=cyl, xlab="Displacement", ylab="MPG", main="Aliya Gamez - Displacement and MPG")
dev.off()

cat("\t2) Uses plot()")
png(file="plot_2.png")
plot(cars$wt, cars$mpg, xlab="Weight in Thousands", ylab="MPG",main="Aliya Gamez - Weight and MPG")
dev.off()

#close all connections
sink.reset <- function(){
  for(i in seq_len(sink.number())){
    sink(NULL)
  }
}

closeAllConnections()
sink.reset