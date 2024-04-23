# For internationalization

*Сбор всех текстов из вашего проекта .pot*  
  
pybabel extract --input-dirs=. -o locales/messages.pot 
 
*Для компиляции текущих локалей файлов .po -> .mo*   
  
pybabel compile -d locales -D i18n_example_bot
