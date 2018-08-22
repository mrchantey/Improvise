





exports.RequestTimeConversational = function () {
    return new Promise((resolve, reject) => {
        const date = new Date()
        const phrase = `The time is now ${date.getHours()}.${date.getMinutes}`
        resolve(phrase)
    })

}