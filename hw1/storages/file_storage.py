import os


class FileStorage(object):
    '''
    Class for reading data from or saving data to a specified file
    '''

    def __init__(self, file_name):
        self.file_name = file_name

    def read_data(self):
        if not os.path.exists(self.file_name):
            raise StopIteration

        with open(self.file_name, 'rb') as f:
            for line in f:
                yield line.strip()

    def write_data(self, data_array):
        """
        :param data_array: collection of strings that
        should be written as lines
        """
        with open(self.file_name, 'wb') as f:
            for line in data_array:
                if line.decode('utf-8').endswith('\n'):
                    f.write(line)
                else:
                    f.write(line + '\n')

    def append_data(self, data):
        """
        :param data: string to append
        """
        with open(self.file_name, 'ab') as f:
            for line in data:
                if line.decode('utf-8').endswith('\n'):
                    f.write(line)
                else:
                    f.write(line + '\n')
