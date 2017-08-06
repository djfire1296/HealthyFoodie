hospital <- read.csv("機構資料.csv")
a <- hospital %>% filter(營養師>0) %>% select(機構名稱,縣市鄉鎮,地址,電話,營養師)
write.csv(a,"hospital.csv",row.names = F)

