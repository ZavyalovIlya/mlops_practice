### Результаты выполнения лабораторной №4  
В результате выполнения работы настроено удаленное хранилище файлов на Google Drive для версионирования датасета (titanic). 
Также написаны python скрипты для модифицирования датасета. Отслеживание изменений в результате выполнения этих скриптов отслеживается с помощью настроенного dvc.  
[Ссылка на Google Drive](https://drive.google.com/drive/folders/1PgGJSRQ5RTsqnv7dpKz0MdnLx7TTpRgN?usp=sharing) с репозиторием версионирования датасета.  

#### Переключение между версиями
1. Изначальная версия датасета (с отобранными признаками Pclass, Sex, Age)
```
git checkout de594374e8ebfc12df5c1b2fc723fbfbec563059
dvc pull
```
2. Заполнение пустых значений поля Age средним
```
git checkout 9472ce4514ed471396ec7e11c6b01ca2e138e81a
dvc pull
```
3. Версия с one-hot-encoded полем Sex
```
git checkout 27f9d27362051678a838f82b808adc95c33dfd44
dvc pull
```
4. Дополнительное преобразование
```
git checkout c9d82c4bc6d58106bd841db0d51f16c017ef100b
dvc pull
```
