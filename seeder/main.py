from faker import Factory
import requests


def create_person(faker):
    return {
        "name": faker.name(),
        "address": faker.address(),
        "info": faker.text(),
        "company": faker.company(),
        "birthday": faker.date_time_between(start_date="-50y", end_date="-20y").isoformat(),
        "phone": faker.phone_number(),
        "cc_number": faker.credit_card_number(),
        "email": faker.email(),
        "username": faker.user_name()
    }

def main():
    faker = Factory.create()
    database_name = 'test'
    url = 'http://localhost:5984/{}'.format(database_name)
    for _ in range(0, 500):
        person = create_person(faker)
        res = requests.post(url, json=person)
        if res.status_code == 201:
            print "Inserted a row !"
        else:
            print res.content
            return False
    print "Everything is done !"


if __name__ == "__main__":
    main()
