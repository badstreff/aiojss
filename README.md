# aiojss
asyncio  python wrapper for the Jamf JSS Rest API - with a prettier syntax


Note that this project is still in super early beta and it's main purpose
will likely be to just server as a way for git2jss to more cleanly talk
to the jss, but it is being developed here because others *may* find it
useful.


Modified etree that allows working with xml objects in a nicer way,
the main thing is that elements and text can now be referenced with python
dot notation. This causes issues if you need to change attributes but
I haven't ran into needing to do this with the jss.



So far only working with scripts and extension attributes are supported.



Example of how to list all the scripts in the jss.

```
#!/usr/bin/env python
import asyncio
import uvloop
import aiojss

async def main():
    jss = aiojss.JSS('https://your-jss:8443', 'username', 'password')
    scripts = await jss.scripts()
    print(scripts.raw_xml())
    for script in scripts.script:
        print(script.name)


if __name__ == '__main__':
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
```
