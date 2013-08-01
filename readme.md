Generate music from Socrata portals
====

I'd like to use the meta-dataset, but here are some other possibilities.

https://data.baltimorecity.gov/Government/Minority-and-Women-s-Business-Enterprises-Certific/us2p-bijb?
https://data.illinois.gov/Environment/IEPA-Leaking-Underground-Storage-Tank-Incident/2kz4-t22j?

I came across these with this query.

    subset(socrata,
      ncol > 20 & nrow > 1000 & ncol < 70 & ncol.date >= 2 &
      !grepl('Campaign',name) & displayType=='table'
    )[c('portal','id','name','viewCount')]
