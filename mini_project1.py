import pandas as pd

bookings = pd.read_csv('https://stepik.org/media/attachments/lesson/360344/bookings.csv',encoding = 'windows-1251', sep = ';')
bookings_head = bookings[:7] #Выводит первые 7 строк датафрейма
print(bookings_head)
print(bookings.shape[1]) # Выводит количество столбцов в датафрейме
print(bookings.dtypes.value_counts()) # Выводит количество типов данных столбцов

def replace_space_with_star(name): # Фукнция для замены пробелов _ и нижним регистром
    new_name = name.replace(' ', '_')
    new_name = new_name.lower()
    return new_name

bookings = bookings.rename(columns = replace_space_with_star)
print(bookings) 
                        # Количество успешных бронирований по странам
bookings_succes_bron = bookings.query("is_canceled == 0") \
    .groupby(['country'], as_index = False) \
    .agg({'is_canceled': 'count'}) \
    .sort_values('is_canceled',ascending=False) \
    .head(5)
    
print(bookings_succes_bron)

bookings_count_bron = bookings.groupby(['hotel'], as_index = False) \
    .agg({'stays_total_nights': 'mean'}) \
    .sort_values('stays_total_nights',ascending=False) \
    .head(5)

print(bookings_count_bron.round(2))

over_booking = bookings.query("assigned_room_type != reserved_room_type") \
    .agg({'assigned_room_type': 'count'})

print(over_booking)

bron_month = bookings.query("is_canceled == 0") \
    .groupby(['arrival_date_year', 'arrival_date_month'], as_index = False) \
    .agg({'is_canceled': 'count'}) \
    .sort_values(['is_canceled'],ascending=False) 
    
print(bron_month)

                    #Отмена бронирования отеля
bron_month_cancel = bookings.query("is_canceled == 1") \
    .groupby(['arrival_date_year', 'arrival_date_month'], as_index = False) \
    .agg({'is_canceled': 'count'}) \
    .sort_values(['is_canceled'],ascending=False) 
    
print(bron_month_cancel)


                    #Среднее значение adults, children, babies
average_a_c_b = bookings.agg({'adults': 'mean', 'children': 'mean', 'babies': 'mean' }).idxmax()
print(average_a_c_b)

                    #Добавление новых колонок, с объединением стобцов

#union_column = bookings[['children', 'babies']].apply(lambda x: ' '.join(x), axis = 1) 
#print(union_column)
bookings['total_kids'] = bookings['children'] + bookings['babies'] 
insert_bookings = bookings.groupby(['hotel'], as_index = False) \
    .agg({'total_kids': 'mean'}) \
    .sort_values(['total_kids'],ascending=False) 
    
print(insert_bookings.round(2))
