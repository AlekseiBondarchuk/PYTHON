Создать функцию, которая генерирует конфигурацию для trunk-портов.

Параметр trunk - это словарь trunk-портов.

Словарь trunk имеет такой формат (тестовый словарь trunk_dict уже создан):

    { 'FastEthernet0/1':[10,20],
      'FastEthernet0/2':[11,30],
      'FastEthernet0/4':[17] }
        
Функция должна возвращать список команд с конфигурацией на основе указанных портов и шаблона trunk_template.

В конце строк в списке не должно быть символа перевода строки.

Проверить работу функции на примере словаря trunk_dict.

    def generate_trunk_config(trunk):
    """
    trunk - словарь trunk-портов для которых необходимо сгенерировать конфигурацию.
    Возвращает список всех команд, которые были сгенерированы на основе шаблона
    """
    
    trunk_template = ['switchport trunk encapsulation dot1q',
                      'switchport mode trunk',
                      'switchport trunk native vlan 999',
                      'switchport trunk allowed vlan']
    trunk_dict = { 'FastEthernet0/1':[10,20,30],
                   'FastEthernet0/2':[11,30],
                   'FastEthernet0/4':[17] }

Сделать копию скрипта задания ex_2

Изменить скрипт таким образом, чтобы функция возвращала не список команд, а словарь:

  ключи: имена интерфейсов, вида 'FastEthernet0/1';
  значения: список команд, который надо выполнить на этом интерфейсе.

Проверить работу функции на примере словаря trunk_dict.

    def generate_trunk_config(trunk):
    """
    trunk - словарь trunk-портов,
    для которых необходимо сгенерировать конфигурацию, вида:
    
    { 'FastEthernet0/1':[10,20],
    'FastEthernet0/2':[11,30],
    'FastEthernet0/4':[17] }
    Возвращает словарь:
    - ключи: имена интерфейсов, вида 'FastEthernet0/1'
    - значения: список команд, который надо выполнить на этом интерфейсе
    """
    trunk_template = ['switchport trunk encapsulation dot1q',
                      'switchport mode trunk',
                      'switchport trunk native vlan 999',
                      'switchport trunk allowed vlan']
    trunk_dict = { 'FastEthernet0/1':[10,20,30],
                    'FastEthernet0/2':[11,30],
                    'FastEthernet0/4':[17] }
