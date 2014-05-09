mongoexport -d ptt_crawler_db -c ptt_article -f title,url,user_id,time -o short_ptt_article.json
tar cfz short_ptt_article.tar.gz short_ptt_article.json
rm short_ptt_article.json
