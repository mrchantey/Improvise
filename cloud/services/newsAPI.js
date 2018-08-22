const fs = require('fs')
const axios = require('axios')

const baseUrl = "https://newsapi.org/v2/top-headlines"
const country = "au"
const apiKey = fs.readFileSync(__dirname + '/keys/newsAPIKey.txt')

const category = 'entertainment'
// business entertainment general health science sports technology
const url = `${baseUrl}?country=${country}&apiKey=${apiKey}&category=${category}`
exports.requestNewsConversational = function () {
    return new Promise((resolve, reject) => {
        exports.requestNews()
            .then(data => {
                const maxResults = 3
                const max = maxResults > 19 ? 19 : maxResults
                const allTitles = data.articles.map(a => a.title)
                const titles = allTitles.slice(0, max)
                const headlines = titles.join(".\n")
                const phrase = `Here are the News headlines this hour.\n${headlines}`
                resolve(phrase)
            })
            .catch(err => {
                console.error(err)
                reject(err)
            })
    });
}


exports.requestNews = function () {
    return new Promise((resolve, reject) => {
        axios.get(url)
            .then((result) => {
                resolve(result.data)
            }).catch((err) => {
                console.error(err);
                reject(err)
            });
    })
}

if (require.main === module) {
    // exports.requestNews()
    exports.requestNewsConversational()
        .then(res => console.log(res))
        .catch(val => console.error(val))
}

// #         headlines = map(lambda art: art['title'], newsData['articles'])
// #         intro = "Here are todays news headlines." if category == '' else"Here are todays news headlines in {0}.".format(category)
// #         return {"headlines": [intro] + headlines[:maxResults]}

// #     def RequestHeadlinesFromParameters(self, parameters):
// #         urlParams = ''
// #         category = ''
// #         if 'news-category' in parameters:
// #             category = parameters['news-category']
// #             urlParams += '&category=' + category
// #         return self.RequestHeadlines(5, urlParams, category)

// #     def RequestHeadlines(self, maxResults=10, urlParams='', category=''):
// #         newsData = utility.GetJson(url + urlParams)
