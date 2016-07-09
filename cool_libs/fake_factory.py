from faker import Factory

fake = Factory.create()
fake.seed(123)
fname, lname = fake.name().split()
print fname, lname