from table import Table


def next_cur_pos(keysym: str, table: Table):
    """move cursor on keys"""
    if keysym == 'Up':
        table.cur_pos[1] -= 1
    if keysym == 'Down':
        table.cur_pos[1] += 1
    if keysym == 'Right':
        table.cur_pos[0] += 1
    if keysym == 'Left':
        table.cur_pos[0] -= 1
    table.move_cursor(table.cur_pos[1] % table.rows, table.cur_pos[0] % table.columns)


def analyze_value(n_value, table: Table):
    """check input value in current cell"""
    cur_value = table.table_list[table.cur_pos[1]][table.cur_pos[0]]
    if not (((n_value.isdigit() and len(cur_value) <= 4) or (n_value.isdigit() and
                                                             len(cur_value) == 5 and cur_value.count('.') == 1)) or
            (n_value == '.' and cur_value.count('.') == 0 and 0 < len(cur_value) <= 4)):
        return False
    return True


def new_value(value, table: Table):
    """set new value for current cell in table"""
    table.change_value(table.cur_pos, value)


def del_num(table: Table):
    """delete one char from current cell in table"""
    cur_value = table.table_list[table.cur_pos[1] % table.rows][table.cur_pos[0] % table.columns]
    if len(cur_value) != 0:
        table.table_list[table.cur_pos[1]][table.cur_pos[0]] = cur_value[:-1]
        table.draw_table()
