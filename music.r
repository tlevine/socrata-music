#!/usr/bin/env Rscript

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


p.1 <- ggplot(socrata) + aes(x = portal) + geom_bar() + coord_flip()
p.2 <- ggplot(socrata) + aes(x = createdAt.day, group = portal, fill = portal) + geom_bar()

subset(socrata, nrow > 100000)
