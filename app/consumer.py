from kafka import KafkaConsumer
consumer = KafkaConsumer(
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=False,
    api_version=(3, 8)
)

print(consumer.bootstrap_connected())