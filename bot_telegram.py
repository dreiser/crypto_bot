from aiogram.utils import executor
from create_bot import dp


async def on_startup(_):
    print('bot online')

from handlers import particapent, admin, other

particapent.register_handlers_particapent(dp)
other.register_handlers_other(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)

    
