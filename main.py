from entity.Curier import Curier
from entity.Request import Request
from entity.Shop import Shop
from entity.Store import Store

shop = Shop(items={"печенька": 5, "ноутбук": 10})

store = Store(items={"печенька": 7, "ноутбук": 10})

storages = {'магазин': shop, 'склад': store}


def main():
    while True:
        print("Добрый день!")
        for item in storages:
            print(f"В {item} хранится {storages[item].get_items()}")

        user_input = input("Введите запрос на перемещение в формате: 'Доставить 3 печенька из склад в магазин' \n"
                           "Введите 'stop' или 'стоп', чтобы остановиться \n",
                           )
        if user_input in ('stop', 'стоп'):
            break

        request = Request(storages, user_input)

        curier = Curier(request, storages)
        curier.move()


if __name__ == '__main__':
    main()
