mongoexport -d ptt_crawler_db -c ptt_article_push -f url,userid,datetime -o short_ptt_article_push.json
tar cfz short_ptt_article_push.tar.gz short_ptt_article_push.json
rm short_ptt_article_push.json
