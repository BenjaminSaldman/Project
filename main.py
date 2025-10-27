from src.services import decryptor, data_receiver, language_detector, translator
from src.utils import Pipeline


def main():
    data_receiver_iterator = data_receiver.receive_data()

    pipeline = Pipeline()
    (pipeline
     .add_stage(decryptor)
     .add_stage(language_detector)
     .add_stage(translator))

    for data in data_receiver_iterator:
        pipeline.run(data)


if __name__ == '__main__':
    main()
