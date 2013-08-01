#!/usr/bin/env Rscript

if (!('socrata' %in% ls())) {
  socrata <- (function() {
    d <- read.csv('socrata.csv', stringsAsFactors = T)
  
    # Characters
    for (key in c('description', 'name', 'id', 'tags')) {
      d[,key] <- as.character(d[,key])
    }
  
    # Dates
    for (key in c('createdAt', 'publicationDate', 'viewLastModified', 'rowsUpdatedAt')) {
      d[,key] <- as.POSIXct(d[,key], origin = '1970-01-01')
      d[,paste(key,'day',sep='.')] <- as.Date(d[,key])
    }
  
    d
  })()
}

library(ggplot2)
library(scales)
p.1 <- ggplot(socrata) + aes(x = portal) + geom_bar() + coord_flip() + scale_y_log10('Number of datasets', labels = comma)
p.2 <- ggplot(socrata) + aes(x = createdAt.day, group = portal, fill = portal) +
  geom_bar(binwidth = 30) + scale_x_date('Month') + scale_y_continuous('Datasets uploaded per month')

png('socrata1.png', width = 1600, height = 1200, res = 200) 
print(p.1)
dev.off()
png('socrata2.png', width = 1600, height = 1600, res = 200) 
print(p.2)
dev.off()


# subset(socrata, nrow > 100000)
