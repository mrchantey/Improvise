
def DoRecursive(item, func):
    func(item)
    if item['type'] == 'collection':
        for subItem in item['items']:
            DoRecursive(subItem, func)


def RecursiveFlatten(item):
    items = [item]
    if item['type'] == 'collection':
        for subItem in item['items']:
            items += RecursiveFlatten(subItem)
    return items
