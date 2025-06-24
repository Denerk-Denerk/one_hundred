import csv
def dict_sotka_stat(name_file):
    users_stat = []
    with open(name_file) as f:
        reader = csv.DictReader(f, delimiter=';')
        for row in reader:
            users_stat.append(row)
        return users_stat
    

def render_stat_of_the_day(dict_stat):
    strok = '-' * 28
    sum_stat = {}
    stat = {}
    TEMPLATE = []
    names = {'Denerk':"Денис",'wellspringweather': 'Виталик','Kron3583': 'Тима'}
    stats = {'Denerk':[],'wellspringweather': [],'Kron3583': []}
    for row in dict_stat:
        username = row['username']
        if username not in sum_stat:
            sum_stat[username] = [0, 0, 0, 0]
        pull_ups = int(row.get('pull_ups'))*4
        squats_1 = int(row.get('squats_1'))*4
        push_ups = int(row.get('push_ups'))*4
        squats_2 = int(row.get('squats_2'))*4

        stat.update({username: [pull_ups, squats_1, push_ups, squats_2]})

        sum_stat[username][0] += pull_ups
        sum_stat[username][1] += squats_1
        sum_stat[username][2] += push_ups
        sum_stat[username][3] += squats_2
        
        date = row['date']
        stats[username].append([date,stat[username]])
        stat = {}

    for us in stats:
        TEMPLATE.append(f"{'Дата':^6}|{names[us]:^20}|\n")
        for gg in stats[us]:
            TEMPLATE.append(f'{gg[0]:^6}|{gg[1][0]:^5}{gg[1][1]:^5}{gg[1][2]:^5}{gg[1][3]:^5}|\n')
        TEMPLATE.append(f"{'Всего':^6}|{sum_stat[us][0]:^5}{sum_stat[us][1]:^5}{sum_stat[us][2]:^5}{sum_stat[us][3]:^5}|\n")
                        
    return f'{strok}\n'.join(TEMPLATE)