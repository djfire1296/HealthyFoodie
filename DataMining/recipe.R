require(gdata)
library(dplyr)
ingre <- read.csv("ingre.csv")
df <- read_csv("腎臟食譜final.csv")

a <- unlist(strsplit(df$成分,"\\|"))
b <- strsplit(a,":") %>% sapply("[",1)
b
unique(b)

c <- b[!b %in% ingre$樣品名稱]
unique(c)


ingre$俗名 <- as.character(ingre$俗名)
ingre4 <- ingre
ingre4$樣品名稱 <- paste(ingre4$樣品名稱,ingre4$俗名,ingre4$X,sep=",")
ingre4$樣品名稱 <- strsplit(ingre4$樣品名稱,",")
#d[!d %in% unlist(ingre4$樣品名稱)]
library(tidyr)
ingre5 <- unnest(ingre4,樣品名稱)
ingre6 <- ingre5 %>% select(樣品名稱, 粗蛋白.成分值.g., 粗脂肪.成分值.g.,總碳水化合物.成分值.g. ,修正熱量.成分值.kcal.)
ingre7<- ingre6 %>% filter(!樣品名稱=="")

#d[!d %in% unlist(ingre7$樣品名稱)]

#grep(".雞蛋.*",ingre7$樣品名稱)

ingre2 <- ingre %>% select(-樣品名稱)
names(ingre2)[3]<-"樣品名稱"
ingre2<- ingre2 %>% filter(樣品名稱!= "")
ingre3 <- ingre2


ingre3$樣品名稱 <- strsplit(ingre3$樣品名稱,",")
sapply(ingre3$樣品名稱, paste, collapse = ",")





#
df <- read.csv("腎臟食譜final.csv")
df$成分 <- gsub("\\(","=",df$成分)
df$成分 <- gsub(" g)","",df$成分)
df$成分 <- gsub("\\)","",df$成分)
df$成分 <- gsub(" \\|","|",df$成分)
df <- df %>% select(-X)

write.csv(df,"腎臟食譜final.csv",row.names = FALSE)




