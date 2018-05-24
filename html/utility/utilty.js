function SplitAndValidateParagraph(paragraph) {
    const split = paragraph.split('.')
    const validSplit = split.filter(s => s !== "");
    return validSplit.map(s => s + '.')
}