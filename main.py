import models

models.XRate.create_table()
models.XRate.create(from_currency=900, to_currency=840, rate=25)