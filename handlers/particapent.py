from aiogram import types, Dispatcher
from create_bot import dp, bot
from crypto_market import api_market
from keyboards import kb_particapent
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

# @dp.message_handler(commands=['start', 'help'])
async def command_start(message : types.Message):
    try:
        await bot.send_message( message.from_user.id, 
                                'Хай. Чем я могу помочь? Вот не мгое, что я умею', 
                                reply_markup=kb_particapent
                                )

        await message.delete()
    except:
        await message.reply( ' По правилам боты не могут писать первые\nНапиши мне в ЛС,\n @assistiant_crypto_bot')



async def get_20pairs(message : types.Message):
    pairs20 = await api_market.fetch_20pairs()
    await bot.send_message(message.from_user.id, pairs20)
    await message.delete()

class FSMCost(StatesGroup):
    price = State()


# @dp.message_handler(commands=['fetch_priсe'], state=None)
async def fetch_priсе(message : types.Message):
    await FSMCost.price.set()
    await bot.send_message(message.from_user.id, 'Укажите инетресующую пару\nнапример: BTCUSDT')

# @dp.message_handler(content_types=['text'], state=FSMCost.price)
async def load_pair(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['price'] = message.text
        p = await api_market.fetch_pair_price(data['price'])
    await message.reply(p)

    await state.finish()



def register_handlers_particapent(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(fetch_priсе, commands=['fetch_price'])
    dp.register_message_handler(get_20pairs, commands=['pairs20'])
    dp.register_message_handler(load_pair, state=FSMCost.price)
