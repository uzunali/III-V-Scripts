from Newport_844_PE import Newport_844_PE

np844 = Newport_844_PE()

np844.initialize_dev()

first_data = True
for i in range(10):
    np844.get_data(first_data)
    first_data = False
np844.set_range(1)
np844.close_connection()

