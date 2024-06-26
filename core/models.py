from django.contrib.auth.models import User
from django.db import models
from autoslug import AutoSlugField
from unidecode import unidecode


# модели для сайта
class News(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержание")
    date = models.DateTimeField(auto_now_add=True, verbose_name="Дата")
    image = models.ImageField(upload_to='news_images/', verbose_name="Изображение",null=True, blank=True)
    theme = models.CharField(max_length=200, verbose_name="Тема", null=True, blank=True)
    slug = AutoSlugField(
        populate_from="slugify_function", unique=True, always_update=True, default=" "
    )

    def slugify_function(self):
        return unidecode(self.title)
    
    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

    def __str__(self):
        return self.title


# учёные звания
class AcademicTitle(models.Model):
    title = models.CharField(max_length=255, verbose_name="Учёное звание/степень")
    
    class Meta:
        verbose_name = "Учёное звание"
        verbose_name_plural = "Учёные звания"

    def __str__(self):
        return self.title


# должности
class Position(models.Model):
    title = models.CharField(max_length=255, verbose_name="Должность")
    
    class Meta:
        verbose_name = "Должность"
        verbose_name_plural = "Должности"

    def __str__(self):
        return self.title


# пользователи
class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(verbose_name="Email", unique=True)  # Добавляем поле email
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    first_name = models.CharField(max_length=150, verbose_name="Имя")
    last_name = models.CharField(max_length=150, verbose_name="Фамилия")
    middle_name = models.CharField(max_length=150, verbose_name="Отчество", blank=True)
    
    photo = models.ImageField(
        upload_to="person_photos/", verbose_name="Фотография", null=True, blank=True
    )
    
    positions = models.ManyToManyField(Position, blank=True)
    academic_titles = models.ManyToManyField(
        AcademicTitle, blank=True
    )
    bio = models.TextField(verbose_name="Биография", blank=True)
    departments = models.ManyToManyField(
        "Department", blank=True
    )
    
    class Meta:
        verbose_name = "Пользователь сайта"
        verbose_name_plural = "Пользователи сайта"

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.middle_name}"


# кафедры
class Department(models.Model):
    name = models.CharField(max_length=255, default="", verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    address = models.CharField(max_length=255, default="", verbose_name="Адрес")
    phone = models.CharField(max_length=20, default="", verbose_name="Телефон")
    email = models.EmailField(default="", verbose_name="Email")
    head = models.ForeignKey(
        "Person",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="head_of_department",
        verbose_name="Заведующий",
    )
    members = models.ManyToManyField(
        Person, related_name="department_members", blank=True
    )
    
    class Meta:
        verbose_name = "Кафедра"
        verbose_name_plural = "Кафедры"

    def __str__(self):
        return self.name


# ученый совет
class AcademicCouncil(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    members = models.ManyToManyField(
        Person, related_name="council_members", blank=True, verbose_name="Участники"
    )
    
    class Meta:
        verbose_name = "Ученый совет"
        verbose_name_plural = "Ученый совет"

    def __str__(self):
        return self.name


class Presentation(models.Model):
    event = models.ForeignKey(
        "Event",
        on_delete=models.CASCADE,
        related_name="presentations",
        verbose_name="Мероприятие",
    )
    title = models.CharField(max_length=200, verbose_name="Заголовок презентации")
    file = models.FileField(upload_to="presentations/", verbose_name="Файл презентации")
    
    class Meta:
        verbose_name = "Презентация"
        verbose_name_plural = "Презентации"

    def __str__(self):
        return self.title


# мероприятия
class Event(models.Model):
    name = models.CharField(max_length=200, verbose_name="Заголовок")
    date = models.DateTimeField(verbose_name="Дата")
    place = models.CharField(max_length=255, verbose_name="Место проведения")
    url_conf = models.URLField(verbose_name="Сайт конференции", null=True, blank=True)
    url_speakers = models.URLField(
        verbose_name="Ссылка на докладчиков", null=True, blank=True
    )
    description = models.TextField(verbose_name="Описание мероприятия")
    registration_email = models.EmailField(
        verbose_name="Email для регистрации", null=True, blank=True
    )
    registration_url = models.URLField(
        verbose_name="Ссылка на регистрацию", null=True, blank=True
    )
    sections = models.TextField(
        verbose_name="Секции конференции", null=True, blank=True
    )
    organizer_contacts = models.TextField(
        verbose_name="Контактная информация организаторов", null=True, blank=True
    )
    program_committee = models.TextField(
        verbose_name="Программный комитет", null=True, blank=True
    )
    organizing_committee = models.TextField(
        verbose_name="Оргкомитет", null=True, blank=True
    )
    secretariat = models.TextField(verbose_name="Секретариат", null=True, blank=True)
    speakers = models.ManyToManyField("Person", verbose_name="Докладчики", blank=True)
    
    class Meta:
        verbose_name = "Мероприятие"
        verbose_name_plural = "Мероприятия"

    def __str__(self):
        return self.name


# мероприятия на страницы студенческая жизнь
class StudentLifeEvent(models.Model):
    name = models.CharField(max_length=200, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Содержание")
    date = models.DateTimeField(verbose_name="Дата")
    image = models.ImageField(upload_to='event_images/', verbose_name="Изображение",null=True, blank=True)
    
    class Meta:
        verbose_name = "Мероприятие студенческой жизни"
        verbose_name_plural = "Мероприятия студенческой жизни"

    def __str__(self):
        return self.name


# проекты
class Project(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    head = models.ForeignKey(
        "Person",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="project_head",
        verbose_name="Руководитель проекта",
    )
    participants = models.ManyToManyField(
        Person, related_name="project_participants", blank=True, verbose_name="Участники"
    )
    date = models.DateTimeField(verbose_name="Дата")
    
    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"

    def __str__(self):
        return self.name


# партнеры
class Partner(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    photo = models.ImageField(upload_to="partner_photos", blank=True, null=True, verbose_name="Изображение")
    url = models.URLField(verbose_name="Ссылка")
    
    class Meta:
        verbose_name = "Партнер"
        verbose_name_plural = "Партнеры"

    def __str__(self):
        return self.name


class YouthDivision(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название отдела")
    head = models.ForeignKey(
        "Person",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="youth_division_head",
        verbose_name="Руководитель отдела",
    )
    activities = models.TextField(verbose_name="Деятельность")

    def activities_list(self):
        return self.activities.split('\n')
    
    class Meta:
        verbose_name = "Молодежный отдел"
        verbose_name_plural = "Молодежные отделы"

    def __str__(self):
        return self.name


class Speciality(models.Model):
    BACHELOR = 'B'
    MASTER = 'M'
    POSTGRADUATE = 'P'

    EDUCATION_LEVEL_CHOICES = [
        (BACHELOR, 'Бакалавриат'),
        (MASTER, 'Магистратура'),
        (POSTGRADUATE, 'Аспирантура'),
    ]

    name = models.CharField(max_length=255, verbose_name="Название специальности")
    duration = models.CharField(max_length=50, verbose_name="Срок обучения")
    cost = models.CharField(max_length=100, verbose_name="Стоимость обучения")
    exams = models.TextField(verbose_name="Экзамены")
    budget_places = models.PositiveIntegerField(verbose_name="Количество бюджетных мест")
    paid_places = models.CharField(max_length=4, verbose_name="Количество платных мест")
    career = models.TextField(verbose_name="Карьера")
    description = models.TextField(verbose_name="Описание специальности", default="")
    education_level = models.CharField(
        max_length=1,
        choices=EDUCATION_LEVEL_CHOICES,
        default=BACHELOR,
        verbose_name="Уровень образования"
    )
    
    class Meta:
        verbose_name = "Специальность"
        verbose_name_plural = "Специальности"

    def __str__(self):
        return self.name


class Schedule(models.Model):
    EDUCATION_LEVEL_CHOICES = [
        ("B", "Бакалавриат"),
        ("M", "Магистратура"),
        ("S", "ГИА"),  # ГИА может быть представлено как 'S'
    ]

    ASSESSMENT_TYPE_CHOICES = [
        ("exam", "Экзамен"),
        ("credit", "Зачет"),
    ]

    FORM_CHOICES = [
        ("FT", "Очная"),
        ("PT", "Заочная"),
        ("FT_PT", "Очно-заочная"),
    ]

    TYPE_CHOICES = [
        ("interim", "Промежуточная аттестация"),
        ("retake", "Пересдача"),
    ]

    education_level = models.CharField(
        max_length=1,
        choices=EDUCATION_LEVEL_CHOICES,
        verbose_name="Уровень образования",
    )

    assessment_type = models.CharField(
        max_length=10,
        choices=ASSESSMENT_TYPE_CHOICES,
        verbose_name="Тип проведения",
    )

    form = models.CharField(
        max_length=5, choices=FORM_CHOICES, verbose_name="Форма обучения"
    )
    schedule_type = models.CharField(
        max_length=10, choices=TYPE_CHOICES, verbose_name="Тип расписания"
    )
    group = models.CharField(max_length=100, verbose_name="Группа")
    course = models.PositiveIntegerField(verbose_name="Курс")
    subject = models.CharField(max_length=255, verbose_name="Название предмета")
    date = models.DateField(verbose_name="Дата")
    semester = models.PositiveIntegerField(verbose_name="Семестр")
    teacher = models.ForeignKey("Person",
        on_delete=models.SET_NULL,
        null=True,
        blank=True, verbose_name="Преподаватель")
    place = models.CharField(max_length=255, verbose_name="Место проведения")

    def __str__(self):
        return f"{self.subject} - {self.group} - {self.date}"

    class Meta:
        ordering = ['course']
        verbose_name = "Расписание ПА/ПЕРЕСДАЧ"
        verbose_name_plural = "Расписания ПА/ПЕРЕСДАЧ"


class AdditionalEducationProgram(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название программы")
    program_director = models.ForeignKey("Person",
        on_delete=models.SET_NULL,
        null=True,
        blank=True, verbose_name="Руководитель программы"
    )
    duration = models.CharField(max_length=100, verbose_name="Сроки проведения")
    program_type = models.CharField(max_length=100, verbose_name="Вид программы")
    form_of_education = models.CharField(
        max_length=100, verbose_name="Форма проведения"
    )
    cost = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Стоимость обучения"
    )
    details = models.TextField(verbose_name="Описание")
    application_link = models.URLField(verbose_name="Ссылка на подачу заявки")
    contact_info = models.CharField(
        max_length=100, verbose_name="Контактная информация"
    )
    
    class Meta:
        verbose_name = "Дополнительное образование"
        verbose_name_plural = "Дополнительное образование"

    def __str__(self):
        return self.title


class Announcement(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержание")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создано")

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"

    def __str__(self):
        return self.title


class Course(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    code = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"

    def __str__(self):
        return self.name


class Student(models.Model):
    person = models.OneToOneField("Person", on_delete=models.CASCADE)
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name="students"
    )

    class Meta:
        verbose_name = "Студент"
        verbose_name_plural = "Студенты"

    def __str__(self):
        return self.name


class Competency(models.Model):
    name = models.CharField(max_length=512)
    code = models.CharField(max_length=50)
    slug = AutoSlugField(
        populate_from="slugify_function", unique=True, always_update=True, blank=True
    )

    def slugify_function(self):
        return unidecode(self.code)

    def __str__(self):
        return f"{self.code} - {self.name}"


class ParentDiscipline(models.Model):

    code = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name="parent_disciplines"
    )

    def __str__(self):
        return f"{self.code} - {self.description}"


class Discipline(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=50)
    parent_discipline = models.ForeignKey(
        ParentDiscipline, on_delete=models.CASCADE, related_name="disciplines"
    )
    competencies = models.ManyToManyField(Competency, related_name="disciplines")
    slug = AutoSlugField(
        populate_from="slugify_function", unique=True, always_update=True, blank=True
    )

    def slugify_function(self):
        return unidecode(self.code)

    def __str__(self):
        return self.name
