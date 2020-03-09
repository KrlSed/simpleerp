from django.db import models
from django.dispatch import receiver
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
#

class Ret():

    def get_items(self):
        return '; '.join([p.name_group + ' ' + p.item.name + ' Количество:' + str(p.count) for p in self.items.all()])
    get_items.short_description = 'Вещи'

    def get_issup(self):
        return "; \n".join([p.name_group for p in self.items_supplier.all()])
    get_issup.short_description = 'Вещи, доступные поставщику'

    def get_mesh(self):
        return (self.mesh.mesh + ' - ' + self.mesh.additional_mesh)
    get_mesh.short_description = 'Материал'

    def get_founders_company(self):
        return '\n,'.join([p.companyname for p in self.founderscompanyorganization.all()])
    get_founders_company.short_description = 'Основатели'

    def get_founders(self):
        return ",\n".join([p.founders for p in self.founders.all()])
    get_founders.short_description = 'Основатели'

    def get_founder(self):
        return ",\n".join([p.second_name + '\n' + p.first_name for p in self.founder.all()])
    get_founder.short_description = 'Основатели'

    def get_factories(self):
        return ",\n".join([p.holding for p in self.factories.all()])
    get_factories.short_description = 'Фабрики'

    def get_factory(self):
        return ",\n".join([p.name for p in self.factory.all()])
    get_factory.short_description = 'Фабрики'

    def get_offices(self):
        return ",\n".join([p.holding for p in self.offices.all()])
    get_offices.short_description = 'Офисы'
    
    def get_office(self):
        return ';\n'.join([p.name + ' Адрес=' + p.address.country + ', ' + p.address.city + ', ' + p.address.street + ', ' + p.address.bilding + '-' + p.address.flat for p in self.office.all()])
    get_office.short_description = 'Офисы'

    def get_storages(self):
        return ",\n".join([p.holding for p in self.storages.all()])
    get_storages.short_description = 'Склады'

    def get_storage(self):
        return ",\n".join([p.name for p in self.storage.all()])
    get_storage.short_description = 'Склады'    

    def get_role_now(self):
        return '; '.join([p.name + ' ' + p.countpeople + ' ' + p.needHE for p in self.role.all()])
    get_role_now.short_description = 'Роль'


    def get_orderes(self):
        return '; '.join(['Заказ доставлен: ' +  p.get_date.strftime("%m/%d/%Y")  for p in self.orderes.all()])
    get_orderes.short_description = 'Заказы'
   
    def get_delivery_variant(self):
        return ";\n".join([p.model_name + '-' + p.type_of_transport + " Цена=" + p.order_coast + ' Время=' + p.time_delivery + ' ' for p in self.delivery_transport.all()])
    get_delivery_variant.short_description = 'Варианты доставки'

    def get_orders(self):
        return ",\n".join([p.order_status + ' $=' + p.total_price for p in self.orderes.all()])
    get_orders.short_description = 'Заказы'



class Address(models.Model):
    choosetype = (('O', 'Офис'),
                  ('F','Фабрика'),
                  ('S', 'Склад'),
                  ('PH', 'Жилой дом'),
                  ('FH', 'Многоквартирный дом'),
                  ('EP', 'Рабочее место'),
                  ('LP', 'Жилое мест'),
    )
    country = models.CharField(max_length=100, verbose_name='Страна')
    city = models.CharField(max_length=100, verbose_name='Город')
    street = models.CharField(max_length=100, verbose_name='Улица')
    bilding = models.CharField(max_length=100, verbose_name='Здание')
    flat = models.CharField(max_length=100, verbose_name='Квартира или офис')
    type_org = models.CharField(max_length=10, choices=choosetype ,verbose_name='Тип организации')
    user = models.ForeignKey('UserCustom' , null=False, on_delete=models.PROTECT, related_name='User', verbose_name='Добавил пользователь')
    


    def __str__(self):
        return (self.country + ', ' + self.city + ', ' + self.street + ', ' + self.bilding + '-' + self.flat)

    

    class Meta:
        verbose_name_plural = 'Адрес'
        verbose_name = 'Адрес'
        ordering = ['-country']

class Firm(models.Model, Ret):
    name = models.CharField(max_length=100, verbose_name='Название')
    mobile = models.CharField(max_length=10, verbose_name='Телефон')
    director = models.CharField(max_length=100, verbose_name='Директор')
    mail = models.EmailField(verbose_name='Почта')
    connect_date_firm = models.DateTimeField(db_index=True, verbose_name='Дата начало сотрудничества')
    create_date_firm = models.DateTimeField(db_index=True, verbose_name='Дата создания')
    firm_is_supplier = models.BooleanField(verbose_name='Фирма это доставщик')
    info = models.TextField(null=True, blank=True, verbose_name='Описание')
    founderscompanyorganization = models.ManyToManyField('FoundersCompanyOrganization', related_name='Организаторы', verbose_name='Основатели')
    user = models.ForeignKey('UserCustom' , null=False, on_delete=models.PROTECT, related_name='User', verbose_name='Добавил пользователь')
    

    def __str__(self):
        return self.name   


    class Meta:
        verbose_name_plural = 'Фирма'
        verbose_name = 'Фирма'
        ordering = ['name']

class Founder(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    second_name = models.CharField(max_length=100, verbose_name='Фамилия')
    age = models.IntegerField(verbose_name='Возраст')
    namber = models.CharField(max_length=10, verbose_name='Телефон')
    mail = models.CharField(max_length=100, verbose_name='Почта')
    info = models.TextField(verbose_name='Информация')
    user = models.ForeignKey('UserCustom' , null=False, on_delete=models.PROTECT, related_name='User', verbose_name='Добавил пользователь')


    def __str__(self):
        return (self.first_name + ' ' + self.second_name)


    class Meta:
        verbose_name_plural = 'Основатель'
        verbose_name = 'Основатель'
        ordering = ['second_name']

class Mesh(models.Model):
    mesh = models.CharField(max_length=100, verbose_name='Материал')
    info_mesh = models.TextField(verbose_name='Информация о материале')
    additional_mesh = models.CharField(max_length=100, verbose_name='Название доп. материала')
    info_additional_mesh = models.TextField( verbose_name='Информация о доп. материале')
    user = models.ForeignKey('UserCustom' , null=False, on_delete=models.PROTECT, related_name='User', verbose_name='Добавил пользователь')


    def __str__(self):
        return self.mesh + ' - ' + self.additional_mesh
    
    class Meta:
        verbose_name_plural = 'Материал'
        verbose_name = 'Материал'
        ordering = ['mesh']

class Price(models.Model):
    price = models.CharField(max_length=100, verbose_name='Цена')
    sale_price = models.CharField(max_length=100, verbose_name='Цена со скидкой')
    user = models.ForeignKey('UserCustom' , null=False, on_delete=models.PROTECT, related_name='User', verbose_name='Добавил пользователь')


    def __str__(self):
        return self.price  

    class Meta:
        verbose_name_plural = 'Цена'
        verbose_name = 'Цена'
        ordering = ['price']


class OrderTable(models.Model, Ret): # Добавить поле выполнено или нет и названание заказа
    name = models.CharField(max_length=50, verbose_name='Название заказа')
    wornot = models.BooleanField(verbose_name='Доставлен')
    address = models.ForeignKey('Address' , null=False, on_delete=models.PROTECT, related_name='Адрес')
    items = models.ManyToManyField('Items', related_name='Вещи')
    create_date = models.DateTimeField(db_index=True, verbose_name='Дата создания')
    get_date = models.DateTimeField(db_index=True, verbose_name='Дата получения')
    user = models.ForeignKey('UserCustom' , null=False, on_delete=models.PROTECT, related_name='User', verbose_name='Добавил пользователь')


    def __str__(self):
        if self.wornot:
            return self.name + '(Доставлен: ' + self.get_date.strftime("%m/%d/%Y") + ')'
        else:
            return self.name + 'Не доставлен'
    

    class Meta:
        verbose_name_plural = 'Таблица заказа'
        verbose_name = 'Таблица заказа'
        ordering = ['address']



class RoleNow(models.Model, Ret):
    name = models.CharField(max_length=100, verbose_name='Название')
    countpeople = models.IntegerField(verbose_name='Количество людей в подчинении')  
    needHE = models.BooleanField(verbose_name='Необходимость высшего образования')
    user = models.ForeignKey('UserCustom' , null=False, on_delete=models.PROTECT, related_name='User', verbose_name='Добавил пользователь')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Должность'
        verbose_name = 'Должность'
        ordering = ['name']


class TotalRole(models.Model, Ret):
    name = models.CharField(max_length=100, verbose_name='Название')
    role_now = models.ForeignKey('RoleNow', related_name='Должность', verbose_name='Занимаемая должность', on_delete=models.CASCADE)
    user = models.ForeignKey('UserCustom' , null=False, on_delete=models.PROTECT, related_name='User', verbose_name='Добавил пользователь')


    class Meta:
        verbose_name_plural = 'Должность'
        verbose_name = 'Должность'
        ordering = []

    def __str__(self):
        return self.name


class UserCustomManager(BaseUserManager):

    def create_user(self, email, password1, password2, name, perm):
        if not email:
            raise ValueError('Email must be set!')
        if not (password1 == password2):
            raise ValueError('Passwords not =')
        user = self.model(email=email, name = name, perm = perm)
        user.set_password(password1)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, name, perm):
        user = self.model(email=email, name = name, perm = perm)
        user.set_password(password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class UserCustom(AbstractBaseUser, PermissionsMixin):

    ChoseRole = (('A', 'Бухгалтер'),
                 ('GA', 'Главный бухгалтер'),
                 ('D', 'Default'),
                 ('SM', 'Управляющий складом'),
                 ('GSM', 'Главный Управляющий складами'),
                 ('FM', 'Управляющий фабрикой'),
                 ('GFM', 'Главный управляющий фабриками'),
                 ('OM', 'Управляющий офисом'),
                 ('GOM', 'Главный управляющий офисами'),
                 ('FO', 'Основатель'),
                 ('CFO', 'Компания основателей'),
                 ('SM', 'Менеджер по безопасности'),
                 ('GSM', 'Главный мнеджер по безопасности'),
                 ('H', 'Помощник - контролер'),
                 ('S', 'Поставщик'),
                 ('F', 'Фирма'),
                 ('PM', 'Отдел кадров'),
                 ('GPM', 'Начальник отдела кадров'),
                 ('DIR', 'Директор'),
                 ('AAA', 'ADMIN')
    )
    perm = models.CharField(max_length=10, choices=ChoseRole, verbose_name='Должность')
    email = models.EmailField(unique=True, verbose_name='Почта')
    name = models.CharField(max_length=100, verbose_name='Логин')
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'perm']

    def __str__(self):
        return self.name + ' ' + self.email + '-' + self.perm

    
    
    def natural_key(self):
        return self.email

    objects = UserCustomManager()

    class Meta:
        verbose_name_plural = 'Пользователи'
        verbose_name = 'Пользователи'
        ordering = ['-email']




class Employee(Ret, models.Model): # Добавить def profile_photo(self, obj): return '<img src="%s" title="%s" />' % (resize_image(obj.photo, '100x100'), obj.title)
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    second_name = models.CharField(unique=True, max_length=100, verbose_name='Фамилия')
    photo = models.ImageField(verbose_name='Фото', blank=True)
    mobile = models.CharField(max_length=100, verbose_name='Телефон')
    mail = models.EmailField(unique=True, verbose_name='Почта')
    info = models.TextField( verbose_name='Информация')
    he = models.BooleanField (verbose_name='Высшее образование')
    salary = models.CharField(max_length=30, verbose_name='Зарплата')
    create_date = models.DateTimeField(db_index=True, verbose_name='Дата создания')
    address = models.ForeignKey('Address' , null=True, on_delete=models.PROTECT, blank=True, related_name='Адрес_работы')
    trole = models.ForeignKey('TotalRole', related_name='Права', on_delete=models.CASCADE,  null=True, blank=True)
    orderes = models.ManyToManyField('OrderTable', related_name='Заказы_работника', blank = True)
    experience = models.CharField(max_length=100, verbose_name='Опыт')
    user = models.ForeignKey('UserCustom', on_delete=models.PROTECT, related_name='Логин')
    useradd = models.ForeignKey('UserCustom' , null=False, on_delete=models.PROTECT, related_name='User', verbose_name='Добавил пользователь')
    

    def __str__(self):
        return self.second_name + ' ' + self.first_name + ' ' + self.trole.name

    class Meta:
        verbose_name_plural = 'Работник'
        verbose_name = 'Работник'
        ordering = ['second_name']


    



class Param(models.Model, Ret):
    height = models.CharField(max_length=20, verbose_name='Высота')
    width = models.CharField(max_length=20, verbose_name='Ширина')
    thickness = models.CharField(max_length=20, verbose_name='Толщина')
    weight = models.CharField(max_length=20, verbose_name='Вес')
    diagonal = models.CharField(max_length=20, verbose_name='Диагональ')
    mesh = models.ForeignKey('Mesh', null=True, on_delete=models.PROTECT, verbose_name='Материал')
    user = models.ForeignKey('UserCustom' , null=False, on_delete=models.PROTECT, related_name='User', verbose_name='Добавил пользователь')


    def __str__(self):
        return (self.height + 'x' + self.width + 'x' + self.thickness + '  вес:' + self.weight + '  диагональ:' + self.diagonal + ' материал:' + self.mesh.mesh + '-' + self.mesh.additional_mesh) 
    

    class Meta:
        verbose_name_plural = 'Параметры'
        verbose_name = 'Параметры'
        ordering = ['-weight']

class Office(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    mobile = models.CharField(max_length=20, verbose_name='Телефон')
    mail = models.CharField(max_length=50, verbose_name='Почта')
    info = models.TextField(verbose_name='Информация о офисе')
    this_company_office = models.BooleanField(db_index=True, verbose_name='Принадлежит этой компании')
    state_or_private = models.BooleanField(db_index=True, verbose_name='Госсударственная?')
    address = models.ForeignKey('Address', null=True, on_delete=models.PROTECT, verbose_name='Адрес')
    user = models.ForeignKey('UserCustom' , null=False, on_delete=models.PROTECT, related_name='User', verbose_name='Добавил пользователь')


    def __str__(self):
        return (self.name)

    class Meta:
        verbose_name_plural = 'Офис'
        verbose_name = 'Офис'
        ordering = ['-name']

class Factory(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    mobile = models.CharField(max_length=20, verbose_name='Телефон')
    mail = models.CharField(max_length=50, verbose_name='Почта')
    info = models.TextField(verbose_name='Информация о фабрике')
    count_empl = models.IntegerField(verbose_name='Колличество сотрудников')
    this_company_factory = models.BooleanField(db_index=True, verbose_name='Принадлежит этой компании')
    state_or_private = models.BooleanField(db_index=True, verbose_name='Госсударственная?')
    address = models.ForeignKey('Address', null=True, on_delete=models.PROTECT, verbose_name='Адрес')
    user = models.ForeignKey('UserCustom' , null=False, on_delete=models.PROTECT, related_name='User', verbose_name='Добавил пользователь')


    def __str__(self):
        return (self.name)

    class Meta:
        verbose_name_plural = 'Фабрикa'
        verbose_name = 'Фабрикa'
        ordering = ['-name']

class Storage(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    mobile = models.CharField(max_length=20, verbose_name='Телефон')
    mail = models.CharField(max_length=50, verbose_name='Почта')
    info = models.TextField(verbose_name='Информация о складе')
    full_content = models.CharField(max_length=50, verbose_name='Полная вместимость')
    content = models.IntegerField(verbose_name='Заполненность в %')
    this_company_storage = models.BooleanField(db_index=True, verbose_name='Принадлежит этой компании')
    state_or_private = models.BooleanField(db_index=True, verbose_name='Госсударственная?')
    address = models.ForeignKey('Address', null=True, on_delete=models.PROTECT, verbose_name='Адрес')
    user = models.ForeignKey('UserCustom' , null=False, on_delete=models.PROTECT, related_name='User', verbose_name='Добавил пользователь')


    def __str__(self):
        return (self.name)

    class Meta:
        verbose_name_plural = 'Склад'
        verbose_name = 'Склад'
        ordering = ['-name']

class Founders(models.Model, Ret):
    founders = models.CharField(max_length=50, verbose_name = 'Компания')
    founder = models.ManyToManyField('Founder', related_name='Основатель')
    user = models.ForeignKey('UserCustom' , null=False, on_delete=models.PROTECT, related_name='User', verbose_name='Добавил пользователь')


    def __str__(self): 
        return (self.founders + ' ('  + ' & '.join([str(foundr) for foundr in self.founder.all()])+ ')')

    class Meta:
        verbose_name_plural = 'Основатели'
        verbose_name = 'Основатели'
        ordering = ['-founders']

class Offices(models.Model, Ret):
    holding = models.CharField(max_length=50, verbose_name = 'Холдинг')
    office = models.ManyToManyField('Office', related_name='Офисы', verbose_name='Офисы')
    user = models.ForeignKey('UserCustom' , null=False, on_delete=models.PROTECT, related_name='User', verbose_name='Добавил пользователь')


    def __str__(self): 
        return (self.holding + ' ('  + ' & '.join([str(of) for of in self.office.all()]) + ')')  


    class Meta:
        verbose_name_plural = 'Офисы'
        verbose_name = 'Офисы'
        ordering = ['-holding']

class Factories(models.Model, Ret):
    holding = models.CharField(max_length=50, verbose_name = 'Холдинг')
    factory = models.ManyToManyField('Factory', related_name='Фабрики', verbose_name='Фабрики')  
    user = models.ForeignKey('UserCustom' , null=False, on_delete=models.PROTECT, related_name='User', verbose_name='Добавил пользователь')


    def __str__(self): 
        return (self.holding + ' ('  + ' & '.join([str(fac) for fac in self.factory.all()])+ ')')


    class Meta:
        verbose_name_plural = 'Фабрики'
        verbose_name = 'Фабрики'
        ordering = ['-holding']



class Storages(models.Model, Ret):
    holding = models.CharField(max_length=50, verbose_name = 'Холдинг')
    storage = models.ManyToManyField('Storage', related_name='Склады', verbose_name = 'Склады')
    user = models.ForeignKey('UserCustom' , null=False, on_delete=models.PROTECT, related_name='User', verbose_name='Добавил пользователь')


    def __str__(self): 
        return (self.holding + ' ('  + ' & '.join([str(s) for s in self.storage.all()])+ ')')
    

    class Meta:
        verbose_name_plural = 'Склады'
        verbose_name = 'Склады'
        ordering = ['-holding']




class FoundersCompanyOrganization(models.Model, Ret):
    companyname = models.CharField(max_length=50, verbose_name = 'Имя компании')
    founders = models.ManyToManyField('Founders', related_name='Основатели', verbose_name = 'Основатели')
    storages = models.ManyToManyField('Storages', related_name='Склады_компании', verbose_name = 'Склады', blank = True)
    factories = models.ManyToManyField('Factories', related_name='Фабрики_компании', verbose_name = 'Фабрики', blank = True)
    offices = models.ManyToManyField('Offices', related_name='Офисы_компании', verbose_name = 'Офисы', blank = True)
    user = models.ForeignKey('UserCustom' , null=False, on_delete=models.PROTECT, related_name='User', verbose_name='Добавил пользователь')


    def __str__(self): 
        return (self.companyname + ' ('  + ' & '.join([str(founder) for founder in self.founders.all()])+ ')')
    

    class Meta:
        verbose_name_plural = 'Таблица компаний'
        verbose_name = 'Таблица компаний'
        ordering = ['-companyname']

class Item(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    firm = models.ForeignKey('Firm', null=True, on_delete=models.PROTECT, verbose_name='Фирма')
    param = models.ForeignKey('Param', null=True, on_delete=models.PROTECT, verbose_name='Параметры')
    price = models.ForeignKey('Price', null=True, on_delete=models.PROTECT, verbose_name='Цена')
    create_date = models.DateTimeField(db_index=True, verbose_name='Дата создания')
    user = models.ForeignKey('UserCustom' , null=False, on_delete=models.PROTECT, related_name='User', verbose_name='Добавил пользователь')
    

    def __str__(self):
        return self.name   


    class Meta:
        verbose_name_plural = 'Вещь'
        verbose_name = 'Вещь'
        ordering = ['name']

class Items(models.Model):
    name_group = models.CharField (max_length=50, verbose_name='Название группы')
    item = models.ForeignKey('Item', null=True, on_delete=models.PROTECT, verbose_name='Предмет')
    count = models.IntegerField(verbose_name='Количество')
    user = models.ForeignKey('UserCustom' , null=False, on_delete=models.PROTECT, related_name='User', verbose_name='Добавил пользователь')

    
    def __str__(self):
        return (self.name_group + ' ' + self.item.name + ' количество' + str(self.count))

    class Meta:
        verbose_name_plural = 'Вещи'
        verbose_name = 'Вещи'
        ordering = ['name_group']

class ItemsSupplier(models.Model, Ret):
    name_group = models.CharField (max_length=50, verbose_name='Название группы') #Кастрюли
    items = models.ManyToManyField('Items', related_name='Вещи_доступные_поставщику', verbose_name='Вещи, доступные поставщику')
    user = models.ForeignKey('UserCustom' , null=False, on_delete=models.PROTECT, related_name='User', verbose_name='Добавил пользователь')


    def __str__(self):
        return self.name_group  


    class Meta:
        verbose_name_plural = 'Вещи, которые доступны от поставщика'
        verbose_name = 'Вещи, которые доступны от поставщика'
        ordering = ['name_group']

class ItemsInStorage(models.Model, Ret):
    storage = models.ForeignKey('Storage', null=True, on_delete=models.PROTECT, verbose_name='Склад')
    items = models.ManyToManyField('Items', related_name='Предметы' , verbose_name='Группы вещей на складе')
    user = models.ForeignKey('UserCustom' , null=False, on_delete=models.PROTECT, related_name='User', verbose_name='Добавил пользователь')


    class Meta:
        verbose_name_plural = 'Вещи на складе'
        verbose_name = 'Вещи на складе'
        ordering = ['storage']

class DeliveryTransport(models.Model):
    TRANSPORT = (
       ('S', 'Самолет'),
       ('V', 'Вертолет'),
       ('P', 'Поезд'),
       ('A', 'Автобус'),
       ('MA', 'Микроавтобус'),
       ('K', 'Корабль'),
    )
    model_name = models.CharField(max_length=50, verbose_name='Модель')
    type_of_transport = models.CharField(max_length=3, choices=TRANSPORT, verbose_name='Тип транспорта')
    year_constructed = models.CharField(max_length=12, verbose_name='Год создания')
    order_coast = models.CharField(max_length=50, verbose_name='Стоимость перевозки')
    ready = models.BooleanField(db_index=True, verbose_name='Готовность')
    time_delivery = models.CharField(max_length=50, verbose_name='Время Доставки')
    done_order = models.CharField(max_length=50, verbose_name='Рейсов выполненно')
    user = models.ForeignKey('UserCustom' , null=False, on_delete=models.PROTECT, related_name='User', verbose_name='Добавил пользователь')


    def __str__(self):
        return (self.type_of_transport + ' - ' + self.model_name)

    class Meta:
        verbose_name_plural = 'Доставляющий транспорт'
        verbose_name = 'Доставляющий транспорт'
        ordering = ['-type_of_transport']

class DeliveryInAWay(models.Model, Ret):
    transport = models.ForeignKey('DeliveryTransport', null=False, on_delete=models.PROTECT, related_name='Транспорт_доставки' , verbose_name='Транспорт доставки')
    items = models.ManyToManyField('Items', related_name='Вещи_в_пути' , verbose_name='Вещи в пути')
    user = models.ForeignKey('UserCustom' , null=False, on_delete=models.PROTECT, related_name='User', verbose_name='Добавил пользователь')


    class Meta:
        verbose_name_plural = 'Транспорт с грузом'
        verbose_name = 'Транспорт с грузом'
        ordering = ['transport']
    

class SupplierInfo(models.Model, Ret): 
    count_storages = models.IntegerField(verbose_name='Количество складов')
    average_time_delivery = models.TextField(verbose_name='Среднее время доставки')
    offices = models.ManyToManyField('Offices', related_name='Офисы_поставщика' , verbose_name='Офисы поставщика')
    storages = models.ManyToManyField('Storages', related_name='Склады_поставщика' , verbose_name='Склады поставщика')
    factories = models.ManyToManyField('Factories', related_name='Фабрики_поставщика' , verbose_name='Фабрики поставщика')
    delivery_transport = models.ManyToManyField('DeliveryTransport', related_name='Доставляющий_транспорт' , verbose_name='Доставляющий транспорт')
    text = models.TextField(verbose_name='Доп. информация')
    user = models.ForeignKey('UserCustom' , null=False, on_delete=models.PROTECT, related_name='User', verbose_name='Добавил пользователь')


    def __str__(self):
        return (self.average_time_delivery)

    class Meta:
        verbose_name_plural = 'Информация о поставщике'
        verbose_name = 'Информация о поставщике'
        ordering = ['count_storages']

class Supplier(models.Model, Ret):
    name = models.CharField(max_length=50, verbose_name='Название')
    mobile = models.CharField(max_length=50, verbose_name='Телефон')
    director = models.TextField(verbose_name='Директор')
    founderscompanyorganization = models.ManyToManyField('FoundersCompanyOrganization', related_name='Компании_организаторы' , verbose_name='Компании-организаторы')
    mail = models.EmailField(verbose_name='Почта')
    supplier_info = models.ForeignKey('SupplierInfo', null=False, on_delete=models.PROTECT, related_name='Информация_о_поставщике' , verbose_name='Информация о поставщике')
    items_supplier = models.ManyToManyField('ItemsSupplier', related_name='Постовляемые_вещи' , verbose_name='Поставляемые вещи')
    create_date = models.DateTimeField(db_index=True, verbose_name='Дата создания')
    connect_date = models.DateTimeField(db_index=True, verbose_name='Дата начала сотрудничества')
    user = models.ForeignKey('UserCustom' , null=False, on_delete=models.PROTECT, related_name='User', verbose_name='Добавил пользователь')


    def __str__(self):
        return (self.name)

    class Meta:
        verbose_name_plural = 'Поставщик'
        verbose_name = 'Поставщик'
        ordering = ['name']

class Ready(models.Model):
    ORDER = (('R', 'Ready'),
             ('W', 'Wait'),
             ('R-P', 'Ready-part'),
    )
    order_status = models.CharField(max_length=4, choices=ORDER, verbose_name='Статус')
    employee = models.ForeignKey('Employee', null=False, on_delete=models.PROTECT, related_name='Заказавший_работник', related_query_name='Работник' , verbose_name='Заказавший работник')
    address = models.ForeignKey('Address', null=False, on_delete=models.PROTECT, related_name='Адрес_доставки_товаров', related_query_name='Адрес_доставки_товаров' , verbose_name='Адрес доставки товаров')
    items = models.ForeignKey('Items', null=False, on_delete=models.PROTECT, related_name='Вещи_на_доставку', related_query_name='Вещи_на_доставку' , verbose_name='Вещи на доставку')
    total_price = models.CharField(max_length= 100, verbose_name='Полная стоимость')
    user = models.ForeignKey('UserCustom' , null=False, on_delete=models.PROTECT, related_name='User', verbose_name='Добавил пользователь')


    def __str__(self):
        return (self.items.name_group + ' ' + self.items.item.name + ' количество:' + str(self.items.count) + ' ' + self.employee.first_name + ' ' + self.employee.second_name + ' (' + '\n,'.join([p.name for p in self.employee.role.all()]) + ')-' + self.order_status)

    class Meta:
        verbose_name_plural = 'Статус заказа'
        verbose_name = 'Статус заказа'
        ordering = ['order_status']
 
class Orderes(models.Model, Ret):
    RECEIVED = (('Y', 'Да'),
                ('N', 'Нет'),
                ('N\A', 'Не определено')
    )
    orderes = models.ManyToManyField('Ready', related_name='Заказы', related_query_name='Заказы' , verbose_name='Заказы')
    total_price = models.CharField(max_length=50, verbose_name='Полная стоимость')
    supplier = models.ForeignKey('Supplier', null=False, on_delete=models.PROTECT, related_name='Поставщик_товара', related_query_name='Поставщик_товара' , verbose_name='Поставщик')
    storage = models.ForeignKey('Storage', null=False, on_delete=models.PROTECT, related_name='Склад_получатель', related_query_name='Склад_получатель' , verbose_name='Склад-получатель')
    send = models.BooleanField(verbose_name='Отправлено')
    received = models.CharField(max_length=3, choices=RECEIVED, verbose_name='Получено?')
    pos_one_get = models.CharField(max_length=3, choices=RECEIVED, verbose_name='Возможность одной доставки')
    date_send = models.DateTimeField(db_index=True, verbose_name='Дата отправки')
    date_get = models.DateTimeField(db_index=True, verbose_name='Дата получения')   
    user = models.ForeignKey('UserCustom' , null=False, on_delete=models.PROTECT, related_name='User', verbose_name='Добавил пользователь')


    def __str__(self):
        return (self.received + ' - ' + self.total_price)


    class Meta:
        verbose_name_plural = 'Заказы'
        verbose_name = 'Заказы'
        ordering = ['total_price']


