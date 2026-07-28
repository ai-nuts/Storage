import os, glob, asyncio
from playwright.async_api import async_playwright
HERE=os.path.dirname(os.path.abspath(__file__))
SRC=os.path.join(HERE,"svg_output"); OUT=os.path.join(HERE,"_preview"); os.makedirs(OUT,exist_ok=True)
async def main():
    async with async_playwright() as p:
        br=await p.chromium.launch()
        pg=await br.new_page(viewport={"width":1280,"height":720},device_scale_factor=2)
        for f in sorted(glob.glob(os.path.join(SRC,"*.svg"))):
            await pg.goto("file://"+f)
            png=os.path.join(OUT,os.path.basename(f).replace(".svg",".png"))
            await pg.screenshot(path=png,clip={"x":0,"y":0,"width":1280,"height":720})
            print("rastered",os.path.basename(png))
        await br.close()
asyncio.run(main())
