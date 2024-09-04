from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    api_version=(3, 8)
)
print(producer.bootstrap_connected())
while True:
    _input = input('message: ')
    print(_input)
    producer.send("my-topic", value=_input.encode("utf-8"))
    print(_input)