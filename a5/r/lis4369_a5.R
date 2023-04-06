a <-9
a
a+5

b<-sqrt(a)
b

c<- c(1,2.5,3,6,-2,4)
print(c)


typeof(c)
is.list(c)
is.vector(c)

d <- c("one","two","three")
d

typeof(d)

e <- c(TRUE,TRUE,TRUE,FALSE,TRUE,FALSE)
e
typeof(e)

d[1]

my_str <- "Hello World!"
my_str

typeof(my_str)

sqrt(a)
sqrt(c)

a^2
c^2


min(c)
max(c)
mean(c)
sum(c)

url ="https://raw.githubusercontent.com/vincentarelbundock/Rdatasets/master/csv/Stat2Data/Titanic.csv"
titanic <- read.csv(file=url,head=TRUE,sep=",")

titanic
summary(titanic)

dir()
getwd()

names(titanic)

titanic$Name 
titanic$Age 

attributes(titanic)
ls()

mean(titanic$Age)

mean(titanic$Age, na.rm =TRUE)
median(titanic$Age, na.rm =TRUE)
quantile(titanic$Age, na.rm =TRUE)
min(titanic$Age, na.rm =TRUE)
max(titanic$Age, na.rm =TRUE)
var(titanic$Age, na.rm =TRUE)
sd(titanic$Age, na.rm =TRUE)

summary(titanic$Age, na.rm=TRUE)

titanic[!complete.cases(titanic),]

titanic_no_missing_data <- na.omit(titanic)
titanic_no_missing_data 

help(stripchart)

pdf(file="C:/Users/17862/lis4369/a5/myplotfile.pdf")
stripchart(titanic_no_missing_data$Age)

boxplot(titanic_no_missing_data$Age)

dev.off()

boxplot(titanic_no_missing_data$Age,
        main='Distribution of Titanic Passenger Ages',
        xlab ='Ages',
        horizontal=TRUE)

plot(titanic_no_missing_data$Age,titanic_no_missing_data$Survived,
    main="Relationship Between Ages and Survival",
    xlab="Age",
    ylab="Survived")