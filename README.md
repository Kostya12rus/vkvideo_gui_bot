# VK Video GUI Bot

Бот для управления подписками на стримеров VK Video с графическим интерфейсом на Flet.

## Структура проекта

```
src/
├── models/           # Модели базы данных (Peewee)
│   ├── account.py
│   ├── streamer.py
│   ├── settings.py
│   ├── subscription.py
│   └── __init__.py
├── utils/            # Утилиты
│   ├── callbackmanager.py
│   ├── logger.py
│   ├── decorators.py
│   └── __init__.py
├── api/              # API клиенты
│   └── vkvideo/
│       ├── api.py
│       └── __init__.py
├── ui/               # Интерфейс Flet
│   ├── app.py
│   └── __init__.py
├── data/             # Данные (база данных)
├── config.py         # Конфигурация
└── main.py           # Точка входа
```

## Установка

1. Убедитесь, что установлен Python 3.13 и pipenv:
   ```bash
   pip install pipenv
   ```

2. Установите зависимости:
   ```bash
   pipenv install
   ```

3. Активируйте виртуальное окружение:
   ```bash
   pipenv shell
   ```

## Запуск

```bash
python src/main.py
```

## Зависимости

- **flet** - GUI фреймворк
- **peewee** - ORM для базы данных
- **requests** - HTTP клиент
- **seleniumbase** - для автоматизации (уже есть)

## Модели базы данных

- **Account** - аккаунты пользователей VK
- **Streamer** - стримеры VK Video
- **Subscription** - подписки аккаунтов на стримеров
- **Settings** - настройки интерфейса для каждого аккаунта

## Разработка

### Добавление нового функционала

1. Модели данных: `src/models/`
2. Утилиты: `src/utils/`
3. API клиенты: `src/api/`
4. Интерфейс: `src/ui/`

### Логирование

Используйте логгер из `src.utils.logger`:

```python
from src.utils.logger import logger

logger.info("Сообщение")
logger.error("Ошибка")
```

### Декораторы

Доступные декораторы в `src.utils.decorators`:

- `@log_execution` - логирование выполнения функции
- `@retry(max_attempts=3)` - повтор при ошибке