def get_prop(node,name):
    """
    Return the property in the title of a node
    """
    title = node.get('title')
    props = title.split(';')
    for prop in props:
        (key,args) = prop.split(None,1)
        if key==name: return args

def get_text(node):
    """
    Return the text content of a node
    """
    textnodes = node.xpath(".//text()")
    s = string.join([text for text in textnodes])
    return re.sub(r'\s+',' ',s)

def get_bbox(node, normalize=1):
    """
    Get the bbox values of a node
    """
    bbox = get_prop(node,'bbox')
    if not bbox: return None
    return tuple([int(x) / normalize * normalize for x in bbox.split()])


