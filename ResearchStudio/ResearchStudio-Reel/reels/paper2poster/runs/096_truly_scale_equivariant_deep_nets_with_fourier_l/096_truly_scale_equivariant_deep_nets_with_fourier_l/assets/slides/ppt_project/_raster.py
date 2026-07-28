import asyncio, glob, os
from playwright.async_api import async_playwright
async def main():
    svgs=sorted(glob.glob("svg_output/*.svg"))
    async with async_playwright() as p:
        b=await p.chromium.launch()
        pg=await b.new_page(viewport={"width":1280,"height":720},device_scale_factor=1)
        for s in svgs:
            uri="file://"+os.path.abspath(s)
            await pg.goto(uri)
            await pg.wait_for_timeout(120)
            out="_preview/"+os.path.basename(s).replace(".svg",".png")
            await pg.screenshot(path=out,clip={"x":0,"y":0,"width":1280,"height":720})
            print("rendered",out)
        await b.close()
asyncio.run(main())
