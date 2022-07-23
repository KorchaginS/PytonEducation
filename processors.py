class Processor:
    def __init__(self, reader, writer):
        self.reader = reader
        self.writer = writer

    def Process(self):
        while True:
            data = self.reader.readline()
            if not data: break
            data = self.converted(data)
            self.writer.write(data)

    def converter(self, data):
        assert False, 'converter must be defined'

