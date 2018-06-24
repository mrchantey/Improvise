from pkg.utilservices import utility

baseUrl = "https://newsapi.org/v2/top-headlines"
country = "au"
apiKey = utility.OpenJson('pkg/keys/newsAPIKey.json')['key']
url = "{0}?country={1}&apiKey={2}".format(baseUrl, country, apiKey)


def RequestHeadlinesFromParameters(parameters):
    urlParams = ''
    category = ''
    if 'news-category' in parameters:
        category = parameters['news-category']
        urlParams += '&category=' + category
    return RequestHeadlines(10, urlParams, category)


def RequestHeadlines(maxResults=10, urlParams='', category=''):
    newsData = utility.GetJson(url + urlParams)
    headlines = map(lambda art: art['title'], newsData['articles'])
    intro = "Here are todays news headlines." if category == '' else"Here are todays news headlines in {0}.".format(category)
    return [intro] + headlines[:maxResults]


if __name__ == '__main__':
    headlines = RequestHeadlinesFromParameters({'news-category': 'sports'})
    for headline in headlines:
        print headline
