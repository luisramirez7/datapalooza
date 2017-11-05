df <- read.csv("~/Projects/datapalooza/cleanhybriddata/hybriddataset.csv")
nrow(df)
lmodel <- lm(formula = Yield.Rate ~ First.Allele + Second.Allele, data = df)
summary(lmodel)
