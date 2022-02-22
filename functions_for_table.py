def list_generate(rows: int, columns: int, value=0) -> list:
    """
    generate a list rows left columns and fill every element with value
    :param rows: number of lists in main list (row lists)
    :param columns: number of lists in every row list (column lists)
    :param value: filling of every column list
    :return: generated list
    """
    generated_list = []
    for i in range(0, rows):
        generated_list.append([value] * columns)
    return generated_list
