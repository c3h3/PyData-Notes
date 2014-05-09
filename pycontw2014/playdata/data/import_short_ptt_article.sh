tar xfz short_ptt_article.tar.gz
mongoimport -d short_ptt_crawler_db -c ptt_article --file short_ptt_article.json
rm short_ptt_article.json

