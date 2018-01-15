import etree.ElementTree as ET


data = '''<?xml version="1.0"?>
<data>
    <country name="Liechtenstein">
        <rank>1</rank>
        <year>2008</year>
        <gdppc>141100</gdppc>
        <neighbor name="Austria" direction="E"/>
        <neighbor name="Switzerland" direction="W"/>
    </country>
    <country name="Singapore">
        <rank>4</rank>
        <year>2011</year>
        <gdppc>59900</gdppc>
        <neighbor name="Malaysia" direction="N"/>
    </country>
    <country name="Panama">
        <rank>68</rank>
        <year>2011</year>
        <gdppc>13600</gdppc>
        <neighbor name="Costa Rica" direction="W"/>
        <neighbor name="Colombia" direction="E"/>
    </country>
</data>
'''


class XMLObject(object):

    def __init__(self, root):
        self._root = root

    def _bfs(self, root):
        # pylint: disable=invalid-name
        l = []
        d = {}
        for child in root:
            if not child:
                d[child.tag] = child.text
            else:
                l.append({child.tag: self._bfs(child)})
        if d:
            return d
        return l


if __name__ == '__main__':
    ROOT = ET.fromstring(data)
    print(type(ROOT))
    print(ROOT.country)
