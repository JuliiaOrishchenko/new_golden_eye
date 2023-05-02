import models

models.XRate.create_table()
models.XRate.create(from_currency=900, to_currency=840, rate=25)
models.XRate.create(from_currency=840, to_currency=643, rate=80)
models.XRate.create(from_currency=643, to_currency=840, rate=79)