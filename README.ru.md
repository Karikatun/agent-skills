# Agent Skills

Навыки для coding-агентов: каждый решает конкретную задачу и устанавливается отдельно.

[English](README.md)

## Доступные навыки

| Навык | Версия | Для чего |
| --- | --- | --- |
| [API Performance Review](skills/api-performance-review/README.md) | 1.0.2 | Проверить стоимость запросов, масштабирование, повторы, кэш и поведение при сбоях; отделить дефекты от нехватки данных |
| [Learn from Task](skills/learn-from-task/README.md) | 1.0.0 | Извлечь полезные уроки из завершённой задачи и предложить, где их закрепить, прежде чем что-либо записывать |
| [Documentation Update](skills/documentation-update/README.md) | 1.0.0 | Сверить документацию с реализацией и исправить неподтверждённые обещания |
| [Humanize Russian Text](skills/humanize-russian-text/README.md) | 1.0.0 | Сделать русский текст естественным, сохранив факты, условия и тон |

Инструкции написаны на английском; ответы — на языке пользователя. Навыки не зависят друг от друга, не требуют MCP-серверов, API-ключей, пакетов или отдельных подписок помимо выбранного агента. Необязательные проверочные скрипты используют Python 3.9+ и стандартную библиотеку.

## Установить один навык

### Скачать только выбранный навык

Выбери один архив в таблице. В каждом ZIP лежит папка одного навыка. Git и клонирование репозитория не нужны.

| Навык | Архив | Проверка целостности |
| --- | --- | --- |
| API Performance Review 1.0.2 | [Скачать ZIP](https://github.com/Karikatun/agent-skills/releases/download/api-performance-review-v1.0.2/api-performance-review-1.0.2.zip) | [SHA-256](https://github.com/Karikatun/agent-skills/releases/download/api-performance-review-v1.0.2/api-performance-review-1.0.2.zip.sha256) |
| Learn from Task 1.0.0 | [Скачать ZIP](https://github.com/Karikatun/agent-skills/releases/download/learn-from-task-v1.0.0/learn-from-task-1.0.0.zip) | [SHA-256](https://github.com/Karikatun/agent-skills/releases/download/learn-from-task-v1.0.0/learn-from-task-1.0.0.zip.sha256) |
| Documentation Update 1.0.0 | [Скачать ZIP](https://github.com/Karikatun/agent-skills/releases/download/documentation-update-v1.0.0/documentation-update-1.0.0.zip) | [SHA-256](https://github.com/Karikatun/agent-skills/releases/download/documentation-update-v1.0.0/documentation-update-1.0.0.zip.sha256) |
| Humanize Russian Text 1.0.0 | [Скачать ZIP](https://github.com/Karikatun/agent-skills/releases/download/humanize-russian-text-v1.0.0/humanize-russian-text-1.0.0.zip) | [SHA-256](https://github.com/Karikatun/agent-skills/releases/download/humanize-russian-text-v1.0.0/humanize-russian-text-1.0.0.zip.sha256) |

1. Скачай выбранный ZIP и файл контрольной суммы в одну папку.
2. Перед распаковкой проверь контрольную сумму. В macOS выполни подходящую команду из этой папки:

   ```sh
   shasum -a 256 -c api-performance-review-1.0.2.zip.sha256
   ```

   ```sh
   shasum -a 256 -c learn-from-task-1.0.0.zip.sha256
   ```

   В Linux используй `sha256sum -c` с тем же именем файла контрольной суммы. В Windows выполни в PowerShell `Get-FileHash .\api-performance-review-1.0.2.zip -Algorithm SHA256` (или укажи ZIP второго навыка) и сравни хеш с текстом в соответствующем файле `.sha256`.
3. Распакуй ZIP и прочитай `README.md` и `SKILL.md` навыка.
4. Скопируй распакованную папку со всем содержимым в каталог навыков своего агента. Для ручной личной установки в Codex документация указывает `$HOME/.agents/skills`; в Windows — `.agents/skills` внутри профиля пользователя. Если родительского каталога ещё нет, создай его.

Например, после установки API Performance Review должен появиться файл:

```text
~/.agents/skills/api-performance-review/SKILL.md
```

Если папка этого навыка уже существует, сравни версии и сохрани свои изменения перед заменой именно этой папки. Резервные копии не должны оставаться в каталоге, который агент сканирует. Другие навыки устанавливать не требуется.

### Попросить Codex установить один навык

Если в твоём Codex доступен встроенный `$skill-installer`, отправь ему **один** из этих запросов. Это текст для Codex, а не команда терминала:

```text
Используй $skill-installer: установи только api-performance-review из https://github.com/Karikatun/agent-skills/tree/api-performance-review-v1.0.2/skills/api-performance-review в мой личный каталог навыков. Сохрани существующую копию, если она есть; другие навыки не устанавливай.
```

```text
Используй $skill-installer: установи только learn-from-task из https://github.com/Karikatun/agent-skills/tree/learn-from-task-v1.0.0/skills/learn-from-task в мой личный каталог навыков. Сохрани существующую копию, если она есть; другие навыки не устанавливай.
```

Ссылки ведут на фиксированные теги выпусков. Установщик выбирает поддерживаемый личный каталог и сообщает путь; некоторые версии используют `$CODEX_HOME/skills` (обычно `~/.codex/skills`). Используй указанный им путь и не создавай дубликат в другом каталоге.

Устанавливается только выбранный навык. Установщик может временно скачать архив исходников репозитория; если нужны только файлы одного навыка, используй ZIP из таблицы выше. Собственного установщика и автоматического обновления у коллекции нет.

### Вызвать установленный навык

```text
Используй $api-performance-review: проверь GET /orders. Код пока не меняй.
```

```text
Используй $learn-from-task: разбери завершённую задачу и предложи полезные уроки. Пока ничего не записывай.
```

Если агент не увидел установленный навык, перезапусти клиент. [Документация OpenAI](https://learn.chatgpt.com/docs/build-skills), проверенная 10 сентября 2026 года, описывает локальные каталоги навыков и установку из других репозиториев. OpenAI рекомендует плагины для распространения; эта коллекция пока содержит отдельные папки и архивы. Публикация в каталоге плагинов и установка во всех агентах не заявлены.

## Что проверено

Методики не привязаны к языку приложения или фреймворку. Совместимость с агентом — отдельный вопрос: проверка формата Codex и ограниченные прогоны не доказывают работу во всех клиентах и ОС.

- [API-review](evaluations/api-performance-review/VALIDATION.md): искусственные примеры, исполняемые проверки фактов и ограничения. Предыдущее сравнение не показало преимущества над агентом без навыка.
- [Извлечение уроков](evaluations/learn-from-task/VALIDATION.md): предложение изменений, отсутствие полезного урока, уже одобренное изменение и недоверенный входной текст.
- [Documentation Update](evaluations/documentation-update/VALIDATION.md): проверенные примеры и ограничения.
- [Humanize Russian Text](evaluations/humanize-russian-text/VALIDATION.md): проверенные примеры и ограничения.
- [Границы безопасности](SECURITY.md): доступ, происхождение, объём проверки и оставшиеся ограничения. Инструкция навыка не создаёт песочницу.

Локальная проверка состава пакетов и семи API-примеров:

```sh
python3 -B scripts/check.py
```

Команда проверяет структуру и факты в примерах. Она не запускает агента и не доказывает качество его решений. Порядок проверки с агентом описан рядом с примерами.

## Развитие

Правила изменений — в [CONTRIBUTING.md](CONTRIBUTING.md). У каждого навыка своя версия и архив. Проектные команды, правила, пути и примеры остаются в проектах-потребителях; соседние репозитории не нужны для работы навыков.

Оригинальные материалы доступны под [MIT](LICENSE). У API-навыка сохранено исходное уведомление об авторских правах. Внешние стандарты и другие источники сохраняют свои условия; ссылка на них не меняет их лицензию.
