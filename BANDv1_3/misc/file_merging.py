import os

def merge_files_by_timestamp(large_file_path, small_file_path):

    with open(large_file_path, 'r') as large_file, open(small_file_path, 'r') as small_file:
        large_lines = large_file.readlines()
        small_lines = small_file.readlines()

    merged_lines = []

    small_file_dict = {}
    for line in small_lines:
        timestamp = line.split(',')[0]
        small_file_dict[timestamp] = line.strip()

    for large_line in large_lines:
        timestamp = large_line.split(',')[0]
        if timestamp in small_file_dict:
            merged_line = large_line.strip() + ',' + ','.join(small_file_dict[timestamp].split(',')[1:])
        else:
            merged_line = large_line.strip()
        
        merged_lines.append(merged_line)

    with open(large_file_path, 'w') as large_file:
        for line in merged_lines:
            large_file.write(line + '\n')

    #os.remove(small_file_path)
    os.rename("sensors/received_data.txt", "sensors/ride_complete.txt")
    print(f'Merged content written to {large_file_path}. {small_file_path} has been deleted.')


