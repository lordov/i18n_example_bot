For internationalization

Сбор всех текстов из вашего проекта .pot
1. pybabel extract --input-dirs=. -o locales/messages.pot

Для компиляции текущих локалей файлов .po -> .mo
2. pybabel compile -d locales -D i18n_example_bot
