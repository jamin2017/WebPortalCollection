'''
Created on 2017年11月5日

@author: SunYawei
'''
import math
from numpy.lib.financial import rate

# 相关新闻推荐,保存到数据库中
# news_to_tags：key:string newsID ; value:[tag1,tag2,...]
# news_to_rates: key:string newsID ; value:int rate
# userNews：该用户今日看过的新闻，[newsID1,newsID2,...]
def recommendSimilarNews(newsID,news_to_tags,news_to_rates):
    tmpTags = news_to_tags[newsID]
    recommendNews = {}
    for news in news_to_tags:
        num = 0
        for tag in news_to_tags[news]:
            if tag in tmpTags:
                num += 1
        if num>0 and news!=newsID:
            score = num + 0.001*news_to_rates[news]
            recommendNews[news] = score
    recommendNews = sorted(recommendNews.items(), key = lambda x:x[1] , reverse=True)
    recommendList = []
    relatedNews = ""
    # 推荐新闻条数
    count = 0
    for news in recommendNews:
        recommendList.append(news[0]) 
        relatedNews = relatedNews + news[0] + '\t'
        count += 1
        if count>=20:
            break
    #返回相关新闻ID集合字符串
    return relatedNews


news_to_rates = {"1":23}
news_to_tags = {"1":['iphone','手机']}
newsID = "100651304"
recommendList,txt = recommendSimilarNews(newsID, news_to_tags, news_to_rates) 
