import asyncio
async def make_greeting(name):
  return f"Hello {name}"

async def main():
  for name in ["paula", "thomas", "lewis"]:
    a = await make_greeting(name)
    print(a)
asyncio.run(main())
# The event loop is a waiter who takes multiple orders, delivers them to kitchen, then serves whoever is ready first — never just standing and waiting