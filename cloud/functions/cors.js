exports.PreflightResponse = function (req, res) {
    res.set("Access-Control-Allow-Origin", "*");
    // res.set("Access-Control-Allow-Methods", "GET, POST");
    // res.set("Access-Control-Allow-Methods", "POST");
    res.set("Access-Control-Allow-Headers", "Content-Type");
    // res.set("Access-Control-Max-Age", "3600");
    res.set('Access-Control-Allow-Headers', 'X-Requested-With')
    res.set('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
    res.set('Access-Control-Max-Age', '86400')
    if (req.method == 'OPTIONS') {
        res.status(204).send('');
    }
}