import asyncio
import random

async def cook_rice():
    await asyncio.sleep(1 + random.random())
    return 'ข้าวผัด (rice)'

async def cook_noodle():
    await asyncio.sleep(1 + random.random())
    return 'ก๋วยเตี๋ยว (noodle)'

async def cook_curry():
    await asyncio.sleep(1 + random.random())
    return 'ข้าวแกง (curry)'

async def main():
    # สร้าง task objects
    tasks = [
        asyncio.create_task(cook_rice()),
        asyncio.create_task(cook_noodle()),
        asyncio.create_task(cook_curry())
    ]

    # รอจนกว่าจะมี task ใดเสร็จสมบูรณ์
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)

    # แสดงผล task ที่เสร็จสมบูรณ์
    for task in done:
        print(f'นักศึกษา A ได้รับอาหาร: {task.result()}')

    # ยกเลิก tasks ที่เหลือ
    for task in pending:
        task.cancel()

# เรียกใช้ main() โดยใช้ asyncio.run()
asyncio.run(main())


