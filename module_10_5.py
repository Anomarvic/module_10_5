from multiprocessing import Pool
import time

def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf8') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line.strip())

filenames = [f'./file {number}.txt' for number in range(1, 5)]

if __name__ == '__main__':
    # Линейный вызов
    start_time_linear = time.time()
    for filename in filenames:
        read_info(filename)
    end_time_linear = time.time()
    print(f'{end_time_linear - start_time_linear} (линейный)')

    # Многопроцессный
    start_time_multiprocessing = time.time()
    with Pool() as p:
        p.map(read_info, filenames)
    end_time_multiprocessing = time.time()
    print(f'{end_time_multiprocessing - start_time_multiprocessing} (многопроцессный)')