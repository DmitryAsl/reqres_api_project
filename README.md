<h2 align="center"> Тестовый проект API автотестов на reqres.in </h2>  


### Используемый стек
<p>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original-wordmark.svg" height=50 weight=50 />  
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/pytest/pytest-original-wordmark.svg" height=50 weight=50 />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/jenkins/jenkins-original.svg" height=50 weight=50 />
  <img src="https://avatars.githubusercontent.com/u/5879127?s=200&v=4" height=50 weight=50 />
  <img src="https://github.com/DmitryAsl/reqres_api_project/blob/master/data/pictures/Telegram.svg" height=50 weight=50 />
</p>        

### Автоматизированные кейсы
1. Регистрация нового пользователя
2. Регистрация пользователя без данных (негативный)
3. Получение данных пользователя
4. Создание пользователя
5. Обновление данных пользователя
6. Удаление пользователя
7. Получение данных по несуществующему пользователю (негативный)

<details>
<summary><h3> Запуск тестов с помощью Jenkins </h3><img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/jenkins/jenkins-original.svg" height=30 weight=30 /></summary> 

  > **Перейти в [сборку](https://jenkins.autotests.cloud/job/dmitry_asl_reqres_api_project/)**  
  > **Нажать на кнопку "Build Now"**  
  <p>
  <img src="https://github.com/DmitryAsl/reqres_api_project/blob/master/data/pictures/jenkins_build.png" />
  </p> 

  > Результаты запуска находятся в левом углу, последний запуск  
  <img src="https://github.com/DmitryAsl/reqres_api_project/blob/master/data/pictures/jenkins_builds_allurepng.png" />
</details>
<details>
<summary><h3> Запуск тестов локально </h3></summary>  

  1. Склонировать репозиторий
  2. Открыть проект в PyCharm
  3. Ввести в терминале следующие команды
     - если Poetry ещё **не установлен**, сначала установите его:  
    ```
    pip install poetry  
    ```
  > Основные команды по настройке проекта и запуска тестов  
  ```
  poetry install --no-root
  poetry shell
  pytest tests
  ```
**Если локально установлен Allure можно посмотреть отчет, для этого выполняем**
  ```
  allure serve allure-results
  ```

</details>

### Отчет о результатах в Allure <img src="https://avatars.githubusercontent.com/u/5879127?s=200&v=4" height=30 weight=30 />
> В качестве системы отчетности выбран **Allure Report**  
> Для перехода в отчет, в Jenkins в левом углу нажать на иконку на Вашем запуске
>> Запуск отображается упавшим, т.к. присутствует упавший тест, который является багом в продукте   
  <img src="https://github.com/DmitryAsl/reqres_api_project/blob/master/data/pictures/jenkins_builds_allurepng.png" />
  
> В открывшемся окне представлена общая информация по тестам  
>> Для подробной информации переходим на вкладку **Suits** и раскрываем все тесты для наглядности  
>>> При нажатии на конкретный тест справа отображается подробная информация по нему.  
>>> В каждом тесте присутствуют логи всех запросов и ответов.
 <img src="https://github.com/DmitryAsl/reqres_api_project/blob/master/data/pictures/allure_full_info.png" />

### Отправка оповещения прохождения тестов в Telegram <img src="https://github.com/DmitryAsl/qa_guru_hw_14_Samokat/blob/main/data/icons/Telegram.svg" height=30 weight=30 />

> Автоматически настроена отправка оповещения о результатах прохождения тестов в чат **Telegram** с тегом ответственных людей.  
> В оповещении присутствует общая информация о запуске и ссылка на отчет в **Allure**.  
<img src="https://github.com/DmitryAsl/reqres_api_project/blob/master/data/pictures/notifications_tg.png" />

#### Для вопросов и предложений можно связаться в [telegram](https://t.me/Dmitry_Asl) 
