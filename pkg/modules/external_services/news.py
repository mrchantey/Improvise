# from pkg.utilities import utility

# baseUrl = "https://newsapi.org/v2/top-headlines"
# country = "au"
# apiKey = utility.OpenJson('pkg/keys/newsAPIKey.json')['key']
# url = "{0}?country={1}&apiKey={2}".format(baseUrl, country, apiKey)


# class News():
#     def __init__(self):
#         pass

#     def OnRequest(self, requestBody):
#         return self.RequestHeadlines()

#     def RequestHeadlinesFromParameters(self, parameters):
#         urlParams = ''
#         category = ''
#         if 'news-category' in parameters:
#             category = parameters['news-category']
#             urlParams += '&category=' + category
#         return self.RequestHeadlines(5, urlParams, category)

#     def RequestHeadlines(self, maxResults=10, urlParams='', category=''):
#         newsData = utility.GetJson(url + urlParams)
#         headlines = map(lambda art: art['title'], newsData['articles'])
#         intro = "Here are todays news headlines." if category == '' else"Here are todays news headlines in {0}.".format(category)
#         return {"headlines": [intro] + headlines[:maxResults]}


# if __name__ == "__main__":
#     news = News()
#     response = news.OnRequest({})
#     print response
