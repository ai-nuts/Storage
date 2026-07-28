import glob, os, asyncio
from playwright.async_api import async_playwright
DECK=os.environ["DECK"]
svgs=sorted(glob.glob(os.path.join(DECK,"svg_final","*.svg")))
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch()
        pg=await b.new_page(viewport={"width":1920,"height":1080})
        for s in svgs:
            await pg.goto("file://"+s)
            out=os.path.join(DECK,"preview",os.path.basename(s).replace(".svg",".png"))
            await pg.screenshot(path=out,clip={"x":0,"y":0,"width":1920,"height":1080})
            print("raster",os.path.basename(out))
        await b.close()
asyncio.run(main())
