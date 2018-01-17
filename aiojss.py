# pylint: disable=invalid-name,redefined-builtin
import asyncio
import aiohttp

from etree import ElementTree


class JSS(object):
    def __init__(self, url, username, password):
        self.url = url
        self.username = username
        self.password = password
        self.auth = aiohttp.BasicAuth(username, password)
        self.session = aiohttp.ClientSession(loop=asyncio.get_event_loop())

    def __del__(self):
        self.session.close()

    async def _get_endpoint(self, endpoint, id=None, name=None):
        base_url = self.url + f'/JSSResource/{endpoint}'
        if id:
            url = base_url + f'/id/{id}'
            async with self.session.get(url, auth=self.auth) as resp:
                assert resp.status == 200
                return JSSObject(await resp.text())
        elif name:
            url = base_url + f'/name/{name}'
            async with self.session.get(url, auth=self.auth) as resp:
                assert resp.status == 200
                return JSSObject(await resp.text())
        else:
            async with self.session.get(base_url, auth=self.auth) as resp:
                assert resp.status == 200
                return JSSObject(await resp.text())

    async def scripts(self, id=None, name=None):
        return await self._get_endpoint('scripts', id, name)

    async def computer_extension_attributes(self, id=None, name=None):
        return await self._get_endpoint('computerextensionattributes', id, name)


class JSSObject(object):
    def __init__(self, xml):
        self._root = ElementTree.fromstring(xml)
        self.base_url = None

    def __getattr__(self, name):
        return self._root.__getattr__(name)

    def save(self):
        raise NotImplementedError

    def delete(self):
        raise NotImplementedError

    def raw_xml(self):
        return ElementTree.tostring(self._root)
