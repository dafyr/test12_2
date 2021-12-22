import re

data_str = "23 Авг, 1978"
result = re.search(r'[123|]\d (Янв|Фев|Мар|Апр|Май|Июн|Июл|Авг|Сен|Окт|Дек)+, 
\d\d\d\d*', data_str)
print(result.group(0))